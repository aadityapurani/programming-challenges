#Programmed by Aaditya Purani

def getHeight(self,root):
    if root is None:
        return -1
    else:
        return  max(1+self.getHeight(root.left),1+self.getHeight(root.right))
