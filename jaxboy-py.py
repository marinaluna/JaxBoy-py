###################################################
## © Marina Terry 2020 ############################
###################################################
from gameboy import GameBoy
from sdlcontext import SDLContext
from ppu import PPU
from options import Options
import common

### Screen width and height ###
width = 160
height = 144
### Scale for the display ###
scale = 1
### Main GameBoy instance ###
gameboy = 0
### SDL context ###
sdl_context = 0

### Entry point ###
def main():
	options = Options()
	gameboy = GameBoy(options, width, height, None, None)
	sdl_context = SDLContext(width, height, scale, gameboy)

	while(gameboy.isRunning() and sdl_context.isRunning()):
		gameboy.cycle()
		sdl_context.update(gameboy.getPPU().getBackBuffer())
		sdl_context.pollEvents(gameboy)

main()
