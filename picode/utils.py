import os
class BankAccount:
     # constructor or initializer
    def __init__(self, name, money):
         self.__name = name
         self.__balance = money   
         # __balance is private now, so it is only accessible inside the class
    def deposit(self, money):
         self.__balance += money
    def withdraw(self, money):
         if self.__balance > money :
             self.__balance -= money
             return money
         else:
             return "Insufficient funds"
    def checkbalance(self):
         return self.__balance

class Person:
    # constructor or initializer
    def __init__(self, name): 
        self.name = name # name is data field also commonly known as inst

    # method which returns a string
    def whoami(self):
        return "You are " + self.name

