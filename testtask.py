import os
import os.path
import shutil
import time
from datetime import datetime

src=input("Enter the source folder path: ")
dest=input("Enter the destination folder path: ")
interval= input("Enter what is the execution time interval in minutes: ")
log_path =input("Enter the log folder path: ")

#Input validation
if not os.path.exists(src) or not os.path.exists(dest):
	exit("Invalid path")
if not interval:
	interval = 60
if not (os.path.exists(log_path)):
	log_path = ''
else:
	log_path = log_path + "/"
#Backup function
def backup():
	now = datetime.now()
	now = now.strftime("%m/%d/%Y, %H:%M:%S")
	#directories content
	files = os.listdir(src)
	files_dest = os.listdir(dest)
	#search for files in source content and copy to destination content
	for file in files:
		#get file paths
		src_file = src +'/' + file
		dest_file = dest + '/' + file
		src_size = os.path.getsize(src_file)
		if os.path.exists(dest_file):
			dest_size = os.path.getsize(dest_file)
		else:
			dest_size = 0
		#check paths and if the file doesnt exists or is different it copies
		if not (os.path.exists(dest_file)) or ((src_size != dest_size)):
			shutil.copy(src_file, dest_file)
			message =str(now) + " " +  src_file + " copied to: " + dest_file + "\n"
			with open(log_path + 'log.txt', 'a') as file:
				file.write(message)
	#delete files that are in the destination folder but not in the source
	for file in files_dest:
		src_file = src +'/' + file
		dest_file = dest + '/' + file
		#check paths and if the file doest exist anymore it will be removed from backup
		if not os.path.exists(src_file):
			if os.path.exists (dest_file):
				os.remove(dest_file)
				message =str(now) + " " + dest_file + " removed from destination folder\n"
				with open(log_path +'log.txt', 'a') as file:
					file.write(message)
while 1:
	backup()
	time.sleep(int(interval) * 60)
