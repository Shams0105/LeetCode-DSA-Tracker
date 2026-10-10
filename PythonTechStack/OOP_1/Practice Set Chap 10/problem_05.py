# Write a class train which has methods to book a ticket , get status(no of seats) & get fare
# info of train running under Indian Railways

#import random no for fare generation

from random import randint
class train:

    def __init__(self,trainNo):
        self.trainNo = trainNo #Since all wil have same trainNo use __instance attr for the same
        #No need of passing trainNo attr in each method --> Directly use self.trainNo

    def bookTicket(self, fro , to):
        print(f"Ticket booked for train number {self.trainNo} \n travelling from {fro} to {to}")


    def getStatus(self):
        print(f"Train number {self.trainNo} \n Is ON TIME !!")


    def getFareInfo(self , fro , to):
        print(f"Ticket fare for train number {self.trainNo} \n travelling from {fro} to {to} is \n {randint(222,5555)}")

t = train(12399)

t.bookTicket( "Mumbai" , 'Delhi')
t.getStatus()
t.getFareInfo("Mumbai" , "Delhi")
