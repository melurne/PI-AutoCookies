#!/usr/bin/python3
import os

from pynput.keyboard import Key, Listener
import keyboard 
import time

data_dir = "/home/maxence/SC/5A/data_cookies/"

files = os.listdir(data_dir)

for file in files :
	os.system('clear')
	os.system('cat ' + data_dir + file)
	while True :
		if keyboard.is_pressed('s') :
			os.system('mv ' + data_dir + file + " ./simple")
			time.sleep(0.5)
			break
		if keyboard.is_pressed('q') :
			os.system('mv ' + data_dir + file + " ./bad")
			time.sleep(0.5)
			break
		if keyboard.is_pressed('d') :
			os.system('mv ' + data_dir + file + " ./good")
			time.sleep(0.5)
			break
		if keyboard.is_pressed('f') :
			os.system('mv ' + data_dir + file + " ./toclick")
			time.sleep(0.5)
			break

while True:
    if keyboard.is_pressed('q'):
        print('You Pressed A Key!')
        break 