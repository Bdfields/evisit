from collections import Counter

'''
   Initialize ip address counter data structure.
   A Counter is a dict subclass for counting hashable objects. It is a collection 
   where elements are stored as dictionary keys and their counts are stored as dictionary values. 
   https://docs.python.org/3/library/collections.html#collections.Counter
'''
ip_address_counter = Counter()

def request_handled(ip_address):
  ip_address_counter[ip_address] += 1
  
def top100():
  return ip_address_counter.most_common(100)

def clear():
  ip_address_counter.clear()
