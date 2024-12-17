# user enter fase
from UI.GUI import GUI
from PL.InternetCheck import checkInternet
checkInternet()
guiClass=GUI("http://universities.hipolabs.com/search?") 