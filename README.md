VideoRental — Console Video Rental System

A simple, console-based app for renting and returning movies and managing customers.
Built for learning OOP, collections, and basic persistence.

Features

Classes: Video, Customer, VideoStore

Core actions: add video/customer, rent, return

Listings: available videos, videos rented by a customer

Search: by title (substring, case-insensitive) and/or genre

Persistence: plain-text catalogs for videos and customers

Important: TXT files must be present

This project stores the catalog (videos and customers) in two text files:

videostore.txt → video_id|title|genre|year

customers.txt → customer_id|name

When cloning or switching branches, make sure these files are downloaded from Git and exist in the project root.
The app loads them on startup. If they’re missing, the app starts with an empty catalog.

If you add videos or customers via the menu, they are appended to the corresponding file.

Quick Start
1) Clone and set up
git clone https://github.com/jobben-2025/VideoRental.git
cd VideoRental
# Ensure the TXT files exist locally (tracked in Git)
ls videostore.txt customers.txt


If you don’t see them, pull latest:

git pull --rebase origin dev


(Or create empty files to start from scratch: touch videostore.txt customers.txt)

2) Run
python3 main.py

Using the App

Menu options:

Add a video – prompts for Video ID, Title, Genre, Year.
Saves to memory and appends a line to videostore.txt.

Add a customer – prompts for Customer ID, Name.
Saves to memory and appends a line to customers.txt.

Rent a video – enter Customer ID and Video ID.
Marks the video as not available and records on the customer.

Return a video – enter Customer ID and Video ID.
Marks the video available again and removes from the customer.

Show available videos – lists all not currently rented.

Show rented videos by customer – lists videos for a given customer.

Search videos – title substring and/or exact genre (both optional).

Exit

File Formats
videostore.txt
video_id|title|genre|year
V001|The Shawshank Redemption|Drama|1994
V002|Inception|Sci-Fi|2010
...

customers.txt
customer_id|name
C001|Alice Example
C002|Bob Sample
...


Note: The files hold the catalog only. Availability and “who rented what” are runtime state managed by the program. This avoids merge complexity and conflicting edits.