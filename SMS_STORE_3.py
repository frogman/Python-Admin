#TASK - Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:
from datetime import datetime

class sms_store:

    has_been_viewed = False
    def __init__(self):
        self.store = [] #inicijalizacija kad god se objekat pozove - instancira

    def __str__(self):
        return ("{0}".format(self)) #konverzija u string

    def add_new_arrival(self, number, time, text): #funkcija za novi SMS dolazak
        #self.store.append( "Read: False", "From: " + number, "Received: " + time, "Msg: " + text)
        self.store.append( ("From: {}, Received: {}, Msg: {}".format( number, time, text ) ))

    def message_count(self):
        return(len(self.store))

    def get_unread_indexes(self):  #moram sa has_been_viewed nekako resiti
        result = []
        for (i, v) in enumerate(self.store):
            if v[0] == "Read: False":
                result.append(i)
        return(result)

    def get_message(self,i):
        msg = self.store[i]
        msg = ("Read: True",) + msg[0:]
        self.store[i] = (msg)
        return (self.store[i][0:])

    def delete(self,i):
        del self.store[i]

    def print_all(self) -> object:
        return print(self.store)

    def clear(self):
        self.store = []

time = datetime.now().strftime('%H:%M:%S')
inbox = sms_store() #instanciranje objekta inbox od klase sms_store
#https://www.programiz.com/article/python-self-why
#u ovom slucaju in
inbox.add_new_arrival(441223324343,time,"Hello I am the first sms")
inbox.add_new_arrival(436648832123,time,"Hello I am the second sms")
#inbox.get_message(1)
inbox.print_all()
#inbox.clear()

