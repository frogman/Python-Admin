#http://stackoverflow.com/questions/16240858/python-sms-store-program-using-class-and-methods-has-been-viewed-status
from datetime import datetime

class sms_store:
    store = []
    read = []
def add_new_arrival(self,number,time,text):
    sms_store.read.append(len(sms_store.store))
    sms_store.store.append(("From: {}, Recieved: {}, Msg: {}".format(number,time,text)))
def delete(self,i):
    try:
        del sms_store.store[i]
    except IndexError:
        print("Index is out of range. Cannot delete")
def message_count(self):
    return print("Amt of messages in inbox: {}".format(len(sms_store.store)))
def viewall(self):
    print(sms_store.store)

def get_message(self,i):
    print(sms_store.store[i])

### tests ####
time = datetime.now().strftime('%H:%M:%S')
my_inbox = sms_store() #instantiate an object 'store' for class
my_inbox.add_new_arrival("12345",time,"Hello how are you?") #instance of store object
my_inbox.add_new_arrival("1111111",time,"BYE BYE BYE")
my_inbox.viewall()
my_inbox.msgcount()