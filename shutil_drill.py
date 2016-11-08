##Scenario: Your employer wants a program to move all his .txt files from one folder to another
##with the click of a click of a button. On your desktop make 2 new folders. Call one Folder A &
##the second Folder B. Create 4 random .txt files & put them in Folder A.
##Plan:
##- Move the files from Folder A to Folder B.
##- Print out each file path that got moved onto the shell.
##- Upon viewing Folder A after the execution, the moved files should not be there.
##Guidelines:
##● Use Python 2.7 .x on this drill.
##● Import the shutil module.
##● Run it on the python shell.
##● Use the IDLE for this Drill.
##

import shutil
import os

dirA = 'C:\\Users\\Student\\Desktop\\Folder A\\'
print(dirA)
dirB = 'C:\\Users\\Student\\Desktop\\Folder B\\'
print(dirB)

print("Here is the list of files in " + dirA + " before the move")
print(os.listdir(dirA)) 

for filename in os.listdir(dirA):
    print(dirA + filename)
    shutil.move(dirA+filename, dirB)

print("Here is the list of files in " + dirA + " after the move")
print(os.listdir(dirA)) 

