# Algorithm
# 1. We'll have two varuables for checking whether we have seen a char before
#   a. one (str) for traversing and storing the unique chars
#   b. a list for storing the duplicate onces
# 2. Start traversing the given sting
# 3. If the current char is not in unique chars, this char is added
# 4. Else, this char has been seen before, so that we add this the list of 
#   duplicate chars
# 5. Finallty return the list of duplicate chars.

# Input: "aabbssd" -> Output: [a,b,s]
# Input: "12124" -> Output: [1,2]
# Input: "" -> Output: []


def find_duplicate_chars(string):
    e = ""
    duplicate_chars = []
    for ch in string:
        if ch not in e:
            e += ch
        else:
            duplicate_chars.append(ch)
    return duplicate_chars

print(find_duplicate_chars(""))

### Optimization ###
## Time Complexity: O(n), as the code is traversing the given string once
## Space Complexity: O(n), as the code is creating two variables max of n space.
## Alternate Data Structure: This problem could have been solved using a hashmap
##  as well. In that case, time complexity would have been O(n), but time 
#   consumption would have been less than what we had here.