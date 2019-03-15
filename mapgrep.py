#! python3
#this will open a web browser to google maps. screen shot, trim screenshot, save image file

import csv
import webbrowser, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyscreenshot as ImageGrab
import pyautogui
#import Image


#opens csv, passes to a list data type. there were only 3-400 lines in my original data set
#this block works. but is not active in creating the google maps url
inFile = open('NFA Sites Info for Mapping-Sheet1.csv')
inReader = csv.reader(inFile)
inCoordinate = list(inReader)
#to use inData just do:
# i = row. 3 and 4 are colums of latitude longitude
#inData[i][3] csv item, latitude 
#inData[i][4] csv item, longitude
#just like freshman year of college! but with less crying
#testing purposes
i = 3
print(inCoordinate[i][2])
print(inCoordinate[i][3])


#for loop starts here for now i = 3
#url concealed for now. just test the home address!
#searchQuery = "https://www.google.com/maps/search/@?api=1&mapaction=map&zoom=15&center=33.2076635,-97.1337569" ##satellite view does not work for some reason
searchQuery = "https://www.google.com/maps/search/@?api=1&mapaction=map&zoom=15&query=" + inCoordinate[i][2] + "," + inCoordinate[i][3]
print(searchQuery)
driver = webdriver.Firefox()
driver.get(searchQuery)
sleep(1)
driver.maximize_window()
sleep(1)
imageSaveLocation = inCoordinate[i][1] + "_" + inCoordinate[i][2] + ',' + inCoordinate[i][3] + '.png'
print(imageSaveLocation)
im = ImageGrab.grab()
box = (0, 100, 1920, 1054)
region = im.crop(box)
im = region
im.save(imageSaveLocation)
pyautogui.moveTo(54, 999, duration=1)
#(54, 999) #mouse move to
pyautogui.click()
sleep(10)
driver.close()
