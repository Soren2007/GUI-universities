from socket import *
from tkinter import messagebox
from sys import exit
def checkInternet() -> None:
    """"""
    try:
        name = "www.google.com"
        gethostbyname(name)
        create_connection((name,80))
    except:
        messagebox.showerror("Error","Please check your internet !!!")
        exit(0)