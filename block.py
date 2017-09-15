class block:

	block_size = 100
	block_mem = None

	def __init__(self):
		self.block_mem = bytearray(self.block_size)
	
	def __init__(self,block_size):
		self.block_size = block_size
		self.block_mem = bytearray(self.block_size)