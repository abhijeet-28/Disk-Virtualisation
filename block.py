class block:

	block_size = 100
	block_mem = None
	
	def __init__(self,block_size):
		self.block_size = block_size
		self.block_mem = bytearray(self.block_size)

	def put(self,block_info):
		if len(block_info)<=self.block_size:
			self.block_mem = bytearray(block_info)
			return True
		else:
			return False


	def read(self):
		return self.block_mem

	def size(self):
		return self.block_size


if __name__ == "__main__":
	block_ob = block(100)
	block_ob.put([1,2,3])
	print block_ob.block_mem[0]
	print block_ob.block_size