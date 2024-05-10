from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import json
import mechanicalsoup
from selenium import webdriver


def searchCourse(keyWord: str):     #
    browser = webdriver.Chrome()

def fetchCourse(url: str):  #find (title, content, #block) from url at KU course website
    courseInstance = urlopen(url)
    courseByte = courseInstance.read()
    courseCode = courseByte.decode('utf-8')
    #title
    soup = BeautifulSoup(courseCode, "html.parser")
    title = soup.find("h1").string

    #content
    contentSoup = soup.find("div", id="course-content")
    contents = contentSoup.get_text()

    #block number
    pattern = "<dd>Block .</dd>"
    searchResult = re.search(pattern, courseCode)
    result = searchResult.group()
    result = re.sub("<dd>Block ", "", result)
    block = re.sub("</dd>", "", result)
    courseInfo = {}
    courseInfo['title'] = title
    courseInfo['content'] = contents
    courseInfo['block'] = block
    return courseInfo

""" testUrl = "https://kurser.ku.dk/course/ndak22000u/2023-2024"

testDict = fetchCourse(testUrl)

testUrl2 = "https://kurser.ku.dk/course/ndaa09023u/2024-2025"
testDict2 = fetchCourse(testUrl2)

with open('courseData.json', 'w') as courseDataFile:
    json.dump([testDict, testDict2], courseDataFile, indent=1) """


 