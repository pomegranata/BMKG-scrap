# BMKG Web Scraping with Regex and Pop-Up Notifications
This project is a Python-based web scraper designed to fetch data from a specified website and clean the extracted strings using regular expressions (regex) to make them more readable. Additionally, the program features a local pop-up notification system to alert users when the scraping and processing tasks are completed.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Requirements](#requirements)
5. [Setup Instructions](#setup-instructions)
    [* Local Setup](#local-setup)
    [* Google Colab Setup](#google-colab-setup)
6. [Usage](#usage)
7. [Regex String Processing](#regex-string-processing)
8. [Pop-Up Notifications](#pop-up-notifications)
9. [Contributing](#contributing)

## Project Overview

The goal of this project is to create a web scraper that extracts text data from a target website. The extracted strings are often unstructured, making them difficult to read or analyze. This project uses regular expressions to clean and format these strings, enhancing readability and usability. Furthermore, to improve the user experience, the program includes a feature that triggers a pop-up notification on the local machine once the scraping and processing tasks are completed.

## Features

**1. Automated Web Scraping:** Extracts text data from a specified website.

**2. Regex-Based String Cleaning:** Uses regular expressions to structure and clean the scraped data.

**3. Local Pop-Up Notifications:** Displays a notification on the user's desktop when the task is completed.

## Technologies Used

1. Python 3.7 or higher
2. Libraries:
    * requests: To fetch web content.
    * BeautifulSoup: For parsing HTML and extracting data.
    * re: Python’s built-in regex module for string manipulation.
    * toast: For displaying pop-up notifications.

## Requirements
Before running the program, ensure you have the following:

1. Python 3.7 or higher installed.
2. The following Python libraries:
    * requests
    * beautifulsoup4
    * win11toast

    Install them via pip:
```
pip install requests beautifulsoup4 win11toast
```

## Setup Instructions

### Local Setup

1. Clone the Repository:
```
git clone https://github.com/pomegranata/BMKG-scrap
cd BMKG-scrap
```

2. Install Dependencies:
```
pip install -r requirements.txt
```

#### py file:

Run the Script:
```
py bmkg_scrap.py
```

#### ipynb file:

1. Launch Jupyter Notebook

```
jupyter notebook
```

2. Open the bmkg_scrap.ipynb notebook file.

### Google Colab Setup
You can also run this project on Google Colab, which provides free access to GPU resources for faster model training:

**1. Upload the notebook:**

* Go to [Google Colab](https://colab.research.google.com/).

* Click on "File" > "Upload Notebook" and select the bmkg_scrap.ipynb file from your local system.

**2. Mount Google Drive:**

To access the dataset stored in Google Drive, run the following code cell in Colab:

```
from google.colab import drive
drive.mount('/content/drive')
```

Follow the prompts to authorize access to your Google Drive account.

**3. Install necessary packages:**

Use:

```
!pip install
``` 

To install any additional packages required:

```
pip install beautifulsoup4
```

Note: win11toast is a Windows-specific library and may not function within Google Colab, which runs on a cloud-based Linux environment. Therefore, the pop-up notification feature will not be available when running in Colab.

**4. Run All Cells:** Execute the cells to scrape and process data.

**5. Download Processed Data:** If you want to save the cleaned data, use the files.download method from the google.colab module to download the output files to your local machine.

## Usage

**1. Configure the Target Website:**

In this code, specify the URL of the you want to scrape.
```
def web():
    my_url = 'https://warning.bmkg.go.id/'

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    scrap = page_soup.findAll("div", {"class":"col-8"})
    page = scrap[0]

    return page
```


**2. Run the Scraper:**

Execute the script using Python. The program will:

1. Fetch the HTML content from the target site.
2. Use BeautifulSoup to parse the HTML and extract text data.
3. Apply regex patterns to clean and format the strings.

**3. View Processed Data:**

The cleaned text will be printed to the console or saved to a file, depending on your configuration.

**4. Receive Notification (Windows Only):**

Once the task is completed, a Windows toast notification will appear, informing you that the process has finished.

## Regex String Processing
The core functionality of this project revolves around cleaning and structuring raw text data using regex. This includes:

**1. Removing unwanted characters:** Strip out unnecessary symbols, HTML tags, and other clutter.

**2. Formatting text:** Apply patterns to magnitude, time, and position.

**3. Splitting and joining strings:** Reshape the text to improve readability and structure.

```
import re

def magnitudo_gempa():
    magnitudo = web().div.select("li", {"img alt":"Magnitudo"}) #getting the string text
    mag = magnitudo[0].text
    
    def angka_magnitude():                  #earthquake magnitude power
        ang_mag = r'[\d\W]'
        ang = re.findall(ang_mag, mag)
        an = ''.join(ang)

        return an

    def text_magnitude():                   #just 'magnitude' text
        hur_mag = r'[a-zA-Z]'
        hur = re.findall(hur_mag, mag)
        hu = ''.join(hur)

        return hu
    
    magni = angka_magnitude() + " " + text_magnitude()

    return magni
```

## Pop-Up Notifications

The program includes a feature to notify the user when the scraping and processing tasks are complete using win11toast. This library allows the program to display a toast notification on Windows, alerting the user that the operation is finished.

Example with win11toast:

```
from win11toast import toast

toast("Update Gempa ", "Magnitudo : " + magnitudo_gempa() + '\n' + "Waktu: " + waktu_gempa() + '\n' + "Lokasi : " + lokasi_gempa())
```

This ensures that the user is informed immediately after the task is completed, even if they are not actively monitoring the console.

**Note:** This feature is only available on Windows and cannot be used when running the program in Google Colab.

## Contributing
Contributions are welcome! To contribute:

**1. Fork the Repository.**
**2. Create a New Branch:** git checkout -b feature-branch
**3. Commit Your Changes:** git commit -m 'Add new feature'
**4. Push to the Branch:** git push origin feature-branch
**5. Open a Pull Request.**