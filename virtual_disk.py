import real_disk
class virtual_disk:
	id=0
	d_size=0
	block_map=[]

	def __init__(self,rd,size,id,block_size=100):
		if rd.free_mem<size:
			print('Not enough space,Cant create disk')
			return
		self.d_size=size
		self.id=id
		cur_size=0
		self.block_map=[]
		for i in xrange(rd.size) :
			if cur_size<size:
				if not rd.bitmap[i]:
					self.block_map.append(i)
					rd.bitmap[i]=True
					rd.free_mem-=1
					cur_size=cur_size+1

			else:
				break


	def copy_virtual_disk(self,rd,vd):

		for x in xrange(self.d_size):
			rd.write(self.block_map[x],list(rd.read(vd.block_map[x]).block_mem))

		#print "map",rd.read(self.block_map[100])

	def delete_disk(self,rd):
		for i in self.block_map:
			rd.bitmap[i]=False
		rd.free_mem+=self.d_size
		self.d_size=0
		self.block_map=[]
        

	def write(self,rd,Block_no,info):
		if Block_no<self.d_size:
			i = self.block_map[Block_no]
			return rd.write(i,info)	
		return False
				

	def read(self,rd,Block_no):
		if Block_no<self.d_size:
			i = self.block_map[Block_no]
			return rd.read(i)
		return None

	def size(self):
		return self.d_size

	def get_id(self):
		return self.id

if __name__ == "__main__":
  rd=real_disk.real_disk()
  rd.add_disk(300)
  rd.add_disk(200)
  vd1=virtual_disk(rd,350,0)
  arr=[1,2,3]
  x=vd1.write(rd,320,arr)
  print x
  y=vd1.read(rd,320)
  print y
  vd2=virtual_disk(rd,150,1)
  # vd2.delete_disk(rd)
  # vd3=virtual_disk(rd,100,1)
  print vd1.block_map
  print vd2.block_map

  print 'size',vd1.size()
  print 'size',vd2.size()
