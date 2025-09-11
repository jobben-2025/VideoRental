# Main project file

# Video Rental System

# 🎯 Goal
# Students will build a console-based system for renting movies, returning them, and managing members.

# 🔑 Learning Focus
# Classes: Video, Customer, VideoStore
# Functions: rent, return, search, list
# Collections: use of dict and list for efficient management

# 🎯 Learning Objectives
# By the end of this project, students will be able to:
# Apply Object-Oriented Programming (OOP) principles by creating and using classes (Video, Customer, VideoStore).
# Encapsulate functionality inside methods (e.g., rent, return, search, list).
# Use Python collections (list, dict) to store and retrieve structured data efficiently.
# Implement control flow with conditions and loops to manage system operations.
# Design modular code by splitting responsibilities across classes and functions.
# Collaborate in groups, practice version control (if used), and present solutions.

# 🗓️ Weekly Breakdown
# Day 1: Define Classes
#   Video: attributes → title, genre, video_id, available (bool).
#   Customer: attributes → name, customer_id, rented_videos (list).
#   VideoStore: manages collections of videos and customers.
# Day 1–3: Implement Core Functions
#   In the VideoStore class:
#   add_video(video) – add a new movie.
#   add_customer(customer) – register a new customer.
#   rent_video(customer_id, video_id) – customer rents if available.
#   return_video(customer_id, video_id) – customer returns a video.
#   list_available_videos() – show available movies.
#   list_customer_videos(customer_id) – show what a customer has rented.
# Day 3–6: Extensions (Group Work)
#   Encourage groups to add one or two enhancements:
#   Search feature: by title or genre.
#   Late fee system: calculate fee if not returned on time.
#   Ratings system: customers rate videos.
#   Collections: Use a dict for quick lookups (e.g. video_id -> Video).
# Day 7: Presentation & Review
#   Groups demo renting/returning videos.
#   Discuss use of OOP + collections.
#   Compare different extensions.


######################### CLASSES #########################
class Video:
    def __init__(self, video_id: str, title: str, genre: str, year: int, available: bool = True):
        self.video_id = video_id
        self.title = title
        self.genre = genre
        self.year = year
        self.available = available
        # <----- here I changed: removed any class-level lists because Inconsistency : VideoStore should be the single source of truth

    def __str__(self):
        return f"{self.video_id} | {self.title} ({self.year}) [{self.genre}] - {'Available' if self.available else 'Not Available'}"

    # <----- here I changed: make availability check side-effect free because Inconsistency : previous versions sometimes toggled state while 'checking'
    def check_availability(self) -> str:
        return f"{self.title} is {'available' if self.available else 'not available'}."


class Customer:
    def __init__(self, customer_id: str, name: str):
        # unique identifier for the customer
        self.customer_id = customer_id
        # customer's full name
        self.name = name
        # list of video IDs currently rented by this customer (store video_ids as strings)
        self.rented_videos = []

    def rent(self, video_id: str):
        """Add a video id to the list of rented videos."""
        if video_id not in self.rented_videos:
            self.rented_videos.append(video_id)

    def return_video(self, video_id: str):
        """Remove a video id from the list of rented videos."""
        if video_id in self.rented_videos:
            self.rented_videos.remove(video_id)

    def __str__(self):
        return f"Customer[{self.customer_id}]: {self.name}, rented={self.rented_videos}"


class VideoStore:
    """
    Minimal list-based store for videos and customers.
    (Kept simple to match the course scope; could be upgraded to dicts later.)
    """
    def __init__(self, videos=None, customers=None):
        self.videos = videos if videos is not None else []
        self.customers = customers if customers is not None else []

        # type safety
        if not all(isinstance(v, Video) for v in self.videos):
            raise TypeError("All elements of 'videos' must be instances of Video.")
        if not all(isinstance(c, Customer) for c in self.customers):
            raise TypeError("All elements of 'customers' must be instances of Customer.")

    def add_video(self, video):
        if not isinstance(video, Video):
            raise TypeError("Only Video instances can be added.")
        # prevent duplicate IDs (critical for reliable lookups)
        if any(v.video_id == video.video_id for v in self.videos):
            raise ValueError(f"Video ID '{video.video_id}' already exists.")
        self.videos.append(video)

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Only Customer instances can be added.")
        # prevent duplicate customer IDs
        if any(c.customer_id == customer.customer_id for c in self.customers):
            raise ValueError(f"Customer ID '{customer.customer_id}' already exists.")
        self.customers.append(customer)

    # --- helpers ---
    def _find_customer(self, customer_id: str):
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def _find_video(self, video_id: str):
        for v in self.videos:
            if v.video_id == video_id:
                return v
        return None

    # --- core actions ---
    def rent_video(self, customer_id: str, video_id: str) -> bool:
        """Customer rents if video exists, customer exists, and video is available."""
        customer = self._find_customer(customer_id)
        video = self._find_video(video_id)
        if customer is None or video is None:
            return False  # invalid IDs
        if not video.available:
            return False  # already rented
        video.available = False
        customer.rent(video_id)
        return True

    def return_video(self, customer_id: str, video_id: str) -> bool:
        """Customer returns a video if both exist and the customer has it."""
        customer = self._find_customer(customer_id)
        video = self._find_video(video_id)
        if customer is None or video is None:
            return False  # invalid IDs
        if video_id not in customer.rented_videos:
            return False  # customer didn't rent this video
        video.available = True
        customer.return_video(video_id)
        return True

    # --- listings ---
    def list_available_videos(self):
        return [v for v in self.videos if v.available]

    def list_customer_videos(self, customer_id: str):
        customer = self._find_customer(customer_id)
        if customer is None:
            return []
        # map video_ids to Video objects (if still present)
        id_set = set(customer.rented_videos)
        return [v for v in self.videos if v.video_id in id_set]

    # --- stretch: search ---
    def search(self, title: str = "", genre: str = ""):
        """Search by title (substring, case-insensitive) and/or genre (exact, case-insensitive)."""
        t = title.strip().lower()
        g = genre.strip().lower()
        results = []
        for v in self.videos:
            ok_t = (not t) or (t in v.title.lower())
            ok_g = (not g) or (g == v.genre.lower())
            if ok_t and ok_g:
                results.append(v)
        return results


#######################################################################
###### Code Text File Save  ###########################################
#######################################################################
# This section implements a very simple, human-readable persistence.
# We use two plain text files: one for videos, one for customers.
# Each new item is appended as a single line using a stable delimiter ("|").
#
# Why only the catalog (videos/customers) in files?
# - It avoids complex synchronization problems for rentals/availability.
# - Rentals (who has what) and availability are dynamic and change often.
# - Keeping those in memory ensures the "business logic" is the single source of truth.
#
# File formats:
#   videostore.txt   ->  video_id|title|genre|year
#   customers.txt    ->  customer_id|name
#
# On startup:
#   - We load both files (if they exist) and build the initial store lists.
# When adding:
#   - We append the new video/customer to the corresponding file.
#
# Note:
#   - If two teammates add lines in parallel and push via Git, merges may be required.
#   - For a small project this is fine; for bigger systems use JSON/SQLite later.
import os

VIDEO_FILE = "videostore.txt"
CUSTOMER_FILE = "customers.txt"

def save_video_to_file(video: Video):
    """
    Append a single video to videostore.txt in the format:
      video_id|title|genre|year
    We intentionally do NOT store 'available' here to keep files as a pure catalog.
    """
    line = f"{video.video_id}|{video.title}|{video.genre}|{video.year}\n"
    with open(VIDEO_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def save_customer_to_file(customer: Customer):
    """
    Append a single customer to customers.txt in the format:
      customer_id|name
    """
    line = f"{customer.customer_id}|{customer.name}\n"
    with open(CUSTOMER_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def load_videos_from_file():
    """
    Read all videos from videostore.txt and return a list[Video].
    If the file doesn't exist yet, return an empty list.
    All loaded videos start as available=True (catalog only).
    """
    videos = []
    if not os.path.exists(VIDEO_FILE):
        return videos

    with open(VIDEO_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) != 4:
                # Skip malformed lines rather than crashing.
                continue
            video_id, title, genre, year_str = parts
            try:
                year = int(year_str)
            except ValueError:
                # If year isn't a number, default to 0.
                year = 0
            videos.append(Video(video_id, title, genre, year, available=True))
    return videos

def load_customers_from_file():
    """
    Read all customers from customers.txt and return a list[Customer].
    If the file doesn't exist yet, return an empty list.
    """
    customers = []
    if not os.path.exists(CUSTOMER_FILE):
        return customers

    with open(CUSTOMER_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) != 2:
                continue
            customer_id, name = parts
            customers.append(Customer(customer_id, name))
    return customers
#######################################################################
###### End of Code Text File Save #####################################
#######################################################################


######################### FUNCTIONS (CLI) #########################
# Initialize the store by loading from files (if present).
# We pass the loaded lists into VideoStore so the app starts with existing data.
VideoCollection1 = VideoStore(
    videos=load_videos_from_file(),
    customers=load_customers_from_file()
)

def first_add_video():
    print("\n1. Add a video to system\n")
    global VideoCollection1

    new_video_id = input("Video ID: ").strip()
    if not new_video_id:
        print("❌ Video ID cannot be empty.")
        return

    title = input("Title: ").strip()
    if not title:
        print("❌ Title cannot be empty.")
        return

    genre = input("Genre: ").strip()
    if not genre:
        print("❌ Genre cannot be empty.")
        return

    year_raw = input("Year (e.g., 1999): ").strip()
    try:
        year = int(year_raw)
    except ValueError:
        print("❌ Year must be a number.")
        return

    try:
        new_video = Video(new_video_id, title, genre, year, available=True)
        VideoCollection1.add_video(new_video)
        save_video_to_file(new_video)  # persist so the catalog survives restarts
        print("✅ Video added and saved to videostore.txt.")
    except (TypeError, ValueError) as e:
        print(f"❌ {e}")

def second_add_customer():
    print("\n2. Add a customer to system\n")
    global VideoCollection1

    new_customer_id = input("Customer ID: ").strip()
    if not new_customer_id:
        print("❌ Customer ID cannot be empty.")
        return

    new_customer_name = input("Name: ").strip()
    if not new_customer_name:
        print("❌ Name cannot be empty.")
        return

    try:
        new_customer = Customer(new_customer_id, new_customer_name)
        VideoCollection1.add_customer(new_customer)
        save_customer_to_file(new_customer)  # persist so customers survive restarts
        print("✅ Customer added and saved to customers.txt.")
    except (TypeError, ValueError) as e:
        print(f"❌ {e}")

def third_customer_rent_video():
    print("\n3. Customer rent-a-video\n")
    global VideoCollection1

    cid = input("Customer ID: ").strip()
    if not cid:
        print("❌ Customer ID cannot be empty.")
        return

    vid = input("Video ID: ").strip()
    if not vid:
        print("❌ Video ID cannot be empty.")
        return

    ok = VideoCollection1.rent_video(cid, vid)
    if ok:
        print("🎬 Rented successfully.")
    else:
        # helpful explanation
        customer = VideoCollection1._find_customer(cid)
        video = VideoCollection1._find_video(vid)
        if customer is None:
            print("❌ Rent failed: customer not found.")
        elif video is None:
            print("❌ Rent failed: video not found.")
        elif not video.available:
            print(f"❌ Rent failed: '{video.title}' is not available.")
        else:
            print("❌ Rent failed.")

def fourth_customer_return_video():
    print("\n4. Customer return-video\n")
    global VideoCollection1

    cid = input("Customer ID: ").strip()
    if not cid:
        print("❌ Customer ID cannot be empty.")
        return

    vid = input("Video ID: ").strip()
    if not vid:
        print("❌ Video ID cannot be empty.")
        return

    ok = VideoCollection1.return_video(cid, vid)
    if ok:
        print("🔙 Returned successfully.")
    else:
        customer = VideoCollection1._find_customer(cid)
        video = VideoCollection1._find_video(vid)
        if customer is None:
            print("❌ Return failed: customer not found.")
        elif video is None:
            print("❌ Return failed: video not found.")
        elif vid not in customer.rented_videos:
            print("❌ Return failed: this customer does not have that video.")
        else:
            print("❌ Return failed.")

def fifth_show_avail_videos():
    print("\n5. Show 'available' videos\n")
    global VideoCollection1
    videos = VideoCollection1.list_available_videos()
    if not videos:
        print("(none)")
    else:
        for v in videos:
            print(str(v))

def sixth_show_rented_videos():
    print("\n6. Show rented videos by customer\n")
    global VideoCollection1
    cid = input("Customer ID: ").strip()
    if not cid:
        print("❌ Customer ID cannot be empty.")
        return
    videos = VideoCollection1.list_customer_videos(cid)
    if not videos:
        print("(none or customer not found)")
    else:
        customer = VideoCollection1._find_customer(cid)
        header = f"{customer.name} ({cid})" if customer else cid
        print(f"Customer {header} has rented:")
        for v in videos:
            print(str(v))

def seventh_search_videos():
    print("\n7. Search videos\n")
    global VideoCollection1
    title = input("Title contains (optional): ").strip()
    genre = input("Genre equals (optional): ").strip()
    results = VideoCollection1.search(title=title, genre=genre)
    if not results:
        print("(no matches)")
    else:
        for v in results:
            print(str(v))


######################### MENU #########################
def main_menu():
    while True:
        print("\nWelcome to Video Rental Store (VRS)\n")
        print("1. Add a video to system")
        print("2. Add a customer to system")
        print("3. Customer rent-a-video")
        print("4. Customer return-video")
        print("5. Show 'available' videos")
        print("6. Show rented videos by customer")
        print("7. Search videos")
        print("\n8. Exit program\n")

        choice_raw = input("Please choose menu option to proceed: ").strip()
        try:
            choice = int(choice_raw)
        except ValueError:
            print("Please enter a number 1-8!")
            continue

        if choice == 1:
            first_add_video()
        elif choice == 2:
            second_add_customer()
        elif choice == 3:
            third_customer_rent_video()
        elif choice == 4:
            fourth_customer_return_video()
        elif choice == 5:
            fifth_show_avail_videos()
        elif choice == 6:
            sixth_show_rented_videos()
        elif choice == 7:
            seventh_search_videos()
        elif choice == 8:
            confirm = input("Are you sure you want to exit? (y/n) ").strip().lower()
            if confirm == "y":
                print("Bye!")
                return
        else:
            print("Please enter a number 1-8!")


######################### ENTRYPOINT #########################
if __name__ == "__main__":
    # We load from files on startup, so no seeding here.
    # If the files don't exist yet, you'll start with an empty catalog.
    main_menu()
