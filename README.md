# BMKG Web Scraping with Regex and Pop-Up Notifications
This project is a Python-based web scraper designed to fetch data from a specified website and clean the extracted strings using regular expressions (regex) to make them more readable. Additionally, the program features a local pop-up notification system to alert users when the scraping and processing tasks are completed.

# Table of Contents
1. [Project Overview]()
2. [Features]()
3. [Technologies Used]()
4. [Requirements]()
5. [Setup Instructions]()
6. [Usage]()
7. [Regex String Processing]()
8. [Pop-Up Notifications]()
9. [Contributing]()
Contact Information

# Project Overview

The goal of this project is to create a web scraper that extracts text data from a target website. The extracted strings are often unstructured, making them difficult to read or analyze. This project uses regular expressions to clean and format these strings, enhancing readability and usability. Furthermore, to improve the user experience, the program includes a feature that triggers a pop-up notification on the local machine once the scraping and processing tasks are completed.

# Features

**1. Automated Web Scraping:** Extracts text data from a specified website.

**2. Regex-Based String Cleaning:** Uses regular expressions to structure and clean the scraped data.

**3. Local Pop-Up Notifications:** Displays a notification on the user's desktop when the task is completed.

# Technologies Used

1. Python 3.7 or higher
2. Libraries:
    * requests: To fetch web content.
    * BeautifulSoup: For parsing HTML and extracting data.
    * re: Python’s built-in regex module for string manipulation.
    * toast: For displaying pop-up notifications.