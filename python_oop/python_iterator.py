list1=[1,2,3,4,5,6,7,8,9,10]
my_iter=iter(list1)
print(my_iter) #<list_iterator object at 0x000001BCC4FB5C90>
print(next(my_iter)) #1 
print(next(my_iter)) #2
print(next(my_iter)) #3
print(next(my_iter)) #4
print('\n')

# iterable is an object that contains a countable number of values
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# iteratable: Lists, tuples, dictionaries, and sets are all iterable objects. 
# iterator:  They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:


'''
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

The __iter__() method acts similar to __init__(), you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.

to prevent the iteration from going on forever, we can use "StopIteration" statement

'''

class my_num:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):

        if(self.a<=20):
          x=self.a
          self.a+=1
          return x
        else:
           raise StopIteration # this statement will stop the iteration

my_class=my_num()
my_iter=iter(my_class)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
