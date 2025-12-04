# HOS-09 – Web Scraping News Links 📰  
# City University of Seattle | Fundamentals of Computing (IS-201)

## Overview & How It Works 🌐📄  
This assignment demonstrates how to extract article titles and links from the Hacker News website using Python, Requests, and BeautifulSoup. After collecting the data, the program prints the results to the terminal and also saves them to a text file in a clean, readable format.

## Files Included 📁  
- `news_links.py` — Main Python script that scrapes data and writes output to a text file  
- `news_links.txt` — Generated file containing all titles and links  

## Features ✨  
- Downloads webpage HTML using `requests`  
- Parses and searches the page with `BeautifulSoup`  
- Extracts article titles and their URLs  
- Prints formatted results to the terminal  
- Saves results to a `.txt` file with spacing that matches assignment requirements  

## How to Run ▶️  
Install required packages:

```bash
python -m pip install requests beautifulsoup4
# pe09
