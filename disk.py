import block
class disk:
	id=0
	d_size=200
	block_array=[]
  
	

	def __init__(self,size,id,block_size=100):
		self.d_size=size
		self.id=id
		for i in xrange(size):
			block_obj=block.block(block_size)
			self.block_array.append(block_obj)

	def writetodisk(self,Block_no,info):
		if self.block_array[Block_no].put(info):
		 	return True
		else:
			return False					

	def readfromdisk(self,Block_no):
		if Block_no<self.d_size:
			block=self.block_array[Block_no]
			return block.read()
		else:
			return None

	def size(self):
		return self.d_size

	def get_id(self):
		return self.id

if __name__ == "__main__":
	dis=disk(200,0)
	arr=[1,2,3]

	x=dis.writetodisk(10,arr)
	print x
	val=dis.readfromdisk(10)
	print val


	
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  