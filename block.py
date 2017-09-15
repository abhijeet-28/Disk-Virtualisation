class block:

	block_size = 100
	block_mem = None
	
	def __init__(self,block_size=100):
		self.block_size = block_size
		self.block_mem = bytearray(self.block_size)

	def put(self,block_info):
		if len(block_info)<=self.block_size:
			self.block_mem = bytearray(block_info)
			return True
		else:
			return False

	def read(self):
		return self

	def size(self):
		return self.block_size

	def __str__(self):
		temp=""
		for x in self.block_mem:
			temp = temp + str(x) + " "
		return temp


if __name__ == "__main__":
	block_ob = block(100)
	block_ob.put([1,2,3])
	print block_ob
	print block_ob.block_size