#TASK - Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:
from datetime import datetime

class SMS_store:

    def __init__(self):
        self.store = [] #inicijalizacija kad god se objekat pozove - instancira

    def __str__(self):
        return ("{0}".format(self)) #konverzija u string

    def add_new_arrival(self, number, time, text): #funkcija za novi SMS dolazak
        self.store.append( ("Read: False", "From: " + number, "Recieved: " + time, "Msg: " + text) )
