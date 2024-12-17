from webbrowser import open
from PL.InternetCheck import checkInternet
def send(text):
    checkInternet()
    open(f"https://web.whatsapp.com/send?phone=+9809932062665&text={text}")