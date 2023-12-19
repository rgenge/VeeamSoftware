import os
import os.path
import shutil
import time
import sys
from datetime import datetime
import colorama

colorama.init()
exit_program = False
#Backup function
def backup():
	now = datetime.now()
	now = now.strftime("%m/%d/%Y, %H:%M:%S")
	log_filename = 'log.txt'
	#directories content both source and destination
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
		#check paths and if the file doesnt exists or is different it copies it to destination and print message to log and console
		if not (os.path.exists(dest_file)) or ((src_size != dest_size)):
			shutil.copy(src_file, dest_file)
			message =str(now) + " " +  src_file + " copied to: " + dest_file + "\n"
			with open(log_path + log_filename, 'a') as file:
				file.write(message)
				print(colorama.Fore.BLUE + message + colorama.Fore.RESET)		
	#delete files that are in the destination folder but not in the source
	for file in files_dest:
		src_file = src +'/' + file
		dest_file = dest + '/' + file
		#check paths and if the file doest exist anymore it will be removed from destination folder and print to log and console
		if not os.path.exists(src_file):
			if os.path.exists (dest_file):
				os.remove(dest_file)
				message =str(now) + " " + dest_file + " removed from destination folder\n"
				with open(log_path + log_filename, 'a') as file:
					file.write(colorama.Fore.GREEN + message)
					print(colorama.Fore.RED + message + colorama.Fore.RESET)

#Function to check input validation
while not exit_program:

	try:
		src = input("Enter the source folder path: ")
		dest = input("Enter the destination folder path: ")
		interval = input("Enter what is the execution time interval in minutes: ")
		log_path = input("Enter the log folder path: ")
		# Check if paths exist and have permissions
		if not os.path.exists(src):
			print("Invalid path. Please enter valid source path.")
			continue
		if not os.path.exists(dest):
			print("Invalid path. Please enter valid destination path.")
			continue
		if not os.access(src, os.R_OK | os.W_OK):
			print("Source path does not have permissions to be copied.")
			continue
		if not os.access(dest, os.R_OK | os.W_OK):
			print("Destination path does not have permissions to be altered.")
			continue
		#check if interval is a positive valid number
		if not interval.isdigit():
			print("Interval must be a int positive number")
			continue

		# Validate log path and takes the program root if no valid path is specified
		if not os.path.exists(log_path):
			log_path = ''
			print("Invalid log path, the log will be printed in the program directory")
		else:
			log_path = log_path + "/"
		break

	except KeyboardInterrupt:
		print("Exit program")
		exit_program = True	

#Main loop after input validation that runs backup function every interval 
while not exit_program:
	#constant to change seconds to minute
	minute_converter = 60
	try:
		backup()
		time.sleep(int(interval) * minute_converter)
	except KeyboardInterrupt:
		print("Exit program")
		exit_program = True
