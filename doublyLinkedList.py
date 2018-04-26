'''
Program         : Doubly Linked list Class
Author(s)       : 1. Smrity Chaudhary
                  2. Vipin Kumar
'''

# Import necessary libraries.
from os import listdir
from os.path import isfile,join

# -----------------------------------------------------------------------------
# Class Definition
class Node:
    '''
    Node: Node class.
    '''

    def __init__(self,data):
        '''
        Objective: To initialize data members of object Node
        Input Parameters:
            self (implicit parameter) - object of type Node
            data - int
        Return Value: None
        '''
        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
    '''
    DoublyLinkedList Class Implementation.
    '''
    def __init__(self):
        '''
        Objective: To initialize data members of object DoublyLinkedList
        Input Parameters:
            self (implicit parameter) - object of type MyDate
        Return Value: None
        '''
        self.head = None


    def insert(self,newData):
        '''
        Objective: To insert data at end into doubly linked list.
        Input Parameters:
            self (implicit parameter) - object of type MyDate
            newData - string type, path for song.
        Return Value: None
        '''
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
            return

        temp = self.head

        while(temp.next is not self.head):
            temp = temp.next

        newNode.prev = temp
        temp.next = newNode
        self.head.prev = newNode
        newNode.next = self.head


    def display(self):
        '''
        Objective: To display the contents of linked list.
        Input Parameters:
            self (implicit parameter) - object of type MyDate
        Return Value: None
        '''
        temp = self.head
        while(temp is not self.head.prev):
            print(temp.data," ")
            temp = temp.next
        print(self.head.prev.data)


    def getNext(self):
        '''
        Objective: Get next value from linked list.
        Input Parameters:
            self (implicit parameter) - object of type MyDate
        Return Value: Value of head.next.
        '''
        self.head = self.head.next
        return self.head.data


    def getPrev(self):
        '''
        Objective: Get previous value from linked list.
        Input Parameters:
            self (implicit parameter) - object of type MyDate
        Return Value: Value of head.prev.
        '''
        self.head = self.head.prev
        return self.head.data


    def getFileName(self,path):
        files = [f for f in listdir(path) if isfile(join(path,f))]
        mp3Files = []
        for i in files:
            if '.mp3' in i:
                mp3Files.append(i)
        return mp3Files
