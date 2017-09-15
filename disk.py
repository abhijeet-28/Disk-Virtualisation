import block
class disk:
	id=0
	d_size=200
	block_array=[]
	bitmap=None
  
	

	def __init__(self,size,block_size=100):
		self.d_size=size
		self.bitmap=[False]*size
		for i in xrange(size):
			block_obj=block.block(block_size)
			self.block_array.append(block_obj)

	def writetodisk(self,Block_no,info):
		size=len(info)
		if self.block_array[Block_no].put(info):
			self.bitmap[Block_no]=True
		 	return True
		else:
			return False					

	def readfromdisk(self,Block_no):
		if Block_no<self.d_size:
			block=self.block_array[Block_no]
			return block.read()
		else:
			return None

if __name__ == "__main__":
	dis=disk(200)
	arr=[1,2,3]

	x=dis.writetodisk(10,arr)
	print x
	val=dis.readfromdisk(10)
	print val


	
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  