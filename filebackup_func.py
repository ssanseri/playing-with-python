from tkinter import *
import tkinter as tk
import sqlite3
import os
import shutil
import time
import stat
import datetime
import calendar
from pytz import timezone

# Be sure to import our other modules
# so we can have access to them
import filebackup_main
import filebackup_gui

def center_window (self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user clicks on the window's upper-right 'X' to ensure they want to close
def ask_quit (self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

## Commented these functions out because I don't need them now.
### return the age of a file in seconds
##def file_age_in_seconds (pathname):
##    return time.time() - os.stat(pathname)[stat.ST_MTIME]
##
### return True if the file was updated within 24 hours
##def file_updated_within_24_hours (pathname):
##    seconds = file_age_in_seconds(pathname)
##    return (seconds <= 24 * 60 * 60)
##
### return the current time in string format
##def time_str (gm_time):
##    fmt = "%Y-%m-%d %H:%M:%S"
##    cur_time = time.strftime(fmt, gm_time)
##    return cur_time

# return the current time in seconds since the epoch
def time_now_timegm ():
    return calendar.timegm(time.gmtime(time.time()))

# return True if file (pathname) has been updated since a given date (in seconds since the epoch)
def file_updated_since_gmtime (pathname, last_backup_date):
    modified_time = os.stat(pathname).st_mtime
    return modified_time >= last_backup_date

def get_last_backup_date ():
    conn = sqlite3.connect('db_filebackup.db')
    with conn:
        cursor = conn.cursor()
        # Get last date from the database
        cursor.execute("""SELECT col_last_save_date FROM tbl_filebackup""")
        last_save_date = cursor.fetchone()[0]
        print(last_save_date)
        cursor.close()
    conn.close()
    return last_save_date

def set_last_backup_date ():
    gm_time_now = time_now_timegm()
    conn = sqlite3.connect('db_filebackup.db')
    with conn:
        cursor = conn.cursor()
        # Get last date from the database
        cursor.execute("""SELECT col_last_save_date FROM tbl_filebackup""")
        last_save_date = cursor.fetchone()[0]
        print("old save date: " + str(last_save_date))
        cursor.execute("""UPDATE tbl_filebackup SET col_last_save_date = '{0}'""".format(gm_time_now))
        print("new save date: " + str(gm_time_now))
        cursor.close()
        conn.commit()
    conn.close()
        
# return True if file was updated since the last backup
def file_updated_since_last_backup (pathname):
    backup_date = get_last_backup_date()
    return file_updated_since_gmtime(pathname, backup_date)

def get_src_dst_dirs (self, master):
    root = master
    #   srcdir = filedialog.askdirectory(parent=root,initialdir="/",
    # Start browsing from current directory
    srcdir = ''
    while (len(srcdir) == 0):    
        srcdir = filedialog.askdirectory(parent=root,initialdir=os.getcwd(),
                                         title='Please select a source directory')
    print("Source directory: " + srcdir)
#   dstdir = filedialog.askdirectory(parent=root,initialdir="/",
    # Start browsing from current directory
    dstdir = ''
    while (len(dstdir) == 0):
        dstdir = filedialog.askdirectory(parent=root,initialdir=os.getcwd(),
                                         title='Please select a destination directory')
    print("Destination directory: " + dstdir)
    return srcdir, dstdir

def backup_files (self, srcdir, dstdir):
    # destination folder
    # for files that have been created or modified in last 24 hours
    # Use "\\?\" prefix to pathname so unicode encoding of pathname
    # will be used.  Each of the '\' characters has to be escaped by
    # using "\\", so the above prefix is "\\\\?\\" below.
    # This works around a bug ("feature") in Win32API where path
    # names longer than 260 bytes don't work (will throw FileNotFoundError
    # exception).  This code can handle pathnames with approximately 32767
    # characters, consistent with Windows 32 API.
#    dirPrefix = "\\\\?\\"
    dirPrefix = ''
    files_copied = 0

    # copy all files that have been changed since last backup from srcdir to dstdir
    for filename in os.listdir(dirPrefix + srcdir):
        if file_updated_since_last_backup(os.path.join(srcdir,filename)):
            print(os.path.join(dirPrefix + srcdir, filename))
            try:
                # use copy2 because it copies date/timestamps of files too
                shutil.copy2(os.path.join(dirPrefix + srcdir, filename),
                             os.path.join(dirPrefix + dstdir, filename))
                files_copied += 1
            # eg. src and dest are the same file
            except shutil.Error as e:
                print('Error: %s' % e)
            # eg. source or destination doesn't exist
            except IOError as e:
                print('Error: %s' % e.strerror)
    messagebox.showinfo("File Backup Complete", str(files_copied)+ " files copied successfully!")
    # If we backed up any files, then change the backup date.
    # Note that this is a simplistic solution that only keeps one date in the database.
    # A more complete solution would be to keep a separate backup date entry for each file (or directory).
    if files_copied > 0:
        set_last_backup_date()

    # See if the user wants to backup another directory.
    confirm = messagebox.askokcancel("Backup another directory?", "Backup another directory?")
    return confirm
    
def run_backup (self, srcdir, dstdir):
    while backup_files(self, srcdir, dstdir):
        get_src_dst_dirs(self, self.master)

def count_records (cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_filebackup""")
    count = cur.fetchone()[0]
    return cur,count                                                                                               

def first_run (self):
    cur_time = time_now_timegm()
    print("first run backup time: " + str(cur_time))
    conn = sqlite3.connect('db_filebackup.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_filebackup (col_last_save_date) VALUES (?)""", (cur_time,))
            conn.commit()
    conn.close()

def create_db (self):
    conn = sqlite3.connect('db_filebackup.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_filebackup( \
            col_last_save_date INT \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)

if __name__ == "__main__":
    pass
