from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    arr = []

    for i in range(size):
      new_linked_list = LinkedList()
      arr.append(new_linked_list)
    return arr



  # Creates my own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    first_letter = key[0].lower()

    d_from_origin = ord(first_letter) - ord('b')

    index = d_from_origin % self.size

    return index


  # the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    # we're going to find the index for where our key value pair are placed
    key_hash = self.hash_func(key)
    new_tuple = (key, value)

    

   
    if self.arr[key_hash].find(new_tuple) == -1:
      self.arr[key_hash].append(new_tuple)
      
    elif self.arr[key_hash].find(new_tuple) == True:
      self.arr[key_hash]
    


  # the print_key_values method.

  # Traverses through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    
    
    if self.size == None:
      print("empty")
      return -1
    else:
      for i in self.arr:
        
        i.print_nodes()
        
    

    



