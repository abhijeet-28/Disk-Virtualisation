import disk
import sys
class real_disk:
  total_phy=[]
  size=0
  n_disk=0
  bitmap=[]
  free_mem=0

  def add_disk(self,d_size,block_size=100):
    di=disk.disk(d_size,self.n_disk,block_size)
    self.n_disk=(self.n_disk+1)%sys.maxint
    self.size+=d_size
    self.free_mem+=d_size
    self.total_phy.append(di)
    arr=[False]*d_size
    self.bitmap=self.bitmap+arr


  def del_disk(self,id):
    start=0
    for x in self.total_phy:
      start+=x.size()
      if x.get_id()==id:
        self.bitmap[start-x.size():start]=[]
        self.size -= x.size()
        self.free_mem-=x.size()
        self.total_phy.remove(x)

        return True
      else:
        return False
      
  def write(self,Block_no, info):
    count=0
    for i in self.total_phy:
      count+=i.size()
      if(Block_no<count):
        return i.writetodisk(-count+i.size()+Block_no,info)
    return False

  def read(self,Block_no):
    count=0
    for i in self.total_phy:
      count+=i.size()
      if(Block_no<count):
        return i.readfromdisk(-count+i.size()+Block_no)
    return None

      

  
  
if __name__ == "__main__":
  rd=real_disk()
  rd.add_disk(200)
  arr=[1,2,3]
  arr1=[1,3,5]
  x=rd.total_phy[0].writetodisk(10,arr)
  print x
  y=rd.total_phy[0]
  print y.d_size
  print y.id
  rd.del_disk(0)
  rd.add_disk(300)
  x=rd.total_phy[0].writetodisk(10,arr1)


  val=rd.total_phy[0].readfromdisk(10)
  print val
  