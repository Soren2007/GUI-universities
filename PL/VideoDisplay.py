from moviepy.editor import *
import pygame
class VideoDisplay:
    def __init__(self,videoAddress,name,iconAddress):
        self.__videoAddress = videoAddress
        self.__name = name
        self.__iconAddress =iconAddress
        pygame.display.set_caption(self.__name)
        pygame.display.set_icon(self.__iconAddress)
        clip = VideoFileClip(self.__videoAddress)
        clip.preview()
        pygame.quit()
