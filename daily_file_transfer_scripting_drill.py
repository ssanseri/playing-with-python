##Title: Daily File Transfer scripting project - Python 2.x - IDLE
##Scenario: Your company's users create or edit a collection of text files
##throughout the day. These text files represent data about customer
##orders.
##Once per day, any files that are new, or that were edited within the
##previous 24 hours, must be sent to the home office. To facilitate this,
##these new or updated files need to be copied to a specific 'destination'
##folder on a computer, so that a special file transfer program can grab
##them and transfer them to the home office.
##The process of figuring out which files are new or recently edited, and
##copying them to the 'destination' folder, is currently being done
##manually. This is very expensive in terms of manpower.
##You have been asked to create a script that will automate this task,
##saving the company a lot of money over the long term.
##Guidelines:
##Use Python 2.x for this drill.
##You should create two folders; one to hold the files that get created or
##modified throughout the day, and another to receive the folders that your
##script determines should be copied over daily.
##To aid in your development efforts, you should create .txt files to add
##to the first folder, using Notepad or similar program. You should also
##copy some older text files in there if you like. You should use files
##that you can edit, so that you can control whether they are meant to be
##detected as 'modified in the last 24 hours' by your program.

import os
import shutil
import time
import stat

def file_age_in_seconds(pathname):
    return time.time() - os.stat(pathname)[stat.ST_MTIME]

def file_updated_within_24_hours(pathname):
    seconds = file_age_in_seconds(pathname)
    return (seconds <= 24 * 60 * 60)

# destination folder
# for files that have been created or modified in last 24 hours
destDir = 'C:\\Users\\Student\\Desktop\\Folder B\\'

# source folder:
# Use C:\\ if wanting to test usage of all files on the hard drive.
# Or specify a specific root directory for a subtree.
#sourceDir = 'C:\\Users\\Student\\Desktop\\Folder A\\'
sourceDir = 'C:\\'

# Use "\\?\" prefix to pathname so unicode encoding of pathname
# will be used.  Each of the '\' characters has to be escaped by
# using "\\", so the above prefix is "\\\\?\\" below.
# This works around a bug ("feature") in Win32API where path
# names longer than 260 bytes don't work (will throw FileNotFoundError
# exception).  This code can handle pathnames with approximately 32767
# characters, consistent with Windows 32 API.
dirPrefix = "\\\\?\\"

# for root, dirs, files in os.walk("\\\\?\\C:\\", topdown=False):
for root, dirs, files in os.walk(dirPrefix + sourceDir, topdown=False):
    try:
        for name in files:
            complete_filename = os.path.join(root, name)
            if file_updated_within_24_hours(complete_filename):
                # could do something different here like move/copy the file
                print(complete_filename)
        for name in dirs:
            complete_filename = os.path.join(root, name)
            if file_updated_within_24_hours(complete_filename):
                print(complete_filename)
    # The os.walk() was throwing a PermissionError exception for 
    # temporary files in use by the OS, so I want to catch that
    # exception and keep going
    except PermissionError:
        continue
        
##
##
##print("Here is the list of files in " + dirA + " before the move")
##print(os.listdir(dirA)) 
##
##for filename in os.listdir(dirA):
##    print(dirA + filename)
##    shutil.move(dirA+filename, dirB)
##
##print("Here is the list of files in " + dirA + " after the move")
##print(os.listdir(dirA)) 
##
