###################################################
## © Marina Terry 2020 ############################
###################################################
import sdl2.ext
from enum import IntEnum

### Enum of display modes ###
class DisplayModes(IntEnum):
	HBLANK = 0,
	VBLANK = 1,
	OAMACCESS = 2,
	UPDATE = 3

### Array of colors that can be displayed on the screen ###
gColors = [
	# White
	sdl2.ext.Color(0x9B, 0xBC, 0x0F),
	# Light grey
	sdl2.ext.Color(0x8B, 0xAC, 0x0F),
	# Dark grey
	sdl2.ext.Color(0x30, 0x62, 0x30),
	# Black
	sdl2.ext.Color(0x0F, 0x38, 0x0F)
]