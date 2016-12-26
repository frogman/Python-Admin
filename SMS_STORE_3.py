#TASK - Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:
from datetime import datetime

class sms_store:

    def __init__(self):
        self.store = [] #inicijalizacija kad god se objekat pozove - instancira

    def __str__(self):
        return ("{0}".format(self)) #konverzija u string

    def add_new_arrival(self, number, time, text): #funkcija za novi SMS dolazak
        self.store.append( (str("Read: False"), "From: " + number, "Received: " + time, "Msg: " + text) )

    def message_count(self):
        return(len(self.store))

    def get_unread_indexes(self):
        result = []
        for (i, v) in enumerate(self.store): #listanje za svaki element u store listi i dodavanja indeksa 1,2,3 u vidu v varijable da bi se mogla kasnije
            if v[0] == "Read: False":        #raditi operacija sa v objektom-varijablom
                result.append(i)
        return(result)

    def get_message(self,i):
        msg = self.store[i]
        msg = ("Read: True",) + msg[1:]
        self.store[i] = (msg)
        return (self.store[i][1:])

    def delete(self,i):
        del self.store[i]

    def print_all(self):
        print(sms_store.store)

    def clear(self):
        self.store = []

time = datetime.now().strftime('%H:%M:%S')
inbox = sms_store() #instanciranje objekta inbox od klase sms_store
sms_store.add_new_arrival(inbox,44,time,"Hello I am the first sms")

