#! python3
#this will open a web browser to google maps. screen shot, trim screenshot, save image file

import csv
#import webbrowser, sys
import selenium
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from time import sleep
import pyscreenshot as ImageGrab
import pyautogui
import pyperclip
#import Image

#ff_profile_dir = "/usr/local/selenium/webdriver/firefox"
#ff_profile = selenium.webdriver.FirefoxProfile(profile_directory=ff_profile_dir)

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


for i in range(1, 383):
	#test out statements..
	print(i)
	print(inCoordinate[i][2])
	print(inCoordinate[i][3])
	#this url does not seem to work BUT it will be used for now to get the browser session open..
	searchQuery = "https://www.google.com/maps/search/@?api=1&mapaction=map&zoom=5&query=" + inCoordinate[i][2] + "," + inCoordinate[i][3] #url opening on google maps seems to be broken...
	#print(searchQuery)
	driver = webdriver.Firefox()
	driver.get(searchQuery)
	sleep(1)
	driver.maximize_window()
	sleep(1)
	#manually type in coords...
	#pyperclip.copy(inCoordinate[i][2] + "," + inCoordinate[i][3])
	pyautogui.moveTo(145, 123, duration=0.3)
	sleep(2)
	pyautogui.click()
	#pyperclip.paste()
	#type it out instead..
	pyautogui.typewrite(inCoordinate[i][2] + "," + inCoordinate[i][3] + '\n')
	sleep(3)
	#close side bar..
	#pyautogui.moveTo(379, 126, duration=0.3)
	#pyautogui.click()
	#click on satellite mode...
	#sleep(1)
	pyautogui.moveTo(461, 683, duration=0.3) #this will need to be adjusted based on resolution.
	sleep(1)
	pyautogui.click()
	sleep(25) #allow satellite mode to load...
	imageSaveLocation = inCoordinate[i][0] + "_" + inCoordinate[i][2] + ',' + inCoordinate[i][3] + '.png'
	print(imageSaveLocation)
	im = ImageGrab.grab()
	box = (640, 204, 1124, 648) #this is the smaller screen portion. image size will be 484 x 444 when it is done.
	region = im.crop(box)
	im = region
	im.save(imageSaveLocation)
	driver.close() 
	sleep(1)
