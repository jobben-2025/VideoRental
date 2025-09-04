#Main project file

#Video Rental System

#🎯 Goal
#Students will build a console-based system for renting movies, returning them, and managing members.

#🔑 Learning Focus
#Classes: Video, Customer, VideoStore
#Functions: rent, return, search, list
#Collections: use of dict and list for efficient management

#🎯 Learning Objectives
#By the end of this project, students will be able to:
#Apply Object-Oriented Programming (OOP) principles by creating and using classes (Video, Customer, VideoStore).
#Encapsulate functionality inside methods (e.g., rent, return, search, list).
#Use Python collections (list, dict) to store and retrieve structured data efficiently.
#Implement control flow with conditions and loops to manage system operations.
#Design modular code by splitting responsibilities across classes and functions.
#Collaborate in groups, practice version control (if used), and present solutions.

#🗓️ Weekly Breakdown

#Day 1: Define Classes
#Video: attributes → title, genre, video_id, available (bool).
#Customer: attributes → name, customer_id, rented_videos (list).
#VideoStore: manages collections of videos and customers.

#Day 1–3: Implement Core Functions
#In the VideoStore class:
#add_video(video) – add a new movie.
#add_customer(customer) – register a new customer.
#rent_video(customer_id, video_id) – customer rents if available.
#return_video(customer_id, video_id) – customer returns a video.
#list_available_videos() – show available movies.
#list_customer_videos(customer_id) – show what a customer has rented.

#Day 3–6: Extensions (Group Work)
#Encourage groups to add one or two enhancements:
#Search feature: by title or genre.
#Late fee system: calculate fee if not returned on time.
#Ratings system: customers rate videos.
#Collections: Use a dict for quick lookups (e.g. video_id -> Video).

#Day 7: Presentation & Review
#Groups demo renting/returning videos.
#Discuss use of OOP + collections.
#Compare different extensions.



######################### CLASSES #########################
class Video:
    pass


class Customer:
    def __init__(self, customer_id: str, name: str):
        # unique identifier for the customer
        self.customer_id = customer_id
        # customer's full name
        self.name = name
        # list of video IDs currently rented by this customer
        self.rented_videos = []

    def rent(self, video_id: str):
        """Add a video to the list of rented videos."""
        if video_id not in self.rented_videos:
            self.rented_videos.append(video_id)

    def return_video(self, video_id: str):
        """Remove a video from the list of rented videos."""
        if video_id in self.rented_videos:
            self.rented_videos.remove(video_id)

    def __str__(self):
        """Return a human-readable summary of the customer."""
        return f"Customer[{self.customer_id}]: {self.name}, rented={self.rented_videos}"


class VideoStore:
    def __init__(self, videos=None, customers=None):
        # keep lists for now to match your current structure
        self.videos = videos if videos is not None else []
        self.customers = customers if customers is not None else []

        # basic type safety
        if not all(isinstance(v, Video) for v in self.videos):
            raise TypeError("All elements of 'videos' must be instances of Video.")
        if not all(isinstance(c, Customer) for c in self.customers):
            raise TypeError("All elements of 'customers' must be instances of Customer.")

    def add_video(self, video):
        if not isinstance(video, Video):
            raise TypeError("Only Video instances can be added.")
        self.videos.append(video)

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Only Customer instances can be added.")
        self.customers.append(customer)







######################### FUNCTIONS #########################
def first_add_video():
    pass


def second_add_customer():
        pass


def third_customer_rent_video():
        pass


def fourth_customer_return_video():
        pass


def fifth_show_avail_videos():
        pass


def sixth_show_rented_videos():
        pass


def main_menu():
    try:
        print("")
        print("Welcome to Video Rental Store (VRS)")
        print("")
        print("1. Add a video to system")
        print("2. Add a customer to system")
        print("3. Customer rent-a-video")
        print("4. Customer return-video")
        print("5. Show 'available' videos")           #display only videos,  not rented out; search via 'title' 
        print("6. Show rented videos by customer")
        print("")
        print("7. Exit program")
        print("")
        
        menu_selection = input(f"Please choose menu option to proceed: ")
        try:
            menu_selection = int(menu_selection)
            selection = True
        except:
            TypeError
        if selection == True:
            menu_selection = int(menu_selection)
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
            confirmation = input("Are you sure you want to exit program? (y/n)")
            if confirmation == "y":
                 return
        else:
            print("Please enter a number 1-7!")    

    except:
        ValueError
    main_menu()

    
######################### 1 Operational code and function calls from here:  #########################
main_menu()






























