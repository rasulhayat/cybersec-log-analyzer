#!/usr/bin/python3

#Python Fundamentals
#Project: Log Analyzer


import time	#imports time module
import pyfiglet	#imports python figlet module

#opens auth.log
file = open('/var/log/auth.log','r')
data = file.readlines() #stores auth.log as list 

#function to get timestamp
def getTimestamp(eachline):
	line = eachline.split()	#split string into list
	timeStamp = line[0]	#parse timestamp component from list
	return(timeStamp)	#return to caller
#end of timestamp function

#function to get executing user
def getUser(eachline):
	line = eachline.split()	#split string into list
	USER = line[3]		#parse user component from list
	return(USER)		#return to caller
#end of function

#function to get command
def getCommand(eachline):
	line = eachline.split("=")	 #split string into list, "=" as separator
	PATH = line[-1].split("bin/")	 #split string into list, "bin/" as separator
	COMMAND = PATH[1]		 #parse command
	return(COMMAND)			 #return to caller
#end of function

#title banner
pyfiglet.print_figlet('   Log Analyzer')

#case statement

print('''===================================================================

                    Welcome to the Log Analyzer

===================================================================


This script will extract and monitor important command usage and user authentication changes from the auth.log file.
Get insights on command executions, user additions, deletions, password changes, and sudo/su command usage.
''')
#infinite loop for user to choose program, only valid option for input; ability to quit script is included
while True:
	#prints options; Part 1 & 2
	print('''
Select an option:

	1) Log Parse auth.log: Extract command usage
	2) Log Parse auth.log: Monitor user authentication changes.
''')

	INPUT = input("[?] Enter option (1 or 2). Enter q|Q to quit: " )	#prints for user input
	print('\n')

	if INPUT == '1':
		# start of option 1; Extract command usage
		print('[*] Extract command usage.')
		print('[*] Processing log data... Please wait.\n')
		time.sleep(2)

		counter = 0
		for eachline in data:
			if 'COMMAND' in eachline:

				timeStamp = getTimestamp(eachline)	#invokes function to parse for timestamp
				USER = getUser(eachline)		#invokes function to parse for executing user
				COMMAND = getCommand(eachline)		#invokes function to parse for command
				counter += 1				#count the no. of entries
				#prints output
				print('''
[{}]
	[*] Timestamp:		{}
	[*] Executing user:	{}
	[*] Command used:	{}
'''.format(counter, timeStamp, USER, COMMAND))
				time.sleep(0.3)

		print('\n')
		if counter == 0:	# for when log is not available
			print('[*] Log not available...\n')

		print("[*] Exiting 'Extract command usage'...\n")
		time.sleep(1)

		#end of option 1

	elif INPUT == '2':
		#start of option 2; Monitor user authentication changes
		while True:	#infinite loop for option 2; ability to go back to prev page is included

			print('''
[*] Monitor user authentication changes.
Select an option to parse:

	1) Newly added users
	2) Deleted users
	3) Password changes
	4) 'su' command usage
	5) 'sudo' command usage
	6) Failed 'sudo' attempts
''')

			OPTION = input("[?] Enter option (1-6). Enter b|B to go back: ")#prints for user input
			print('\n')

			if OPTION == '1':
				#start of option 2-1; Newly added users
				print("[*] Processing 'Newly added users'... Please wait.\n")
				time.sleep(2)

				counter = 0
				for eachline in data:
					if 'new user' in eachline:			#when 'new user' in log entry
						timeStamp = getTimestamp(eachline)	#invokes function to parse for timestamp
						line = eachline.split("=")		#splits log entry with "=" as separator
						nameLine = line[1].split(",")		#parse 2nd index and splits with "," as separator
						newUser = nameLine[0]			#parse the name of new user
						counter += 1				#count the no. of entries
						#prints output
						print('''
[{}]
	[*] Timestamp:		{}
	[*] New user:		{}
'''.format(counter, timeStamp, newUser))
						time.sleep(0.3)

				print('\n')
				if counter == 0:	#when entry is not available
					print('[*] No Newly added users...\n')

				print("[*] Exiting 'Newly added users'...\n")
				time.sleep(1)
				#end of option 2-1

			elif OPTION == '2':
				#start of option 2-2; Deleted users
				print("[*] Processing 'Deleted users'... Please wait.\n")
				time.sleep(2)

				counter = 0
				for eachline in data:
					if 'delete user' in eachline:			#when 'deleted user' in log entry
						timeStamp = getTimestamp(eachline)	#invokes function to parse for timestamp
						line = eachline.split("'")		#splits log entry with "'" as separator
						deletedUser = line[1]			#parse deleted user
						counter += 1				#count the no. of entries
						#prints output
						print('''
[{}]
	[*] Timestamp:		{}
	[*] Deleted user:	{}
'''.format(counter, timeStamp, deletedUser))
						time.sleep(0.3)

				print('\n')
				if counter == 0:	#when entry is not available
					print('[*] No deleted users...\n')

				print("[*] Exiting 'Deleted users'...\n")
				time.sleep(1)
				#end of option 2-2

			elif OPTION == '3':
				#start of option 2-3; Password changes
				print("[*] Processing 'Password changes'... Please wait.\n")
				time.sleep(2)

				counter = 0
				for eachline in data:
					if 'password changed' in eachline:		#when 'password changed' in log entry
						timeStamp = getTimestamp(eachline)	#invokes function to parse for timestamp
						line = eachline.split()			#splits log entry with " " as separator
						changedPwdUser = line[-1]		#parse user that changed password
						counter += 1				#count the no. of entries
						#prints output
						print('''
[{}]
	[*] Timestamp:		{}
	[*] User:		{}
'''.format(counter, timeStamp, changedPwdUser))
						time.sleep(0.3)

				print('\n')
				if counter == 0:	#when entry is not available
					print('[*] No password changes...\n')

				print("[*] Exiting 'Password changes'...\n")
				time.sleep(1)
				#end of option 2-3

			elif OPTION == '4':
				#start of option 2-4; 'su' command usage
				print("[*] Processing 'su' command usage... Please wait.\n")
				time.sleep(2)

				counter = 0
				for eachline in data:
					if 'su' and '(to' in eachline:			#when 'su' and "(to" in log entry
						timeStamp = getTimestamp(eachline)	#invokes function to parse for timestamp
						line = eachline.split("to")		#splits log entry with "to" as separator
						nameLine = line[1].split()		#splits string into list with " " as separator
						toUser = nameLine[0].strip(")")		#parse current user
						fromUser = nameLine[1]			#parse prev user
						counter += 1				#count the no. of entries
						#prints output
						print('''
[{}]
	[*] Timestamp:				{}
	[*] From User (Executing):		{}
	[*] To User:				{}
'''.format(counter, timeStamp, fromUser, toUser))
						time.sleep(0.3)

				print('\n')
				if counter == 0:	#when entry is not available
					print("[*] No 'su' command usage...\n")

				print("[*] Exiting 'su' command usage...\n")
				time.sleep(1)
				#end of option 2-4

			elif OPTION == '5':
				#start of option 2-5; 'sudo' command usage
				print("[*] Processing 'sudo' command usage... Please wait.\n")
				time.sleep(2)

				counter = 0
				for eachline in data:
					if 'sudo:' and 'COMMAND' in eachline:		#when 'sudo' & 'COMMAND' in log entry
						timeStamp = getTimestamp(eachline)	#invokes function to parse for timestamp
						USER = getUser(eachline)		#invokes function to parse for executing user
						COMMAND = getCommand(eachline)		#invokes function to parse for command
						counter += 1				#count the no. of entries
						#prints output
						print('''
[{}]
	[*] Timestamp:			{}
	[*] Executing User:		{}
	[*] Command used:		{}
'''.format(counter, timeStamp, USER, COMMAND))
						time.sleep(0.3)
				print('\n')
				if counter == 0:	#when entry is not available
					print("[*] No 'sudo' command usage...\n")
				print("[*] Exiting 'sudo' command usage...\n")
				time.sleep(1)
				#end of option 2-5

			elif OPTION == '6':
				#start of option 2-6; 'Failed 'sudo' command usage'
				print("[*] Processing 'Failed 'sudo' command usage'... Please wait.\n")
				time.sleep(2)

				counter = 0
				for eachline in data:
					if 'incorrect password' in eachline:		#when 'incorrect password' in log entry
						timeStamp = getTimestamp(eachline)	#invokes function to parse for timestamp
						USER = getUser(eachline)		#invokes function to parse for executing user
						line = eachline.split()			#splits string into list with " " as separator
						ATTEMPTS = line[5]			#parse no. of incorrect password attempt(s)
						COMMAND = getCommand(eachline)		#invokes function to parse for command
						counter += 1				#count the no. of entries
						#prints output
						print('''
[{}]
	[*] Timestamp:				{}
	[*] Executing User:			{}
	[*] No. of Incorrect attempt(s):	{} Incorrect password attempt(s)
	[*] Command used:			{}
'''.format(counter, timeStamp, USER, ATTEMPTS, COMMAND))
						print('''
	[!] User {} had {} INCORRECT password attempt(s)!
'''.format(USER, ATTEMPTS))
						time.sleep(0.3)	


				print('\n')
				if counter == 0:	#when entry is not available
					print("[*] No 'Failed 'sudo' command usage'...\n")
				print("[*] Exiting 'Failed 'sudo' command usage'...\n")
				time.sleep(1)
				#end of option 2-6

			elif OPTION == 'b' or OPTION == 'B':	#user option to go back to prev page(main page)
				print("Exiting 'Monitor user authentication changes'...\n")
				time.sleep(1)
				break	#exits loop

			else:	#when user inputs an invalid option.
				print('[!] Invalid input! Please try again.\n')	

		#end of option 2

	elif INPUT == 'q' or INPUT == 'Q': #user option to quit script
		print("[*] Exiting 'Log Analyzer'...\n")
		time.sleep(1)
		print('[*] Thank you for using Log Analyzer.')
		pyfiglet.print_figlet(' Goodbye!')
		break	#exits loop

	else:
		print('[!] Invalid input! Please try again.\n')


#closes auth.log
file.close()
