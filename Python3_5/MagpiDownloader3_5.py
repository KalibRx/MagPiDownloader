import urllib.request
import os
"""13/dec/2016 MagPi downloader script for Python 3.5"""

url = "https://www.raspberrypi.org/magpi-issues/"

def getIssueNames(url):
    """
    method to acquire names of magpi issues
    String url: the url of the download page
    returns a list of pdf issue names 
    """
    response = urllib.request.urlopen("https://www.raspberrypi.org/magpi-issues/")
    html = response.read().decode("utf-8")
    links = html.split("\"")

    for x in links[:]: #process links to leave only issue titles
        if ".pdf" not in x:
            links.remove(x)
        elif ">" in x:
            links.remove(x)
    return links

def checkDirectory(directory):
    """
    method to check if download directory exists and create it if not.
    String directory: the directory to store downloaded issues
    returns a directory string
    """
    if directory[-1] != "\\":
        directory += "\\"
    if not os.path.isdir(directory):
        os.makedirs(directory) #create recursively the directory if it doesn't exist
    return directory

def downloadIssues(url,issues):
    """
    method to download issues
    String url: The url to download from
    List issues: A list of strings containing issue names
    returns nothing
    """
    count = 0
    for element in issues:
        if os.path.isdir(directory):
            file_name = element #filename to save download as
            if os.path.isfile(directory + file_name):
                print ("File already exists!")
                continue
            else:
                f = open(directory + file_name, "wb") #open file for writing in binary
                u = urllib.request.urlopen(url + element)
                print ("Downloading " + element + " to " + directory )
                block = 8192
                while True:
                    buffer = u.read(block)
                    if not buffer:
                        break
                    f.write(buffer)
                f.close()
                count += 1
    print ("Downloads complete!")
    print (str(count) + " issues downloaded!")

issues = getIssueNames(url)
directory = input("Enter a directory to save files: ")
directory = checkDirectory(directory)
downloadIssues(url,issues)
