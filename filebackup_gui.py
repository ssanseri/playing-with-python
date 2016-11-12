# Python Ver:   3.5.2
#
# Author:   Samuel Sanseri
#
# Purpose:  Filebackup Demo. Demonstrating OOP, Tkinter GUI module,
#           using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested with Windows 10

from tkinter import *
import tkinter as tk
import os

# Be sure to import our other modules
# so we can have access to them
import filebackup_main
import filebackup_func

def load_gui(self, master):
    root = master
    #   srcdir = filedialog.askdirectory(parent=root,initialdir="/",
    # Start browsing from current directory
    srcdir = filedialog.askdirectory(parent=root,initialdir=os.getcwd(),
                                     title='Please select a source directory')
    if len(srcdir) > 0:
        print ("You chose " + srcdir)
#   dstdir = filedialog.askdirectory(parent=root,initialdir="/",
    # Start browsing from current directory
    dstdir = filedialog.askdirectory(parent=root,initialdir=os.getcwd(),
                                     title='Please select a destination directory')
    if len(dstdir) > 0:
        print ("You chose " + dstdir)

    self.btn_run = tk.Button(self.master,width=12,height=2,text='Run Backup',
                             command=lambda: filebackup_func.run_backup(self, srcdir, dstdir))
    self.btn_run.grid(row=0,column=0,padx=(25,0),pady=(45,10),sticky=W)

##    self.lbl_fname = tk.Label(self.master,text='First Name:')
##    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
##    self.lbl_lname = tk.Label(self.master,text='Last Name:')
##    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
##    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
##    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
##    self.lbl_email = tk.Label(self.master,text='Email Address:')
##    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
##    self.lbl_user = tk.Label(self.master,text='Information:')
##    self.lbl_user.grid(row=0,column=2,padx=(27,0),pady=(10,0),sticky=N+W)
##
##    self.txt_fname = tk.Entry(self.master,text='')
##    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
##    self.txt_lname = tk.Entry(self.master,text='')
##    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
##
##    self.txt_phone = tk.Entry(self.master,text='')
##    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
##    self.txt_email = tk.Entry(self.master,text='')
##    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
##
##    #Define the listbox with a scrollbar and grid them
##    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
##    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
##    self.lstList1.bind('<<ListboxSelect>>', lambda event: filebackup_func.onSelect(self,event))
##    self.scrollbar1.config(command=self.lstList1.yview)
##    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
##    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
##
##    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: filebackup_func.addToList(self))
##    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
##    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: filebackup_func.onUpdate(self))
##    self.btn_update.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
##    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: filebackup_func.onDelete(self))
##    self.btn_delete.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)
##    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: filebackup_func.ask_quit(self))
##    self.btn_close.grid(row=8,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)
##
##    filebackup_func.create_db(self)
##    filebackup_func.onRefresh(self)

if __name__ == "__main__":
    pass