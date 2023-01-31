#!/usr/bin/python3
import os, zipfile
from selenium import webdriver
from pynput.keyboard import Key, Listener
import keyboard 
import time

ext_dir = '/home/maxence/.config/google-chrome/Default/Extensions/lejdjhmnhlhjhfmcalaimioiogkibdea/1.0.0_0.crx'
ext_file = 'extension.zip'

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_extension(ext_dir)

# Start driver
browser = webdriver.Chrome()#(chrome_options=chrome_options)

data_dir = "/home/maxence/SC/5A/data_cookies/"

files = os.listdir(data_dir)


for file in files :
	os.system('clear')
	#os.system('cat ' + data_dir + file)
	browser.get(file.replace('http:__', 'http://').replace('.txt', ''))
	input()
	#print('mv ' + data_dir + file + './done')
	os.system('mv ' + data_dir + file + ' ./done')
	#time.sleep(10)
