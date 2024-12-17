# ----------------------------------------Information----------------------------------------
# Name File : GUI
# Project Name : Practice_32
# Programmer : Soren Shamloo
# Date : 2022/6/9
# -------------------------------------------------------------------------------------------
# ------------------------------------------Imports------------------------------------------
# API for read Json in URL
from DAL.API import apiData
# ktinter for GUI
from tkinter import Label,Entry,Toplevel,Tk,CENTER
# pygame for play music
from pygame import mixer
# time for Event
from time import sleep
# ttk for Tabel
from tkinter import ttk
# PIL for Insert photo
# from PIL import ImageTk, Image
from PIL import ImageTk, Image
# messagebox for show errors and show info
from tkinter.messagebox import showerror,showinfo,askretrycancel
# webbrowser for Open a website
from webbrowser import open_new
# VideoDisplay Open the help video
from PL.VideoDisplay import VideoDisplay
# ConvertAudioToText for 
from PL.ConvertAudioToText import start
# filedialog for get path
from tkinter.filedialog import askdirectory
# os for end code 
from os import system
# json for read setting and save setting
from json import load,dump
from PL.sendMessage import send
# -------------------------------------------------------------------------------------------
# ------------------------------------------Class--------------------------------------------
# GUI class for show display information to the user
class GUI:
    """GUI class for show display information to the user ..."""
    # init function
    def __init__(self,url):
        self.textMessage={"star":0,"speed":False,"performance":False,"designing":False}
        # self.__url for API
        self.__url=url
        # with for read setting file
        with open("C:/ProgramData/App_Data_Soren/data/Setting/Setting.json",'r') as settingFile:
            self.__jsonSetting=load(settingFile)
        # for play music
        # ************************************************************************************
        self.__pageSong = mixer
        self.__pageSong.init()
        self.__pageSong.music.load(self.__jsonSetting['pageSongPath'])
        self.__pageSong.music.play()
        # ************************************************************************************
        # ----------------------------------------Main Form-----------------------------------
        # ************************************************************************************
        self.__window = Tk()
        GUI.windowSize(self.__window, 1220, 880)
        self.__window.iconbitmap(self.__jsonSetting['icon'])
        self.__window.title("Universitys")
        self.__window.configure(bg=self.__jsonSetting['backgroundForm'])
        self.__settingMenuImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/SettingM_N.jpg"))
        self.__settingMenu=Label(master=self.__window,image=self.__settingMenuImg_N,width=105,height=50,background=self.__jsonSetting['backgroundForm'])
        self.__settingMenu.bind("<Leave>", lambda event: self.__settingMenu.config(image=self.__settingMenuImg_N))
        self.__settingMenuImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/SettingM_E.jpg"))
        self.__settingMenu.bind("<Enter>", lambda event: self.__settingMenu.config(image=self.__settingMenuImg_E))
        self.__settingMenu.bind("<Button>", lambda event: self.setting(self.__settingMenu,self.__settingMenuImg_E))
        self.__settingMenu.grid(row=0, column=0,pady=0,padx=10,sticky="w")
        self.__helpMenuImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/HelpM_N.jpg"))
        self.__helpMenu=Label(master=self.__window,image=self.__helpMenuImg_N,width=105,height=50,background=self.__jsonSetting['backgroundForm'])
        self.__helpMenu.bind("<Leave>", lambda event: self.__helpMenu.config(image=self.__helpMenuImg_N))
        self.__helpMenuImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/HelpM_E.jpg"))
        self.__helpMenu.bind("<Enter>", lambda event: self.__helpMenu.config(image=self.__helpMenuImg_E))
        self.__helpMenu.bind("<Button>", lambda event: VideoDisplay())
        self.__helpMenu.grid(row=0, column=0,pady=0,padx=120,sticky="w")
        self.__aboutMenuImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/AboutM_N.jpg"))
        self.__aboutMenu=Label(master=self.__window,image=self.__aboutMenuImg_N,width=105,height=50,background=self.__jsonSetting['backgroundForm'])
        self.__aboutMenu.bind("<Leave>", lambda event: self.__aboutMenu.config(image=self.__aboutMenuImg_N))
        self.__aboutMenuImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/AboutM_E.jpg"))
        self.__aboutMenu.bind("<Enter>", lambda event: self.__aboutMenu.config(image=self.__aboutMenuImg_E))
        self.__aboutMenu.bind("<Button>", lambda event: self.info(self.__aboutMenu,self.__aboutMenuImg_E))
        self.__aboutMenu.grid(row=0, column=0,pady=0,padx=230,sticky="w")
        self.__imgForm = Label(master=self.__window, text="🏫", font=(None, 170), background=self.__jsonSetting['backgroundForm'], foreground=self.__jsonSetting['backgroundLabels'])
        self.__imgForm.grid(row=1, column=0,pady=0,padx=476,sticky="w")
        self.welcomeText = Label(master=self.__window, text="Welcome", font=(self.__jsonSetting['fontLabel'], 66,"bold"), background=self.__jsonSetting['backgroundForm'], foreground=self.__jsonSetting['backgroundLabels'])
        self.welcomeText.grid(row=2, column=0,pady=0,padx=395,sticky="w")
        self.helpButtonImg_N = ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/help_N.jpg"))
        self.helpButtonImg_E = ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/help_E.jpg"))
        self.imcButtonImg_N = ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/mic_N.jpg"))
        self.imcButtonImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/mic_E.jpg"))
        self.NoneImg = ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/None.jpg"))
        # ************************************************************************************
        self.imcButtonC=Label(master=self.__window,image=self.NoneImg,width=275,height=110,background=self.__jsonSetting['backgroundForm'])
        self.imcButtonC.grid(row=3, column=0,pady=5,padx=947,sticky="w")
        self.imcButtonC.bind("<Enter>", lambda event: GUI.action(self.imcButtonC,self.imcButtonImg_N))
        self.imcButtonC.bind("<Leave>", lambda event: self.imcButtonC.config(image=self.NoneImg))
        self.helpButtonC=Label(master=self.__window,image=self.NoneImg,width=255,height=92,background=self.__jsonSetting['backgroundForm'])
        self.helpButtonC.bind("<Enter>", lambda event: GUI.action(self.helpButtonC,self.helpButtonImg_N))
        self.helpButtonC.bind("<Leave>", lambda event: self.helpButtonC.config(image=self.NoneImg))
        self.helpButtonC.bind("<Button>", lambda event: self.help("HelpCountryTextBox"))
        self.helpButtonC.grid(row=3, column=0,pady=5,padx=10,sticky="w")
        # ************************************************************************************
        self.countryEntryImg = ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Country_N.jpg"))
        self.countryLEntry = Label(master=self.__window,image=self.countryEntryImg,width=681,height=130,background=self.__jsonSetting['backgroundForm'])
        self.countryLEntry.grid(row=3, column=0,pady=0,padx=270,sticky="w")
        self.countryEntry = Entry(master=self.__window, background=(self.__jsonSetting['backgroundLabels']), foreground=self.__jsonSetting['backgroundForm'],font=(self.__jsonSetting['fontEntry'], 36,"bold"),width=15,bd=0,xscrollcommand=True)
        self.countryEntry.insert(0,"IRAN")
        # ************************************************************************************
        self.imcButtonC.bind("<Button>", lambda event: self.microphone(self.countryEntry))
        self.countryEntry.grid(row=3, column=0,pady=0,padx=510,sticky="w")
        self.imcButtonS=Label(master=self.__window,image=self.NoneImg,width=275,height=110,background=self.__jsonSetting['backgroundForm'])
        self.imcButtonS.grid(row=4, column=0,pady=5,padx=947,sticky="w")
        self.imcButtonS.bind("<Enter>", lambda event: GUI.action(self.imcButtonS,self.imcButtonImg_N))
        self.imcButtonS.bind("<Leave>", lambda event: self.imcButtonS.config(image=self.NoneImg))
        self.helpButtonS=Label(master=self.__window,image=self.NoneImg,width=255,height=110,background=self.__jsonSetting['backgroundForm'])
        self.helpButtonS.bind("<Enter>", lambda event: GUI.action(self.helpButtonS,self.helpButtonImg_N))
        self.helpButtonS.bind("<Leave>", lambda event: self.helpButtonS.config(image=self.NoneImg))
        self.helpButtonS.bind("<Button>", lambda event: self.help())
        self.helpButtonS.grid(row=4, column=0,pady=5,padx=8,sticky="w")
        # ************************************************************************************
        self.stateEntryImg = ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/State_N.jpg"))
        self.stateLEntry = Label(master=self.__window,image=self.stateEntryImg,width=681,height=130,background=self.__jsonSetting['backgroundForm'])
        self.stateLEntry.grid(row=4, column=0,pady=0,padx=270,sticky="w")
        self.stateEntry = Entry(master=self.__window, background=(self.__jsonSetting['backgroundLabels']), foreground=self.__jsonSetting['backgroundForm'],font=(self.__jsonSetting['fontEntry'], 36,"bold"),width=15,bd=0,xscrollcommand=True)
        self.stateEntry.insert(0,"Tehran")
        # ************************************************************************************
        self.imcButtonS.bind("<Button>", lambda event: self.microphone(self.stateEntry))
        self.stateEntry.grid(row=4, column=0,pady=0,padx=510,sticky="w")
        self.showButtonImg_1= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Show Button_N.jpg"))
        self.showButton = Label(master=self.__window,image=self.showButtonImg_1,width=832,height=102,background=self.__jsonSetting['backgroundForm'])
        self.showButton.bind("<Leave>", lambda event: self.showButton.config(image=self.showButtonImg_1))
        self.showButtonImg_2= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Show Button_E.jpg"))
        self.showButton.bind("<Enter>", lambda event: GUI.button_Enter(self.showButton,self.showButtonImg_2))
        self.showButton.bind("<Button>", lambda event: self.show(self.showButton,self.stateEntry.get(),self.countryEntry.get()))
        self.showButton.grid(row=5, column=0,pady=5,padx=190,sticky="w")
        # ************************************************************************************
        self.starMButtonImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Star_NM.jpg"))
        self.starMButton=Label(master=self.__window,image=self.starMButtonImg_N,width=60,height=63,background=self.__jsonSetting['backgroundForm'])
        self.starMButton.bind("<Leave>", lambda event: self.starMButton.config(image=self.starMButtonImg_N))
        self.starMButtonImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Star_EM.jpg"))
        self.starMButton.bind("<Enter>", lambda event: GUI.button_Enter(self.starMButton,self.starMButtonImg_E))
        self.starMButtonImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Star_BM.jpg"))
        self.starMButton.bind("<Button>", lambda event: self.showStar())
        self.starMButton.grid(row=6, column=0,pady=10,padx=1150,sticky="w")
        # ************************************************************************************
        self.pauseButtonImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Pause Button_N.jpg"))
        self.pauseButton=Label(master=self.__window,image=self.pauseButtonImg_N,width=60,height=63,background=self.__jsonSetting['backgroundForm'])
        self.pauseButton.bind("<Leave>", lambda event: self.pauseButton.config(image=self.pauseButtonImg_N))
        self.pauseButtonImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Pause Button_E.jpg"))
        self.pauseButton.bind("<Enter>", lambda event: GUI.button_Enter(self.pauseButton,self.pauseButtonImg_E))
        self.pauseButtonImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Pause Button_B.jpg"))
        self.pauseButton.bind("<Button>", lambda event: self.pause(self.pauseButton,self.pauseButtonImg_B))
        self.pauseButton.grid(row=6,columnspan=2, column=0,pady=10,padx=780,sticky="w")
        # ************************************************************************************
        self.unpauseButtonImg_1=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/UPause Button_N.jpg"))
        self.unpauseButton=Label(master=self.__window,image=self.unpauseButtonImg_1,width=60,height=63,background=self.__jsonSetting['backgroundForm'])
        self.unpauseButton.bind("<Leave>", lambda event: self.unpauseButton.config(image=self.unpauseButtonImg_1))
        self.unpauseButtonImg_2= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/UPause Button_E.jpg"))
        self.unpauseButton.bind("<Enter>", lambda event: GUI.button_Enter(self.unpauseButton,self.unpauseButtonImg_2))
        self.unpauseButtonImg_3= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/UPause Button_B.jpg"))
        self.unpauseButton.bind("<Button>", lambda event: self.unpause(self.unpauseButton,self.unpauseButtonImg_3))
        self.unpauseButton.grid(row=6,columnspan=2, column=0,pady=10,padx=680,sticky="w")
        # ************************************************************************************
        self.stopButtonImg_1=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Stop Button_N.jpg"))
        self.stopButton=Label(master=self.__window,image=self.stopButtonImg_1,width=60,height=63,background=self.__jsonSetting['backgroundForm'])
        self.stopButton.bind("<Leave>", lambda event: self.stopButton.config(image=self.stopButtonImg_1))
        self.stopButtonImg_2= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Stop Button_E.jpg"))
        self.stopButton.bind("<Enter>", lambda event: GUI.button_Enter(self.stopButton,self.stopButtonImg_2))
        self.stopButtonImg_3= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Stop Button_B.jpg"))
        self.stopButton.bind("<Button>", lambda event: self.stop(self.stopButton,self.stopButtonImg_3))
        self.stopButton.grid(row=6,columnspan=2, column=0,pady=10,padx=580,sticky="w")
        # ************************************************************************************
        self.settingButtonImg_1=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Setting Button_N.jpg"))
        self.settingButton=Label(master=self.__window,image=self.settingButtonImg_1,width=60,height=63,background=self.__jsonSetting['backgroundForm'])
        self.settingButton.bind("<Leave>", lambda event: self.settingButton.config(image=self.settingButtonImg_1))
        self.settingButtonImg_2= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Setting Button_E.jpg"))
        self.settingButton.bind("<Enter>", lambda event: GUI.button_Enter(self.settingButton,self.settingButtonImg_2))
        self.settingButtonImg_3= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Setting Button_B.jpg"))
        self.settingButton.bind("<Button>", lambda event: self.setting(self.settingButton,self.settingButtonImg_3))
        self.settingButton.grid(row=6,columnspan=2, column=0,pady=10,padx=480,sticky="w")
        # ************************************************************************************
        self.infoButtonImg_1=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Info Button_N.jpg"))
        self.infoButton=Label(master=self.__window,image=self.infoButtonImg_1,width=60,height=63,background=self.__jsonSetting['backgroundForm'])
        self.infoButton.bind("<Leave>", lambda event: self.infoButton.config(image=self.infoButtonImg_1))
        self.infoButtonImg_2= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Info Button_E.jpg"))
        self.infoButton.bind("<Enter>", lambda event: GUI.button_Enter(self.infoButton,self.infoButtonImg_2))
        self.infoButtonImg_3= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Info Button_B.jpg"))
        self.infoButton.bind("<Button>", lambda event: self.info(self.infoButton,self.infoButtonImg_3))
        self.infoButton.grid(row=6,columnspan=2, column=0,pady=10,padx=380,sticky="w")
        # ************************************************************************************
        self.__window.mainloop()
        # *******************************************************************************
    def showStar(self):
        
        # ************************************************************************************
        self.__window_Star=Toplevel(self.__window)
        GUI.windowSize(self.__window_Star,350,360)
        self.__window_Star.title("Score")
        self.__window_Star.configure(bg=self.__jsonSetting['backgroundForm'])
        self.__window_Star.iconbitmap(self.__jsonSetting['icon'])
        # ************************************************************************************
        self.buttonSong = mixer
        self.buttonSong.init()
        self.buttonSong.music.load(self.__jsonSetting['buttonSongPath'])
        self.buttonSong.music.play()
        sleep(0.18)
        self.__pageSong.music.load(self.__jsonSetting['pageSongPath'])
        self.buttonSong.music.play()
        # ************************************************************************************
        self.softwareLabel=Label(master=self.__window_Star, text="----------------Score-------------- ", font=(self.__jsonSetting['fontEntry'], 18,"bold"), background=self.__jsonSetting['backgroundForm'], foreground=self.__jsonSetting['backgroundLabels'])
        self.softwareLabel.grid(row=1, column=0,pady=10,padx=20,sticky="w") 
        self.checkSpeedImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button_N_1.jpg"))
        self.checkSpeedImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button_B_1.jpg"))
        self.checkSpeed=Label(master=self.__window_Star,image=self.checkSpeedImg_N,width=129,height=30,background=self.__jsonSetting['backgroundForm'])
        self.checkSpeed.bind("<Leave>", lambda event: self.check("speed",'N'))
        self.checkSpeed.bind("<Button>", lambda event: self.check("speed",'B'))
        self.checkSpeed.grid(row=2, column=0,pady=10,padx=30,sticky="w")
        # ************************************************************************************
        self.checkDesigningImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button_N_2.jpg"))
        self.checkDesigningImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button_B_2.jpg"))
        self.checkDesigning=Label(master=self.__window_Star,image=self.checkDesigningImg_N,width=177,height=30,background=self.__jsonSetting['backgroundForm'])
        self.checkDesigning.bind("<Leave>", lambda event: self.check("designing",'N'))
        self.checkDesigning.bind("<Button>", lambda event: self.check("designing",'B'))
        self.checkDesigning.grid(row=3, column=0,pady=10,padx=30,sticky="w")
        self.checkPerformanceImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button_N_3.jpg"))
        self.checkPerformanceImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button_B_3.jpg"))
        self.checkPerformance=Label(master=self.__window_Star,image=self.checkPerformanceImg_N,width=206,height=30,background=self.__jsonSetting['backgroundForm'])
        self.checkPerformance.bind("<Leave>", lambda event: self.check("performance",'N'))
        self.checkPerformance.bind("<Button>", lambda event: self.check("performance",'B'))
        self.checkPerformance.grid(row=4, column=0,pady=10,padx=30,sticky="w")
        # ************************************************************************************
        self.starButtonImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Star_N.jpg"))
        self.starButtonImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Star_B.jpg"))
        self.starButtonImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Star_E.jpg"))
        self.star_1_Button=Label(master=self.__window_Star,image=self.starButtonImg_N,width=35,height=39,background=self.__jsonSetting['backgroundForm'])
        self.star_1_Button.bind("<Leave>", lambda event: self.star(1,'N'))
        self.star_1_Button.bind("<Enter>", lambda event: self.star(1,'E'))
        self.star_1_Button.bind("<Button>", lambda event: self.star(1,'B'))
        self.star_1_Button.grid(row=5, column=0,pady=10,padx=60,sticky="w")
        # ************************************************************************************
        self.star_2_Button=Label(master=self.__window_Star,image=self.starButtonImg_N,width=35,height=39,background=self.__jsonSetting['backgroundForm'])
        self.star_2_Button.bind("<Leave>", lambda event: self.star(2,'N'))
        self.star_2_Button.bind("<Enter>", lambda event: self.star(2,'E'))
        self.star_2_Button.bind("<Button>", lambda event: self.star(2,'B'))
        self.star_2_Button.grid(row=5, column=0,pady=10,padx=110,sticky="w")
        # ************************************************************************************
        self.star_3_Button=Label(master=self.__window_Star,image=self.starButtonImg_N,width=35,height=39,background=self.__jsonSetting['backgroundForm'])
        self.star_3_Button.bind("<Leave>", lambda event: self.star(3,'N'))
        self.star_3_Button.bind("<Enter>", lambda event: self.star(3,'E'))
        self.star_3_Button.bind("<Button>", lambda event:self.star(3,'B'))
        self.star_3_Button.grid(row=5, column=0,pady=10,padx=160,sticky="w")
        # ************************************************************************************
        self.star_4_Button=Label(master=self.__window_Star,image=self.starButtonImg_N,width=35,height=39,background=self.__jsonSetting['backgroundForm'])
        self.star_4_Button.bind("<Leave>", lambda event: self.star(4,'N'))
        self.star_4_Button.bind("<Enter>", lambda event: self.star(4,'E'))
        self.star_4_Button.bind("<Button>", lambda event: self.star(4,'B'))
        self.star_4_Button.grid(row=5, column=0,pady=10,padx=210,sticky="w")
        # ************************************************************************************
        self.star_5_Button=Label(master=self.__window_Star,image=self.starButtonImg_N,width=35,height=39,background=self.__jsonSetting['backgroundForm'])
        self.star_5_Button.bind("<Leave>", lambda event: self.star(5,'N'))
        self.star_5_Button.bind("<Enter>", lambda event: self.star(5,'E'))
        self.star_5_Button.bind("<Button>", lambda event: self.star(5,'B'))
        self.star_5_Button.grid(row=5, column=0,pady=10,padx=260,sticky="w")
        # ************************************************************************************
        self.submitButtonImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Submit Button_N.jpg"))
        self.submitButtonImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Submit Button_E.jpg"))
        self.submitButtonImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Submit Button_B.jpg"))
        self.submitButton=Label(master=self.__window_Star,image=self.submitButtonImg_N,width=140,height=57,background=self.__jsonSetting['backgroundForm'])
        self.submitButton.bind("<Leave>", lambda event: self.submitButton.config(image=self.submitButtonImg_N))
        self.submitButton.bind("<Enter>", lambda event: GUI.button_Enter(self.submitButton,self.submitButtonImg_E))
        self.submitButton.bind("<Button>", lambda event: send(f"Star Number:{self.textMessage['star']}         performance:{self.textMessage['performance']}         designing:{self.textMessage['designing']}         speed:{self.textMessage['speed']}"))
        self.submitButton.grid(row=6, column=0,pady=10,padx=105,sticky="w") 
        # ************************************************************************************
    def info(self,nameButton,file):
        # ************************************************************************************
        nameButton.config(image=file)
        showinfo("Info","Version : 1.0.5\nDate : 2022/6/2\nOS : Windows")
        # ************************************************************************************
    def setting(self,nameButton,file):
        nameButton.config(image=file)
        self.settingText={"backgroundForm":self.__jsonSetting["backgroundForm"],"item":self.__jsonSetting["item"],"pageSongPath":self.__jsonSetting["pageSongPath"],"buttonSongPath":self.__jsonSetting["buttonSongPath"],"backgroundLabels":self.__jsonSetting["backgroundLabels"],"fontEntry":self.__jsonSetting["fontEntry"],"fontLabel":self.__jsonSetting["fontLabel"],"icon":self.__jsonSetting["icon"]}
        self.__window_setting=Toplevel(self.__window)
        GUI.windowSize(self.__window_setting,800,700)
        self.__window_setting.title("Setting")
        self.__window_setting.configure(bg=self.__jsonSetting['backgroundForm'])
        self.__window_setting.iconbitmap(self.__jsonSetting['icon'])
        self.buttonSong = mixer
        self.buttonSong.init()
        self.buttonSong.music.load(self.__jsonSetting['buttonSongPath'])
        self.buttonSong.music.play()
        sleep(0.18)
        self.__pageSong.music.load(self.__jsonSetting['pageSongPath'])
        self.buttonSong.music.play()
        self.settingLabel=Label(master=self.__window_setting, text="Setting", font=(self.__jsonSetting['fontLabel'], 50), background=self.__jsonSetting['backgroundForm'], foreground=self.__jsonSetting['backgroundLabels'])
        self.settingLabel.grid(row=0, column=0,pady=10,padx=255,sticky="w") 
            # Items Night
        self.itemLabel=Label(master=self.__window_setting, text="-----------------------------------------Set Item----------------------------------------- ", font=(self.__jsonSetting['fontEntry'], 18,"bold"), background=self.__jsonSetting['backgroundForm'], foreground=self.__jsonSetting['backgroundLabels'])
        self.itemLabel.grid(row=2, column=0,pady=10,padx=20,sticky="w") 
        self.itemsNightButtonImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Night Button_N.jpg"))
        self.itemsNightButtonImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Night Button_B.jpg"))
        self.itemsNightButton=Label(master=self.__window_setting,image=self.itemsNightButtonImg_N,width=210,height=200,background=self.__jsonSetting['backgroundForm'])
        self.itemsNightButton.bind("<Button>", lambda event: self.setItem("Night"))
        self.itemsNightButton.grid(row=3, column=0,pady=5,padx=175,sticky="w") 
            # Items Lite
        self.itemsLiteButtonImg_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Lite Button_N.jpg"))
        self.itemsLiteButton=Label(master=self.__window_setting,image=self.itemsLiteButtonImg_N,width=210,height=200,background=self.__jsonSetting['backgroundForm'])
        self.itemsLiteButtonImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Lite Button_B.jpg"))
        self.itemsLiteButton.bind("<Button>", lambda event: self.setItem("Lite"))
        self.itemsLiteButton.grid(row=3, column=0,pady=5,padx=425,sticky="w") 
        if self.__jsonSetting['item'] =="Night":
            self.itemsNightButton.config(image=self.itemsNightButtonImg_B)
        else:
            self.itemsLiteButton.config(image=self.itemsLiteButtonImg_B)
        self.setMusicLabel=Label(master=self.__window_setting, text="----------------------------------------Set Music---------------------------------------- ", font=(self.__jsonSetting['fontEntry'], 18,"bold"), background=self.__jsonSetting['backgroundForm'], foreground=self.__jsonSetting['backgroundLabels'])
        self.setMusicLabel.grid(row=8, column=0,pady=10,padx=20,sticky="w") 
        self.checkMusic_1_Img_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button Music_N_1.jpg"))
        self.checkMusic_1_Img_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button Music_B_1.jpg"))
        self.checkMusic_1_=Label(master=self.__window_setting,image=self.checkMusic_1_Img_N,width=137,height=37,background=self.__jsonSetting['backgroundForm'])
        self.checkMusic_1_.bind("<Leave>", lambda event: self.setMusic("music_1","N"))
        self.checkMusic_1_.bind("<Button>", lambda event: self.setMusic("music_1","B"))
        self.checkMusic_1_.grid(row=9, column=0,pady=10,padx=180,sticky="w")
        self.checkMusic_2_Img_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button Music_N_2.jpg"))
        self.checkMusic_2_Img_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button Music_B_2.jpg"))
        self.checkMusic_2_=Label(master=self.__window_setting,image=self.checkMusic_2_Img_N,width=137,height=37,background=self.__jsonSetting['backgroundForm'])
        self.checkMusic_2_.bind("<Leave>", lambda event: self.setMusic("music_2","N"))
        self.checkMusic_2_.bind("<Button>", lambda event: self.setMusic("music_2","B"))
        self.checkMusic_2_.grid(row=9, column=0,pady=10,padx=330,sticky="w")
        self.checkMusic_3_Img_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button Music_N_3.jpg"))
        self.checkMusic_3_Img_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/chek Button Music_B_3.jpg"))
        self.checkMusic_3_=Label(master=self.__window_setting,image=self.checkMusic_3_Img_N,width=137,height=37,background=self.__jsonSetting['backgroundForm'])
        self.checkMusic_3_.bind("<Leave>", lambda event: self.setMusic("music_3","N"))
        self.checkMusic_3_.bind("<Button>", lambda event: self.setMusic("music_3","B"))
        self.checkMusic_3_.grid(row=9, column=0,pady=10,padx=480,sticky="w")
        if self.__jsonSetting['pageSongPath'] =="C:/ProgramData/App_Data_Soren/data/Music/Music_1.mp3":
            self.checkMusic_1_.config(image=self.checkMusic_1_Img_B)
        elif self.__jsonSetting['pageSongPath'] =="C:/ProgramData/App_Data_Soren/data/Music/Music_2.mp3":
            self.checkMusic_2_.config(image=self.checkMusic_2_Img_B)
        else: 
            self.checkMusic_3_.config(image=self.checkMusic_3_Img_B)
        self.softwareLabel=Label(master=self.__window_setting, text="-------------------------------------------Save-------------------------------------------- ", font=(self.__jsonSetting['fontEntry'], 18,"bold"), background=self.__jsonSetting['backgroundForm'], foreground=self.__jsonSetting['backgroundLabels'])
        self.softwareLabel.grid(row=10, column=0,pady=10,padx=20,sticky="w") 
        self.saveButton_N=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Save_N.jpg"))
        self.saveButton_E=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Save_E.jpg"))
        self.saveButton_B=ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Save_B.jpg"))
        self.saveButton = Label(master=self.__window_setting,image=self.saveButton_N,width=359,height=104,background=self.__jsonSetting['backgroundForm'])
        self.saveButton.bind("<Leave>", lambda event: self.saveButton.config(image=self.saveButton_N))
        self.saveButton.bind("<Enter>", lambda event: self.saveButton.config(image=self.saveButton_E))
        self.saveButton.bind("<Button>", lambda event: self.saveSetting())
        self.saveButton.grid(row=11, column=0,pady=10,padx=215,sticky="w")
    def setMusic(self,musicNumber,flag):
        if flag == 'B':
            if musicNumber =="music_1":
                self.checkMusic_1_.config(image=self.checkMusic_1_Img_B)
                self.checkMusic_2_.config(image=self.checkMusic_2_Img_N)
                self.checkMusic_3_.config(image=self.checkMusic_3_Img_N)
                self.settingText["pageSongPath"]="C:/ProgramData/App_Data_Soren/data/Music/Music_1.mp3"
            elif musicNumber=="music_2":
                self.checkMusic_1_.config(image=self.checkMusic_1_Img_N)
                self.checkMusic_2_.config(image=self.checkMusic_2_Img_B)
                self.checkMusic_3_.config(image=self.checkMusic_3_Img_N)
                self.settingText["pageSongPath"]="C:/ProgramData/App_Data_Soren/data/Music/Music_2.mp3"
            elif musicNumber=="music_3":
                self.checkMusic_1_.config(image=self.checkMusic_1_Img_N)
                self.checkMusic_2_.config(image=self.checkMusic_2_Img_N)
                self.checkMusic_3_.config(image=self.checkMusic_3_Img_B)
                self.settingText["pageSongPath"]="C:/ProgramData/App_Data_Soren/data/Music/Music_3.mp3"
    def check(self,checkName,flag):
        
        if checkName=="speed" and flag=='B':
            self.textMessage["speed"]=True
            self.checkSpeed.config(image=self.checkSpeedImg_B)
        if checkName=="designing" and flag=='B':
            self.textMessage["designing"]=True
            self.checkDesigning.config(image=self.checkDesigningImg_B)
        if checkName=="performance" and flag=='B':
            self.textMessage["performance"]=True
            self.checkPerformance.config(image=self.checkPerformanceImg_B)
    def star(self,starNumber,flag):
        if flag == 'B':
            if starNumber ==1:
                self.textMessage["star"]=1
                self.star_1_Button.config(image=self.starButtonImg_B)
            elif starNumber==2:
                self.textMessage["star"]=2
                self.star_1_Button.config(image=self.starButtonImg_B)
                self.star_2_Button.config(image=self.starButtonImg_B)
            elif starNumber==3:
                self.textMessage["star"]=3
                self.star_1_Button.config(image=self.starButtonImg_B)
                self.star_2_Button.config(image=self.starButtonImg_B)
                self.star_3_Button.config(image=self.starButtonImg_B)
            elif starNumber==4:
                self.textMessage["star"]=4
                self.star_1_Button.config(image=self.starButtonImg_B)
                self.star_2_Button.config(image=self.starButtonImg_B)
                self.star_3_Button.config(image=self.starButtonImg_B)
                self.star_4_Button.config(image=self.starButtonImg_B)
            elif starNumber==5:
                self.textMessage["star"]=5
                self.star_1_Button.config(image=self.starButtonImg_B)
                self.star_2_Button.config(image=self.starButtonImg_B)
                self.star_3_Button.config(image=self.starButtonImg_B)
                self.star_4_Button.config(image=self.starButtonImg_B)
                self.star_5_Button.config(image=self.starButtonImg_B)
            starNumber = 5-starNumber
            self.starButtonImg_E = self.starButtonImg_B
            self.starButtonImg_N=self.starButtonImg_B
        elif flag == 'E':
            if starNumber ==1:
                self.star_1_Button.config(image=self.starButtonImg_E)
            elif starNumber==2:
                self.star_1_Button.config(image=self.starButtonImg_E)
                self.star_2_Button.config(image=self.starButtonImg_E)
            elif starNumber==3:
                self.star_1_Button.config(image=self.starButtonImg_E)
                self.star_2_Button.config(image=self.starButtonImg_E)
                self.star_3_Button.config(image=self.starButtonImg_E)
            elif starNumber==4:
                self.star_1_Button.config(image=self.starButtonImg_E)
                self.star_2_Button.config(image=self.starButtonImg_E)
                self.star_3_Button.config(image=self.starButtonImg_E)
                self.star_4_Button.config(image=self.starButtonImg_E)
            elif starNumber==5:
                self.star_1_Button.config(image=self.starButtonImg_E)
                self.star_2_Button.config(image=self.starButtonImg_E)
                self.star_3_Button.config(image=self.starButtonImg_E)
                self.star_4_Button.config(image=self.starButtonImg_E)
                self.star_5_Button.config(image=self.starButtonImg_E)
        else:
            if starNumber==1:
                self.star_1_Button.config(image=self.starButtonImg_N)
            elif starNumber==2:
                self.star_1_Button.config(image=self.starButtonImg_N)
                self.star_2_Button.config(image=self.starButtonImg_N)
            elif starNumber==3:
                self.star_1_Button.config(image=self.starButtonImg_N)
                self.star_2_Button.config(image=self.starButtonImg_N)
                self.star_3_Button.config(image=self.starButtonImg_N)
            elif starNumber==4:
                self.star_1_Button.config(image=self.starButtonImg_N)
                self.star_2_Button.config(image=self.starButtonImg_N)
                self.star_3_Button.config(image=self.starButtonImg_N)
                self.star_4_Button.config(image=self.starButtonImg_N)
            elif starNumber==5:
                self.star_1_Button.config(image=self.starButtonImg_N)
                self.star_2_Button.config(image=self.starButtonImg_N)
                self.star_3_Button.config(image=self.starButtonImg_N)
                self.star_4_Button.config(image=self.starButtonImg_N)
                self.star_5_Button.config(image=self.starButtonImg_N)
    def setItem(self, item):
        if item=="Night":
            self.__jsonSetting['item']="Night"
            self.itemsNightButton.config(image=self.itemsNightButtonImg_B)
            self.itemsLiteButton.config(image=self.itemsLiteButtonImg_N)
            self.settingText["backgroundForm"]="#404040"
            self.settingText["item"]="Night"
        elif item=="Lite":
            self.__jsonSetting['item']="Lite"
            self.itemsLiteButton.config(image=self.itemsLiteButtonImg_B)
            self.itemsNightButton.config(image=self.itemsNightButtonImg_N)
            self.settingText["backgroundForm"]="#ffffff"
            self.settingText["item"]="Lite"
    def saveSetting(self):
        with open("C:/ProgramData/App_Data_Soren/data/Setting/Setting.json",'w') as settingFile:
            dump(self.settingText,settingFile, indent=4)
        self.buttonSong.music.stop()
        self.__window.destroy()
        exit(system(r'python C:\Users\asus\Desktop\Programming\Python/PythonAdvanced\Practice\peractice_9\Python\32\Main.py'))
    def microphone(self,entryName):
        entryName.delete(0, 'end')
    def help(self,nameHelp,videoAddress):
        VideoDisplay(videoAddress,nameHelp,self.__jsonSetting['icon'])
    def pause(self,nameButton,file):
        nameButton.config(image=file)
        self.__pageSong.music.pause()
    def unpause(self,nameButton,file):
        nameButton.config(image=file)
        self.__pageSong.music.unpause()
    def stop(self,nameButton,file):
        nameButton.config(image=file)
        self.__pageSong.music.stop()   
    def button_Enter(nameButton,file=None):
        nameButton.config(image=file)
    def show(self,nameButton,state,country):
        answer = True
        if state == "" or country =="":
            answer=askretrycancel("Error","You did not enter the name of the province")
        else:
            self.items=apiData(self.__url,f"country={country}")
            self.bShowImg_3= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Show Button_B.jpg"))
            nameButton.config(image=self.bShowImg_3)
            self.__window_show=Toplevel(self.__window)
            GUI.windowSize(self.__window_show,750,800)
            self.__window_show.title("Universitys")
            self.__window_show.configure(bg=self.__jsonSetting['backgroundForm'])
            self.__window_show.iconbitmap(self.__jsonSetting['icon'])
            self.buttonSong = mixer
            self.buttonSong.init()
            self.buttonSong.music.load(self.__jsonSetting['buttonSongPath'])
            self.buttonSong.music.play()
            sleep(0.18)
            self.__pageSong.music.load(self.__jsonSetting['pageSongPath'])
            self.buttonSong.music.play()
            self.__imgForm = Label(master=self.__window_show, text="🏫", font=(None, 170), background=self.__jsonSetting['backgroundForm'], foreground=self.__jsonSetting['backgroundLabels'])
            self.__imgForm.grid(row=0, column=0,pady=5,padx=10)
            self.textLabel = Label(master=self.__window_show, text="You can choose and open the website",foreground=self.__jsonSetting['backgroundLabels'] , background=self.__jsonSetting['backgroundForm'] ,font=(self.__jsonSetting['fontLabel'],22))
            self.style=ttk.Style()
            self.style.configure("BW.TLabel", foreground=self.__jsonSetting['backgroundLabels'], background=self.__jsonSetting['backgroundForm'],font=(self.__jsonSetting['fontEntry'],12,"bold"))
            self.textLabel.grid(row=2, pady=5, padx=30, sticky="w")
            tree = ttk.Treeview(master=self.__window_show, column=("Row","University Name", "Web Page"), show='headings', height=7)
            tree.config(style="BW.TLabel")
            tree.column("# 1", anchor=CENTER, width=50)
            tree.heading("# 1", text="Row")
            tree.column("# 2", anchor=CENTER, width=420)
            tree.heading("# 2", text="University Name ")
            tree.column("# 3", anchor=CENTER, width=230)
            tree.heading("# 3", text="Web Page")
            tree.bind('<<TreeviewSelect>>',lambda event: self.openWeb(tree))
            self.counter = 1
            self.csvText="row,University Name,Web Page\n"
            for item in self.items:
                if item["state-province"]==state:
                    name=item["name"].replace(","," ")
                    self.csvText+=f"{str(self.counter)},{name},{item['web_pages'][0]}\n"
                    tree.insert('', 'end', text=str(self.counter), values=(self.counter,item["name"],item["web_pages"]))
                    self.counter += 1
            tree.grid(row=3, columnspan=3, pady=5, padx=20, sticky="w")
            self.counterLabel = Label(master=self.__window_show,text=f"**** ({self.counter-1}) Found ****",foreground=self.__jsonSetting['backgroundLabels'] , background=self.__jsonSetting['backgroundForm'] ,font=(self.__jsonSetting['fontEntry'],20))
            self.counterLabel.grid(row=4,  pady=5, padx=250, sticky="w")
            self.returnButtonImg_N= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Return Button_N.jpg"))
            self.returnButton = Label(master=self.__window_show,image=self.returnButtonImg_N,width=585,height=106,background=self.__jsonSetting['backgroundForm'])
            self.returnButton.bind("<Leave>", lambda event: self.returnButton.config(image=self.returnButtonImg_N))
            self.returnButtonImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Return Button_E.jpg"))
            self.returnButton.bind("<Enter>", lambda event: GUI.button_Enter(self.returnButton,self.returnButtonImg_E))
            self.returnButton.bind("<Button>", lambda event: self.__window_show.destroy())
            self.returnButton.grid(row=6, column=0,pady=5,padx=50)
            self.saveCSVButtonImg_N= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Save_CSV_File_Button_N.jpg"))
            self.saveCSVButton = Label(master=self.__window_show,image=self.saveCSVButtonImg_N,width=250,height=104,background=self.__jsonSetting['backgroundForm'])
            self.saveCSVButton.bind("<Leave>", lambda event: self.saveCSVButton.config(image=self.saveCSVButtonImg_N))
            self.saveCSVButtonImg_E= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Save_CSV_File_Button_E.jpg"))
            self.saveCSVButtonImg_B= ImageTk.PhotoImage(Image.open(f"C:/ProgramData/App_Data_Soren/data/Images/{self.__jsonSetting['item']}/Save_CSV_File_Button_B.jpg"))
            self.saveCSVButton.bind("<Enter>", lambda event: GUI.button_Enter(self.saveCSVButton,self.saveCSVButtonImg_E))
            self.saveCSVButton.bind("<Button>", lambda event: self.saveCSV())
            self.saveCSVButton.grid(row=5, column=0,pady=5,padx=250)
            self.__window_show.mainloop()
        if answer == False:
            self.__window.destroy()
    def saveCSV(self):
        self.saveCSVButton.config(image=self.saveCSVButtonImg_B)
        self.location = askdirectory(initialdir="YOUR LOCATION PATH ", title="Save")
        if self.location !="":
            try:
                with open(f"{self.location}/University.csv",'w') as csvFile:
                    csvFile.write(self.csvText)
                    showinfo("Info","File saved ...")
            except Exception as error:
                showerror("Error",error)
    def openWeb(self,name):
        for sItem in name.selection():
            open_new(name.item(sItem)["values"][2])
    def windowSize(form, width, height):
        w = width
        h = height
        ws = form.winfo_screenwidth()
        hs = form.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        form.minsize(width, height)
        form.maxsize(width, height)
        form.geometry("%dx%d+%d+%d" % (w, h, x, y))
    def action(name,img):
        name.config(image=img)
