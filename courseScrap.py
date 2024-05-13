from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def searchCourse(keyWord: str, k=3):     #
    url = "https://kurser.ku.dk/#q=&education=&programme=&volume=&departments=&faculty=FACULTY_0005&studyBlockId=&teachingLanguage=en-GB&period=&schedules=&studyId=&openUniversityInternational=1&searched=1"
    browser = webdriver.Chrome()
    browser.get(url)
    browser.fullscreen_window()
    time.sleep(2)
    cookieBlock = browser.find_element(By.CLASS_NAME, "ccc-buttons")
    cookieButton = cookieBlock.find_element(By.CLASS_NAME, "btn")
    cookieButton.click()

    inputBox = browser.find_element(By.ID, 'q')
    inputBox.send_keys(keyWord)

    #submitButton = WebDriverWait(browser, 2).until(
    #        EC.visibility_of_element_located((By.ID, 'searchall')))
    #submitButton.click()

    inputBox.send_keys(Keys.ENTER)
    time.sleep(7)
    resultsHTML = browser.page_source
    soup = BeautifulSoup(resultsHTML, "html.parser")
    resultTable = soup.find("tbody")
    rootUrl = "https://kurser.ku.dk/"
    urlList = [a['href']  for a in resultTable.find_all('a', href=True)]
    urlList = urlList[:min(len(urlList), k)]
    urlList = list(map((lambda url:rootUrl + url), urlList))

    return urlList



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

def test(word):
    urls = searchCourse(word)
    resultDicts = []
    for url in urls:
        resultDicts.append(fetchCourse(url))
    with open("courseData.json", 'w') as courseDataFile:
        json.dump(resultDicts, courseDataFile, indent=1)

test("quantum")