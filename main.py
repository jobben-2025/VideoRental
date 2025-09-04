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
class Video():
    video_list = []
    def __init__(self, title, variety, year, available=True):
        self.title = title
        self.variety = variety
        self.year = year
        self.available = available
        Video.video_list.append(self)

    def borrow_video(self, customer):
        if self.available:
            self.available = False
            customer.rented_videos.append(self)
            return f"You have borrowed '{self.title}'."
        else:
            return f"'{self.title}' is currently not available."
        
    def return_video(self):
        if not self.available:
                self.available = True
                return f"You have returned '{self.title}'."
        else:
                return f"'{self.title}' was not borrowed."    
        
            
    def check_availability(self):
     if self.available:
           self.available = False
           return f"{self.title} is currently not available."
     else:
         return f"{self.title} is not in stock."

    @classmethod
    def display_videos(cls):
         if not cls.video_list:
            print("No videos in the list.")
         else:
            for video in cls.video_list:
               print(f"{video.title} ({video.year}) - Available: {video.available}")

    def __str__(self):
     return f"{self.title} ({self.year}) - {'Available' if self.available else 'Not Available'}"


class Customer():
    pass



    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Only Customer instances can be added.")   #creation by 'Customer' class
        self.customers.append(customer)

class VideoStore():
    def __init__(self, videos=None):
        if videos == None:
            videos = []
        if not all(isinstance(video, Video) for video in videos):
            raise TypeError("All elements must be instances of video.")
        self.videos = videos    

    def add_video(self, video):
        if not isinstance(video, Video):
            raise TypeError("Only Video instances can be added.")   #creation by 'Video' class
        self.videos.append(video)

    









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

    
######################### Operational code and function calls from here:  #########################
main_menu()






























