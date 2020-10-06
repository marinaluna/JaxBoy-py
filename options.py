###################################################
## © Marina Terry 2020 ############################
###################################################

class Options:
	### This class just contains options that the system can be started with ###
	debug = False
	scale = 1
	force_mbc = -1
	skip_bootrom = False
	framelimiter_hack = False

	### Constructor ###
	def __init__(self, _debug=False, _scale=1, _force_mbc=-1, _skip_bootrom=False, _framelimiter_hack=False):
		self.debug = _debug
		self.scale = _scale
		self.force_mbc = _force_mbc
		self.skip_bootrom = _skip_bootrom
		self.framelimiter_hack = _framelimiter_hack