import real_disk
import virtual_disk
class hypervisor:
	v_disks=[]
	check_points=[]
	rd=real_disk.real_disk()

	def add_phydisk(self,d_size):
		self.rd.add_disk(d_size)


	def create_virtual_disk(self,size,id):
		if self.get_virtual_disk(id)==None:
			vd=virtual_disk.virtual_disk(self.rd,size,id)
			if vd.size()==0:
				return None
			else:
				self.v_disks.append(vd)
				return vd
		print 'Virtual disk with same id already exists'
		return None

	def checkpoint(self,id,no):
		if self.get_check_points(id,no)==None:
			original = self.get_virtual_disk(id)
			vd=virtual_disk.virtual_disk(self.rd,original.size(),id)
			if vd.size()==0:
				return None
			else:
				vd.copy_virtual_disk(self.rd,original)
				self.check_points.append((vd,no))
				return vd
		print 'checkpoint with same id already exists'
		return None		


	def rollback(self,id,no):
		current = self.get_virtual_disk(id)

		if current==None:
			print "checkpoint not found"

		original = self.get_check_points(id,no)

		if not original==None:
			print "current", current.read(self.rd,100)
			print "original", original.read(self.rd,100)
			current.copy_virtual_disk(self.rd,original)
			print "current", current.read(self.rd,100)
			print "original", original.read(self.rd,100)
		else:
			print "checkpoint not found"

	def delete_checkpoint(self,id):
		for i in self.check_points:
			if i[0].get_id()==id:
				i[0].delete_disk(self.rd)
				self.check_points.remove(i)	

	def delete_virtual_disk(self,id):
		for i in self.v_disks:
			if i.get_id()==id:
				i.delete_disk(self.rd)
				self.v_disks.remove(i)
				self.delete_checkpoint(id)
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

	def get_check_points(self,id,no):
		count=0
		for i in self.check_points:
			if i[0].get_id()==id and i[1]==no:
				return i[0]
			count +=1
		return None



if __name__ == "__main__":
  h=hypervisor()
  h.add_phydisk(300)
  h.add_phydisk(200)
  vd1=h.create_virtual_disk(200,1)
  arr=[1,2,3]
  x=h.write(1,1,arr)
  print x
  y=h.read(1,1)
  print y
  h.checkpoint(1,1)

  arr=[1,2,4]
  x=h.write(1,1,arr)
  print x
  y=h.read(1,1)
  print y

  #h.delete_virtual_disk(1)

  h.rollback(1,1)

  y=h.read(1,100)
  print y
  


