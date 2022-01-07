from queue import Queue

My_Queue = Queue(maxsize = 3)



#is Queue empty?
print(My_Queue.empty())


#is Queue is Full?
print(My_Queue.full())


#Keeping Something inside Queue.

#First
My_Queue.put('a')
#Second
My_Queue.put('b')
#Third
My_Queue.put('c')


#Checking Quesize
print(My_Queue.qsize())


print(My_Queue.get())
print(My_Queue.get())
print(My_Queue.get())



############################################
