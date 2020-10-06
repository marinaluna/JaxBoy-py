###################################################
## © Marina Terry 2020 ############################
###################################################
import gameboy
import options


class CPU:
	### GameBoy instance ###
	gameboy = 0
	### Memory Bus instance ###
	bus = 0
	### 16-bit Registers ###
	pc = 0
	sp = 0
	### 8-bit Registers ###
	a = 0
	f = 0
	b = 0
	c = 0
	d = 0
	e = 0
	h = 0
	l = 0
	### Interrupt registers ###
	_ime = 0
	_ie = 0
	_if = 0

	### Constructor ###
	def __init__(self, gameboy, bus):
		self.gameboy = gameboy
		self.bus = bus

		if(self.gameboy.getOptions().skip_bootrom):
			pc = 0x0100
			sp = 0xFFFE

		self._ime = True

	### Executes any interrupts that are scheduled ###
	def tickInterrupts(self):
		if(self._ime):
			### Checks if there are any interrupts for us to execute ###
			if(self._ie and self._if):
				### Masks out only the interrupts that have IE and IF set ###
				interruptPending = self._ie & self._if
				### The priority of each interrupt is determined by
				### their position in the bit mask of IE/IF ###
				###
				### 00000001b - V-Blank: highest priority
				### 00000010b - STAT
				### 00000100b - Timer
				### 00001000b - Serial
				### 00010000b - JoyPad: lowest priority
				if(interruptPending & 0x01):
					### V-Blank ###
					self._ime = False
					self._if &= ~0x01

					self.call(0x0040)
					return 12
				if(interruptPending & 0x02):
					### STAT ###
					self._ime = False
					self._if &= ~0x02

					self.call(0x0048)
					return 12
				if(interruptPending & 0x04):
					### Timer ###
					self._ime = False
					self._if &= ~0x04

					self.call(0x0050)
					return 12
				if(interruptPending & 0x08):
					### Serial ###
					self._ime = False
					self._if &= ~0x08

					self.call(0x0058)
					return 12
				if(interruptPending & 0x10):
					### JoyPad ###
					self._ime = False
					self._if &= ~0x10

					self.call(0x0060)
					return 12

		return 0

	### Get operand 8-bit and 16-bit ###
	def getOperand8(self):
		operand = self.bus.read8(self.pc)
		self.pc += 1
		return operand
	def getOperand16(self):
		operand = self.bus.read16(self.pc)
		self.pc += 2
		return operand

	### Combines two 8-bit regs to return their 16-bit form ###
	def getVal16(self, a, b):
		return (a << 8) | b

	### Increments HL ###
	def incHL(self):
		self.l += 1
		if(self.l > 0xFF):
			self.l &= 0xFF
			self.h = (self.h + 1) & 0xFF

	### Decrements HL ###
	def decHL(self):
		num16 = self.getVal16(self.h, self.l)
		num16 -= 1
		self.h = (num16 >> 8) & 0xFF
		self.l = num16 & 0xFF

	### Executes the next instruction ###
	def executeNext(self):
		opcode = self.bus.read8(self.pc)
		self.pc += 1

		if(opcode == 0xCB):
			#executeCBOpcode()
			return 0
		elif(opcode == 0x00):
			return 0
		elif(opcode == 0x10):
			return 0
		elif(opcode == 0x76):
			return 0
		elif(opcode == 0xF3):
			_ime = False
		elif(opcode == 0xFB):
			_ime = True
		### LD reg8, u8
		elif(opcode == 0x06):
			self.b = self.getOperand8()
		elif(opcode == 0x0E):
			self.c = self.getOperand8()
		elif(opcode == 0x16):
			self.d = self.getOperand8()
		elif(opcode == 0x1E):
			self.e = self.getOperand8()
		elif(opcode == 0x26):
			self.h = self.getOperand8()
		elif(opcode == 0x2E):
			self.l = self.getOperand8()
		elif(opcode == 0x3E):
			self.a = self.getOperand8()
		elif(opcode == 0x0A):
			self.a = self.bus.read8(self.getVal16(self.b, self.c))
		elif(opcode == 0x1A):
			self.a = self.bus.read8(self.getVal16(self.d, self.e))
		elif(opcode == 0x2A):
			self.a = self.bus.read8(self.getVal16(self.h, self.l))
			self.incHL()
		elif(opcode == 0x3A):
			self.a = self.bus.read8(self.getVal16(self.h, self.l))
			self.decHL()
		elif(opcode == 0x46):
			self.b = self.bus.read8(self.getVal16(self.h, self.l))
		elif(opcode == 0x4E):
			self.c = self.bus.read8(self.getVal16(self.h, self.l))
		elif(opcode == 0x56):
			self.d = self.bus.read8(self.getVal16(self.h, self.l))
		elif(opcode == 0x5E):
			self.e = self.bus.read8(self.getVal16(self.h, self.l))
		elif(opcode == 0x66):
			self.h = self.bus.read8(self.getVal16(self.h, self.l))
		elif(opcode == 0x6E):
			self.l = self.bus.read8(self.getVal16(self.h, self.l))
		elif(opcode == 0x7E):
			self.a = self.bus.read8(self.getVal16(self.h, self.l))
		return 0
		#elif(opcode == 0xF0):
		#elif(opcode == 0xF2):
		#elif(opcode == 0xFA):
		#elif(opcode == 0x40):
		#elif(opcode == 0x41):
		#elif(opcode == 0x42):
		#elif(opcode == 0x43):
		#elif(opcode == 0x44):
		#elif(opcode == 0x45):
		#elif(opcode == 0x47):
		#elif(opcode == 0x48):
		#elif(opcode == 0x49):
		#elif(opcode == 0x4A):
		#elif(opcode == 0x4B):
		#elif(opcode == 0x4C):
		#elif(opcode == 0x4D):
		#elif(opcode == 0x4F):
		#elif(opcode == 0x):
		#elif(opcode == 0x):
		#elif(opcode == 0x):
		#elif(opcode == 0x):
		#elif(opcode == 0x):
		#elif(opcode == 0x):
		#elif(opcode == 0x):
		#elif(opcode == 0x):

	### Main CPU ticking function ###
	def tick(self):
		new_cycles = self.executeNext()
		new_cycles += self.tickInterrupts()

		return new_cycles
