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
   
    check_availability

    @classmethod
    def display_videos(cls):
         if not cls.video_list:
            print("No videos in the list.")
         else:
            for video in cls.video_list:
               print(f"{video.title} ({video.year}) - Available: {video.available}")


    def __str__(self):
     return f"{self.title} ({self.year}) - {'Available' if self.available else 'Not Available'}"
   
    display_videos

    #####return video menu###

    def return_video_menu():
            print("=== Video Return Menu ===")
            print("1. Return a Video")
            print("2. View My Rentals")
            print("3. Exit")
   
            choice = input("Please choose an option (1-3): ")
            if choice == '1':
                video_id = input("Enter the video ID you wish to return: ")
                print(f"You have returned video ID: {video_id}")
            elif choice == '2':
                print("Displaying your rented videos...")
            elif choice == '3':
                print("Exiting the return menu.")
            else:
                print("Invalid choice. Please try again.")
                return_video_menu()

    return_video_menu()


class customer():
    pass

class videoStore():
    pass



######################### FUNCTIONS #########################
def main_menu():
    pass






    
######################### Operational code and function calls from here: #########################
main_menu()






























