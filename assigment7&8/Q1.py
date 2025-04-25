class node:
    def __init__(self,data,next):
        self.data=data
        self.next=None


class linkedlist:
    def __init__(self):
      self.head=None

    def createnode(self,data):
       new_node=node(data)
       if self.head is None:
          self.head=new_node
       return  #exiting method
        
    