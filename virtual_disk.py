import real_disk
import random
class virtual_disk:
	id=0
	d_size=0
	block_map=[]
	block_map_copy=[]

	def __init__(self,rd,size,id,block_size=100):
		if rd.free_mem<2*size:
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

		cur_size=0
		self.block_map_copy=[]
		for i in xrange(rd.size) :
			if cur_size<size:
				if not rd.bitmap[i]:
					self.block_map_copy.append(i)
					rd.bitmap[i]=True
					rd.free_mem-=1
					cur_size=cur_size+1
			else:
				break


	def block_copy(self,rd,Block_no,tar):
		for i in xrange(rd.size) :
			if not rd.bitmap[i]:
				self.block_map[Block_no] = i
				rd.write(i,rd.read(tar).block_mem)
				rd.bitmap[i]=True
				rd.free_mem-=1
				return True
		return False

		

	def delete_disk(self,rd):
		for i in self.block_map:
			rd.bitmap[i]=False

		for i in self.block_map_copy:
			rd.bitmap[i]=False

		rd.free_mem+=2*self.d_size
		self.d_size=0
		self.block_map=[]
		self.block_map_copy=[]
        

	def write(self,rd,Block_no,info):
		if Block_no<self.d_size:
			i = self.block_map[Block_no]
			j = self.block_map_copy[Block_no]
			return rd.write(i,info) and rd.write(j,info)	
		return False
				

	def read(self,rd,Block_no):
		if Block_no<self.d_size:
			if random.randint(0, 100)>=50:
				i = self.block_map[Block_no]
				return rd.read(i)
			else:
				print "Block Read Error: Block read from copy"
				i = self.block_map_copy[Block_no]
				self.block_copy(rd,Block_no,i)
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
  vd1=virtual_disk(rd,249,0)
  arr=[1,2,3]
  x=vd1.write(rd,60,arr)
  print x
  y=vd1.read(rd,60)
  print y
  print "free",rd.free_mem
  y=vd1.read(rd,60)
  print y
  print "free",rd.free_mem
  y=vd1.read(rd,60)
  print y
  print "free",rd.free_mem
  vd1.delete_disk(rd)
  vd1 = virtual_disk(rd,249,0)
  print vd1.size()
  
