import real_disk
import virtual_disk
class hypervisor:
	v_disks=[]
	rd=real_disk.real_disk()

	def add_phydisk(self,d_size):
		self.rd.add_disk(d_size)


	def create_virtual_disk(self,size,id):
		if self.get_virtual_disk(id)==None:
			vd=virtual_disk.virtual_disk(self.rd,size,id)
			self.v_disks.append(vd)
			return vd
		print 'Virtual disk with same id already exists'
	def delete_virtual_disk(self,id):
		for i in self.v_disks:
			if i.get_id()==id:
				i.delete_disk(self.rd)
				self.v_disks.remove(i)
				return

	def	write(self,id,Block_no,info):
		for i in self.v_disks:
			if i.get_id()==id:
				return i.write(self.rd,Block_no,info)
		return False

	def read(self,id,Block_no):
		for i in self.v_disks:
			if i.get_id()==id:
				return i.read(self.rd,Block_no)
		return None

	def get_virtual_disk(self,id):
		for i in self.v_disks:
			if i.get_id()==id:
				return i
		return None

if __name__ == "__main__":
  h=hypervisor()
  h.add_phydisk(300)
  h.add_phydisk(200)
  vd1=h.create_virtual_disk(150,1)
  vd2=h.create_virtual_disk(350,2)
  arr=[1,2,4]
  x=h.write(1,100,arr)
  print x
  y=h.read(1,100)
  print vd1.size()
  print vd2.size()
  h.delete_virtual_disk(2)
  vd3=h.create_virtual_disk(50,3)
  vd4=h.create_virtual_disk(50,2)
  vd5=h.create_virtual_disk(50,5)

  print vd1.block_map
  h.delete_virtual_disk(3)
  vd6=h.create_virtual_disk(100,6)
  print vd6.block_map

  z= h.read(1,100)
  print y
  


