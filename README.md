## What would you do differently if you had more time? 

1. I would create a singleton class that encapsulates the 3 methods. The advantage of this would be that it would allow for multiple servers to be able to access the same tracker instance.
2. More exception handling to ensure the ip_addresses are formatted correctly.
3. Think about a more custom data structure to improve performance.

## What is the runtime complexity of each function?
- `request_handled` would be O(1) since we are using a hash map to store the counts
- `top100` would be O(nlgn) to sort the data.
- `clear` would be O(1)
    
 ## How does your code work?
 The code uses python's `collections.Counter` data structure to store the data into a hash map like data structure.
 `collections.Counter` has an instance method, `most_common`, that we use to return the top 100 ip addresses.
 Finally, we use collections.Counter `clear` method to reset the data structure.

## What other approaches did you decide not to pursue? 
- Creating my own custom data structure and algorithm. I could have put more thought into keeping the hash map sorted. This could have possibly saved us from having  the `top100` method having to sort the entire sturcture first.
    
## How would you test this?
 - Unit Tests for each method to make sure it behaves as intended, i.e. gracefully handle bad input, produces correct output
 - Stress test the methods this a large number (10 Million+) ip addresses
