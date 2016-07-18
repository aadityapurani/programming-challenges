#Programmed by Aaditya Purani
#Day 18 Hackerrank

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, char):
        self.stack.append(char)
    
    def popCharacter(self):
        return self.stack.pop()
    
    def enqueueCharacter(self, char):
        self.queue.append(char)
    
    def dequeueCharacter(self):
        return self.queue.pop(0)
