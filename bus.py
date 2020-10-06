###################################################
## © Marina Terry 2020 ############################
###################################################

class Bus:
	### GameBoy instance ###
	gameboy = 0

	### Constructor ###
	def __init__(self, gameboy):
		self.gameboy = gameboy

	### Read 8-bit data ###
	def read8(self, addr):
		return 0xFF

	### Read 16-bit data ###
	def read16(self, addr):
		return 0xFFFF

