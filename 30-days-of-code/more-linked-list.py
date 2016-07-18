#Programmed by Aaditya Purani
#Day24
    def removeDuplicates(self,head):
        #Write your code here
        if not head:
            return head
        
        current_node = head
        prev_node = None
        while current_node:
            if prev_node and current_node.data == prev_node.data:
                prev_node.next = current_node.next
                current_node = prev_node
            #prev_data = current_node.data
            prev_node = current_node
            current_node = current_node.next
        return head    
  
  
  
  
  
  
