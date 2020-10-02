
"""
We will implement a stack and a queue in Python
Stack using a list.   Append pushes items at the top of the stack.    
Pop removes the item at the top of the list.
"""

line_at_walmart = []


print(line_)

"""
Using the deque objects from the collections library
You can find the documentation for deque objects here:
https://docs.python.org/3/library/collections.html?highlight=deque#collections.deque
Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). 

A deque a double ended queue.

"""







"""

If you don't have to implement this yourself, you can use the standard library deque
This code is from stack overfow
https://stackoverflow.com/questions/22772764/circular-queue-python/22772ow


from collections import deque

circular_queue = deque([1,2], maxlen=4)
circular_queue.append(3)
circular_queue.extend([4])

# at this point you have [1,2,3,4]
print(circular_queue.pop())  # [1,2,3] --> 4

# key step. effectively rotate the pointer
circular_queue.rotate(-1)  # negative to the left. positive to the right

# at this point you have [2,3,1]
print(circular_queue.pop())  # [2,3] --> 1
"""