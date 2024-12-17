from requests import get
from tkinter.messagebox  import showerror
def apiData(url,country):
    try:
        res = get(url,country)
        if res.status_code == 200:
            return res.json()
        else:
            showerror("Error",f"Error : Status Code is {res.status_code}")
    except RuntimeError as error:
        showerror("Error",error)

