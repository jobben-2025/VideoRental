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
# Video: attributes → title, genre, video_id, available (bool).
# Customer: attributes → name, customer_id, rented_videos (list).
# VideoStore: manages collections of videos and customers.

# Day 1–3: Implement Core Functions
# In the VideoStore class:
# add_video(video) – add a new movie.
# add_customer(customer) – register a new customer.
# rent_video(customer_id, video_id) – customer rents if available.
# return_video(customer_id, video_id) – customer returns a video.
# list_available_videos() – show available movies.
# list_customer_videos(customer_id) – show what a customer has rented.

# Day 3–6: Extensions (Group Work)
# Encourage groups to add one or two enhancements:
# Search feature: by title or genre.
# Late fee system: calculate fee if not returned on time.
# Ratings system: customers rate videos.
# Collections: Use a dict for quick lookups (e.g. video_id -> Video).

# Day 7: Presentation & Review
# Groups demo renting/returning videos.
# Discuss use of OOP + collections.
# Compare different extensions.


######################### CLASSES #########################
class Video:
    def __init__(self, video_id: str, title: str, genre: str, year: int, available: bool = True):
        self.video_id = video_id
        self.title = title
        self.genre = genre
        self.year = year
        self.available = available

    def __str__(self):
        return f"{self.video_id} | {self.title} ({self.year}) [{self.genre}] - {'Available' if self.available else 'Not Available'}"

    def check_availability(self) -> str:
        return f"{self.title} is {'available' if self.available else 'not available'}."


class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.rented_videos = []  # store video_ids (strings)

    def rent(self, video_id: str):
        if video_id not in self.rented_videos:
            self.rented_videos.append(video_id)

    def return_video(self, video_id: str):
        if video_id in self.rented_videos:
            self.rented_videos.remove(video_id)

    def __str__(self):
        return f"Customer[{self.customer_id}]: {self.name}, rented={self.rented_videos}"


class VideoStore:
    def __init__(self, videos=None, customers=None):
        self.videos = videos if videos is not None else []
        self.customers = customers if customers is not None else []

        if not all(isinstance(v, Video) for v in self.videos):
            raise TypeError("All elements of 'videos' must be instances of Video.")
        if not all(isinstance(c, Customer) for c in self.customers):
            raise TypeError("All elements of 'customers' must be instances of Customer.")

    def add_video(self, video):
        if not isinstance(video, Video):
            raise TypeError("Only Video instances can be added.")
        if any(v.video_id == video.video_id for v in self.videos):
            raise ValueError(f"Video ID '{video.video_id}' already exists.")
        self.videos.append(video)

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Only Customer instances can be added.")
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

    # --- rent / return ---
    def rent_video(self, customer_id: str, video_id: str) -> bool:
        """Rent a video to a customer if both exist and the video is available."""
        customer = self._find_customer(customer_id)
        video = self._find_video(video_id)

        if customer is None or video is None:
            return False
        if not video.available:
            return False

        video.available = False
        customer.rent(video_id)
        return True

    def return_video(self, customer_id: str, video_id: str) -> bool:
        """Return a rented video if customer & video exist and mapping is valid."""
        customer = self._find_customer(customer_id)
        video = self._find_video(video_id)

        if customer is None or video is None:
            return False
        if video_id not in customer.rented_videos:
            return False

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
        id_set = set(customer.rented_videos)
        return [v for v in self.videos if v.video_id in id_set]


######################### FUNCTIONS #########################
# holds videos, customer data of VideoStore class
global VideoCollection1
VideoCollection1 = VideoStore()

def first_add_video():
    print("\n1. Add a video to system\n")
    print("Please enter the details of the video below.")
    global VideoCollection1

    new_video_id = input("Video ID: ").strip()
    title = input("Title: ").strip()
    genre = input("Genre: ").strip()

    year_raw = input("Year (e.g., 1999): ").strip()
    try:
        year = int(year_raw)
    except ValueError:
        print("Year must be a number. Setting year = 0.")
        year = 0

    try:
        VideoCollection1.add_video(Video(new_video_id, title, genre, year, available=True))
        print("✅ Video added.")
    except (TypeError, ValueError) as e:
        print(f"❌ {e}")

    again = input("Do you want to enter another video? (y/n) ").strip().lower()
    if again == "y":
        first_add_video()
    else:
        main_menu()

def second_add_customer():
    print("\n2. Add a customer to system\n")
    print("Please enter the details of the customer below.")
    global VideoCollection1

    new_customer_id = input("Customer ID: ").strip()
    new_customer_name = input("Name: ").strip()

    try:
        VideoCollection1.add_customer(Customer(new_customer_id, new_customer_name))
        print("✅ Customer added.")
    except (TypeError, ValueError) as e:
        print(f"❌ {e}")

    again = input("Do you want to enter another customer? (y/n) ").strip().lower()
    if again == "y":
        second_add_customer()
    else:
        main_menu()

def third_customer_rent_video():
    print("\n3. Customer rent-a-video\n")
    global VideoCollection1

    cid = input("Customer ID: ").strip()
    vid = input("Video ID: ").strip()

    ok = VideoCollection1.rent_video(cid, vid)
    if ok:
        print("🎬 Rented successfully.")
    else:
        print("❌ Rent failed (check IDs / availability).")

    input("Press Enter to return to menu...")
    main_menu()

def fourth_customer_return_video():
    print("\n4. Customer return-video\n")
    global VideoCollection1

    cid = input("Customer ID: ").strip()
    vid = input("Video ID: ").strip()

    ok = VideoCollection1.return_video(cid, vid)
    if ok:
        print("🔙 Returned successfully.")
    else:
        print("❌ Return failed (check IDs / possession).")

    input("Press Enter to return to menu...")
    main_menu()

def fifth_show_avail_videos():
    print("\n5. Show 'available' videos\n")
    global VideoCollection1
    videos = VideoCollection1.list_available_videos()
    if not videos:
        print("(none)")
    else:
        for v in videos:
            print(str(v))
    input("\nPress Enter to return to menu...")
    main_menu()

def sixth_show_rented_videos():
    print("\n6. Show rented videos by customer\n")
    global VideoCollection1
    cid = input("Customer ID: ").strip()
    videos = VideoCollection1.list_customer_videos(cid)
    if not videos:
        print("(none or customer not found)")
    else:
        for v in videos:
            print(str(v))
    input("\nPress Enter to return to menu...")
    main_menu()


def main_menu():
    try:
        print("\nWelcome to Video Rental Store (VRS)\n")
        print("1. Add a video to system")
        print("2. Add a customer to system")
        print("3. Customer rent-a-video")
        print("4. Customer return-video")
        print("5. Show 'available' videos")
        print("6. Show rented videos by customer")
        print("\n7. Exit program\n")

        menu_selection = input("Please choose menu option to proceed: ").strip()
        try:
            menu_selection = int(menu_selection)
            selection = True
        except ValueError:
            selection = False

        if selection:
            if menu_selection == 1:
                first_add_video()
            elif menu_selection == 2:
                second_add_customer()
            elif menu_selection == 3:
                third_customer_rent_video()
            elif menu_selection == 4:
                fourth_customer_return_video()
            elif menu_selection == 5:
                fifth_show_avail_videos()
            elif menu_selection == 6:
                sixth_show_rented_videos()
            elif menu_selection == 7:
                confirmation = input("Are you sure you want to exit program? (y/n) ").strip().lower()
                if confirmation == "y":
                    return
            else:
                print("Please enter a number 1-7!")
        else:
            print("Please enter a number 1-7!")
    except Exception:
        print("Unexpected error, returning to main menu.")
    main_menu()


######################### Operational code and function calls from here:  #########################
if __name__ == "__main__":
    main_menu()
