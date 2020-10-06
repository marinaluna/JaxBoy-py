###################################################
## © Marina Terry 2020 ############################
###################################################
from bus import Bus
from cpu import CPU
from ppu import PPU
from options import Options

class GameBoy:
	### Memory bus ###
    bus = 0
	### CPU instance ###
    cpu = 0
	### PPU instance ###
    ppu = 0
	### Is the system currently running? ###
    _running = True
    ### GameBoy's options instance ###
    _options = Options()
    

    ### Constructor ###
    def __init__(self, options, width, height, rom, bootrom):
        self.bus = Bus(self)

        self.cpu = CPU(self, self.bus)
        self.ppu = PPU(self, width, height, self.bus)

        self._options = options

    ### Returns the options instance ###
    def getOptions(self):
        return self._options

    ### Returns the PPU instance ###
    def getPPU(self):
        return self.ppu

    ### GameBoy system cycle ###
    def cycle(self):
        cycles = self.cpu.tick()
        if(self.ppu.update() == -1):
            stop()

    ### Stop the GameBoy from running any further ###
    def stop(self):
        self._running = False

    ### Check if the GameBoy is running ###
    def isRunning(self):
        return self._running
