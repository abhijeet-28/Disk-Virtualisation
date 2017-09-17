import real_disk
class virtual_disk:
	id=0
	d_size=0
	block_map=[]
	dirty_map=[]
	dirty_bl=0

	def __init__(self,rd,size,id,block_size=100):
		if rd.free_mem<size:
			print('Not enough space,Cant create disk')
			return
		self.d_size=size
		self.id=id
		cur_size=0
		self.dirty_bl=0
		self.block_map=[]
		self.dirty_map=[]
		for i in xrange(rd.size) :
			if cur_size<size:
				if not rd.bitmap[i]:
					self.block_map.append(i)
					self.dirty_map.append(False)

					rd.bitmap[i]=True
					rd.free_mem-=1
					cur_size=cur_size+1

			else:
				break
	def extend_virtual_disk(self,rd,size,id,block_size=100):
		if rd.free_mem<size:
			print('Not enough space,Cant create disk')
			return None
		self.d_size+=size
		self.id=id
		cur_size=0
		for i in xrange(rd.size) :
			if cur_size<size:
				if not rd.bitmap[i]:
					self.block_map.append(i)
					self.dirty_map.append(False)
					rd.bitmap[i]=True
					rd.free_mem-=1
					cur_size=cur_size+1

			else:
				break
		return self


	def copy_virtual_disk(self,rd,vd):
		c=0
		for x in xrange(vd.size()):
			if c>=self.size():
				break
			index=vd.block_map[x]
			if vd.dirty_map[x]:
				z1=(rd.read(index).block_mem)
				v1=z1[:]
				self.write(rd,c,list(v1))
				c+=1
		self.dirty_map=vd.dirty_map[:]
		self.dirty_bl=vd.dirty_bl

		#print "map",rd.read(self.block_map[100])
	def copy_roll_disk(self,rd,vd):
		c=0
		for x in xrange(len(vd.dirty_map)):
			if vd.dirty_map[x]:
				index=vd.block_map[c]
				z1=(rd.read(index).block_mem)
				v1=z1[:]
				self.write(rd,x,list(v1))
				c+=1
		self.dirty_map=vd.dirty_map[:]
		self.dirty_bl=vd.dirty_bl

	def delete_disk(self,rd):
		for i in self.block_map:
			rd.bitmap[i]=False
		rd.free_mem+=self.d_size
		self.d_size=0
		self.block_map=[]
		self.dirty_map=[]
		self.dirty_bl=0
        

	def write(self,rd,Block_no,info):
		if Block_no<self.d_size:
			i = self.block_map[Block_no]
			self.dirty_map[Block_no]=True
			self.dirty_bl+=1
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

# if __name__ == "__main__":
#   rd=real_disk.real_disk()
#   rd.add_disk(300)
#   rd.add_disk(200)
#   vd1=virtual_disk(rd,350,0)
#   arr=[1,2,3]
#   x=vd1.write(rd,320,arr)
#   print x
#   y=vd1.read(rd,320)
#   print y
#   vd2=virtual_disk(rd,150,1)
#   # vd2.delete_disk(rd)
#   # vd3=virtual_disk(rd,100,1)
#   print vd1.block_map
#   print vd2.block_map

#   print 'size',vd1.size()
#   print 'size',vd2.size()
