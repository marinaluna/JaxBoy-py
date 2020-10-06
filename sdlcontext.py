###################################################
## © Marina Terry 2020 ############################
###################################################
from sdl2 import *
import sdl2.ext
import random

import common

class SDLContext:
    ### Width and Height of the window ###
    width = 0
    height = 0
    ### Scale of the window ###
    scale = 500
    ### Window instance ###
    window = 0
    ### RGB Surface ###
    surface = 0
    ### Event ###
    events = 0

    ### Flag to keep track of whether the context is running ###
    _running = True

    ### Constructor ###
    def __init__(self, width, height, scale, gameboy):
        self.width = width
        self.height = height
        self.scale = scale
        
        sdl2.ext.init()
        #window_name = gameboy.getCurrentRom().getRomName()
        self.window = sdl2.ext.Window(  "JaxBoy-py",
                                        size=(self.width * self.scale,
                                        self.height * self.scale))
        self.window.show()

        ### Create graphics renderer so we can draw pixels to the screen ###
        self.renderer = sdl2.ext.Renderer(self.window)


    ### Updates each tick ###
    def update(self, backBuffer):
        for x in range(self.width*self.scale):
            for y in range(self.height*self.scale):
                point_loc = (y*self.width*self.scale) + x
                self.renderer.color = backBuffer[point_loc]
                self.renderer.draw_point((x, y))
        self.renderer.present()

    ### Stops the SDL context ###
    def stop(self):
        self._running = False

    ### Checks if the context is running ###
    def isRunning(self):
        return self._running

    ### Polls events such as key presses or closing the window ###
    def pollEvents(self, gameboy):
        self.events = sdl2.ext.get_events()
        for event in self.events:
            if(event.type == SDL_QUIT):
                self.stop()
                break
