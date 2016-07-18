#Programmed by Aaditya Purani
#Day 23 HackerRank

    def levelOrder(self,root):
  	     #Write your code here
        queue  = []
        queue.append(root)
        while queue:
            next_node = queue.pop(0)
            print next_node.data,
            if next_node.left:
                queue.append(next_node.left)
            if next_node.right:
                queue.append(next_node.right)
