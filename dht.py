import hashlib
class Node:
    def __init__(self,ipaddress,_type):
        self.type=_type
        self.ipaddress = ipaddress
        self.id=self.generate_id(ipaddress)
        self.successor=None
        self.predecessor=None
        self.finger_table=[]
        self.hash_table={}
    
    def generate_id(self,ipaddress):
        # create a hash using sha1 algo
        hashobj=hashlib.sha1(ipaddress.encode())
        return int(hashobj.hexdigest(),16)%(2**160)
    
    def join(self,node,_type):
        if _type=='initial':
            self.predecessor=self.id
            i=0
            while(i<160):
                start=(self.id+2**i)%2**160
                self.finger_table.append(fingure(start,self.id))
                i+=1
            return
        