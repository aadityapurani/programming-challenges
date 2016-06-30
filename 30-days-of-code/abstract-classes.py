#Day 13 Abstract Class
#Coded by Aaditya Purani

from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
    
class MyBook(Book, object):
    def __init__(self,title, author, price):
        self.price = price
        super(MyBook,self).__init__(title,author)
    def display(self):
        print 'Title:', self.title
        print 'Author:', self.author
        print 'Price:', self.price
        
title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()        
