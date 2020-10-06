###################################################
## © Marina Terry 2020 ############################
###################################################
from common import *

class Graphics:
	class Tile:
		### Rows of the tile ###
		rows = list()
		### Constructor ###
		def __init__(self):
			for i in range(8):
				rows.append(0x00)
		### Decodes data from src into the Tile's rows data ###
		def decode(self, src):
			for row in range(8):
				upper = src[(row*2)+1] << 16
				lower = src[row*2]
				morton = upper | lower
				morton = (morton ^ (morton << 4)) & 0x0F0F0F0F
				morton = (morton ^ (morton << 2)) & 0x33333333
				morton = (morton ^ (morton << 1)) & 0x55555555
				self.rows[row] = (morton | (morton >> 15))
		### Gets color of pixel at the given x and y coordinate ###
		def getPixel(self, x, y):
			# Mask out the two bits for the pixel we want
			# then shift it back to the bottom for an
			# array index
			x *= 2
			return ((self.rows[y] & (0xC000 >> x)) >> (14 - x))

	class Sprite:
		### Data for the sprite ###
		_y = 0
		_x = 0
		_id = 0
		_priority = 0
		_flipY = False
		_flipX = False
		_palette = 0
		### Decodes the data for this sprite from a src array ###
		def decode(self, src):
			self._y = src[0]
			self._x = src[1]
			self._id = src[2]
			self._priority = (src[3] & 0x80) >> 7
			self._flipY = (src[3] & 0x40) != 0
			self._flipX = (src[3] & 0x20) != 0
			self._palette = (src[3] & 0x10) >> 4


class PPU:
	### GameBoy instance ###
	gameboy = 0
	### Screen width and height ###
	width = 0
	height = 0
	### Memory Bus instance ###
	bus = 0
	### Backbuffer that the gameboy draws to and is copied to the front buffer for displaying ###
	backBuffer = 0
	### Tile sets ###
	bgTileset = 0
	objTileset = 0
	### Palettes ###
	bgPalette = list()
	objPalette0 = list()
	objPalette1 = list()
	### IO Regs ###
	lcdc = 0
	stat = 0
	scy = 0
	scx = 0
	ly = 0
	lyc = 0
	wy = 0
	wx = 0
	### Number of cycles this frame ###
	frameCycles = 0


	### Constructor ###
	def __init__(self, gameboy, width, height, bus):
		self.gameboy = gameboy
		self.width = width
		self.height = height
		self.bus = bus
		### Init the back buffer by setting the entire thing to "white" ###
		self.backBuffer = list()
		for i in range(width*height):
			self.backBuffer.append(gColors[0])

		self.bgTileset = list()
		self.objTileset = list()


		self.stat |= DisplayModes.VBLANK
		### Initialize the palettes ###
		for i in range(4):
			self.bgPalette.append(gColors[0])
			self.objPalette0.append(gColors[0])
			self.objPalette1.append(gColors[0])

	### Returns the back buffer; called in the SDL context ###
	def getBackBuffer(self):
		return self.backBuffer

	### Main PPU update function ###
	def update(self):
		return
