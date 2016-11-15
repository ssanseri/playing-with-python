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
    filebackup_func.create_db(self)

    self.lbl_srcdir = tk.Label(self.master,text='Source Directory:')
    self.lbl_srcdir.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_dstdir = tk.Label(self.master,text='Destination Directory:')
    self.lbl_dstdir.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    srcdir, dstdir = filebackup_func.get_src_dst_dirs(self, master)
    self.txt_srcdir = tk.Label(self.master,text=srcdir)
    self.txt_srcdir.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_dstdir = tk.Label(self.master,text=dstdir)
    self.txt_dstdir.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.btn_run = tk.Button(self.master,width=12,height=2,text='Run Backup',
                             command=lambda: filebackup_func.run_backup(self, srcdir, dstdir))
    self.btn_run.grid(row=4,column=0,padx=(25,0),pady=(45,10),sticky=W)

    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: filebackup_func.ask_quit(self))
    self.btn_close.grid(row=4,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

if __name__ == "__main__":
    pass
