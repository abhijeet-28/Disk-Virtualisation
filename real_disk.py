import disk
import sys
class real_disk:
  total_phy=[]
  size=0
  n_disk=0
  bitmap=[]


  def add_disk(self,d_size,block_size=100):
    di=disk.disk(d_size,block_size,self.n_disk)
    self.n_disk=(self.n_disk+1)%sys.maxint
    self.size+=d_size
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
        self.total_phy.remove(x)

        return True
      else:
        return False
      
  
  
  
if __name__ == "__main__":
  rd=real_disk()
  rd.add_disk(200)
  arr=[1,2,3]

  x=rd.total_phy[0].writetodisk(10,arr)
  print x
  val=rd.total_phy[0].readfromdisk(10)
  print val
  