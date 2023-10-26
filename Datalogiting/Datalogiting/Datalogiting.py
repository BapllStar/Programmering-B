def udfordrende(k,l1,l2):

    i = 0 # Place reader at start of l1
    j = len(l2)-1 # Place reader at end og l2
    sum = l1[i] + l2[j] # Calculate sum of numbers at readers

    # While we haven't found an answer and readers still are within lists
    while sum != k and j-1 >= 0 and i+1 <= len(l1): 
        sum = l1[i] + l2[j] # Calcualte sum of numbers at readers
        if sum < k:
            # If sum is less than number, move reader1 up
            i = i + 1
        else:
            # If sum is more than number, move reader2 down
            j = j - 1

    return sum == k # Return True/False



print(udfordrende(7,[1,2,3],[2,3,4]))