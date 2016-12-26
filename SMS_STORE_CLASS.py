class SMS_Store:
    has_been_viewed = False
    inboxList = []
    indexList = []

    # def __init__(self):

    def Add(self, number, Time, text):
        self.add = (number, Time, text, self.has_been_viewed)
        self.inboxList.append( self.add )
        return self.inboxList

    def message_count(self):
        return len( self.inboxList )

    def get_unread_indexes(self):

        for i in range( 0, len( self.inboxList ) ):
            if self.inboxList[i][3] == False:
                self.indexList.append( i )

                # else:
                #   continue

        return self.indexList

    def get_message(self, i):

        for j in self.inboxList:
            if self.inboxList[i] == j:
                j = list( j )
                j[3] = True
                self.inboxList[i] = tuple( j )
                print( j )
                if j[3] == True:
                    return "Message Viewed" + "\nFrom:" + str( j[0] ) + "\n Time:" + str( j[1] ) + "\n Text: \t" + str(
                        j[2] )
            elif i > len( self.inboxList ) or i < 0:
                return None

    def delete(self):
        del self.inboxList[i]

    def clear(self):
        del self.inboxList[::]


my_inbox = SMS_Store( )
my_inbox.Add( "0793109102", "2:00", "hello world" )
my_inbox.Add( "0793109102", "12:19", "sya striker ksasa" )
my_inbox.Add( "0793109102", "13:05", "set up ndoda" )
print( my_inbox.get_message( 0 ) )
print( my_inbox.get_message( 1 ) )
# print(my_inbox.get_message(2))
print( my_inbox.get_unread_indexes( ) )
print( my_inbox.message_count( ) )