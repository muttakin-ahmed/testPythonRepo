## Approach ##
# The problem was not clear to me after I read the FUQs, so I am solving this problem
# based on the first of following asssumptions.
# 1. Input is a list of runners and output is the fastest n runners, in this case, n = 3
#   as there are 3 medals for a specific sport
# 2. This would be an extension of 1 but no value of n is passed (3 winners are returned)
# 3. A hashmap of atheletes, and the desired sport will be given as inputs
#    Hashmap key: a string, the name of the sport
#    Hashmap value: unsorted list of times by various atheletes
# 
# # Algorithm ##
# 1. Create an empty list
# 2. Run a loop for asked numbers of medals
# 3. Each time, get the min of athlete times and add it to the created list
# 4. Each time, remove the min value from list of times
# 5. Return the initially created list

# # Test cases # #
# [1,1,41,25,3,15,23,2], 3 -> [1, 1, 2]
# [], 3 -> []
# [2,3], 3 -> [2,3]
# [1,2,3], 3 -> [1,2,3]
# [1,2,3], 0 -> [], as there is no medal available
# [1], -1 -> []
# [1,2,4], 11 -> [1,2,4]

# Edge Cases:
# 1. Blank list: added an initinal check
# 2. List of times is smaller than the number of medals available: Added a case
#    where the input is sent back as outputs.
# 3. If the number of medals is 0, an empty list is returned.

def n_fastest_runners(runners, num_of_winners):
    if len(runners) == 0:
        return []
    if len(runners) < num_of_winners:
        return runners
    min_times = []
    for i in range(num_of_winners):
        x = min(runners)
        min_times.append(x)
        runners.remove(x)
    return min_times

print(n_fastest_runners([1, 2, 3], 11))

## Optimization ##
# Time Complexity: This code has a runtime of maximum O(kn), as the runtime of the function "min()"
# is O(n), "remove()" is O(n) and we are running this for k times, where k numbers of medals are there.
# Space Complexity: The space complexity would be O(k) as the size of the min times will depend
# on the numbers of medals available, k.
