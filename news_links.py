# Import Request library so I can download webpage
#Import beautiful soup so I can read and search the html from webpage
# make function news_link 
# takes in URL
# create beautiful soupl object to parse HTML
# look thru html and find all article title sections 
# For each article , get title , Link (URL) store in a list 
# return list (title, link) in pairs
# create main function 
# Set Url to hacker news website 
# Call my scraping function and get back all title/link pairs 
# Loop thru each pair and print , title link and blank line to match extended output 
# Run main function when program starts 
# Make new function that takes in title link. a File name to save to 
# open text file in write mode
# loop thru every (title, link) pair in list 
# write title to file, write link on next line . Write blank line after each pair to match example format 
# close text file 
# main functoin, after printing results . call save function and pass in list of results 
# confirm file has been created 

import requests
from bs4 import BeautifulSoup


def NewsLink(url): #Function that takes URL
    response = requests.get(url) # get request 
    response.raise_for_status() # stop program if request fails 

    soup = BeautifulSoup(response.text, "html.parser") # create object to parse html 
    links = [] # empty link to store (title, link) pairs 

    for span in soup.find_all("span", class_="titleline"): # find every span that contains title link on hacker news 
        a = span.find("a") # get ancho tag inside the span 
        if a and a.get("href"): # make sure tag exist and has href attribute 
            links.append((a.text.strip(), a["href"].strip())) # add title text and link URL as pair to list 

    return links # return list of all title and links 

def save_text(data, filename): # function to save results 
    with open(filename, "w", encoding="utf-8") as file: # open file for writing 
        for title, link in data: # loop thru each pair 
            file.write(title + "\n")  # write title
            file.write(link + "\n\n")  # write link then blank line


def main(): # define main function that runs program 
    url = "https://news.ycombinator.com/news" # Set url to hacker web 
    results = NewsLink(url) # call newslink function to get all titles and link from page 

    for title, link in results: # Loop thru each (title, link) pair in results 
        print(title) # print title 
        print(link) # print url
        print() # print blank line to match expected output 

    save_text(results, "news_links.txt")  # save to text file
    print("Data saved to news_links.txt")  # confirmation


if __name__ == "__main__": # run main function only when the file is executed directly 
    main()
