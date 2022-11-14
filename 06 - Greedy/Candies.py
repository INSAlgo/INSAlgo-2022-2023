def candies(n, arr):
    #create three array with 0 inside
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    ourCandies = [0 for i in range(n)]
    
    # start with the left side and go to the right
    p = 1
    while p<n:
        if arr[p] > arr[p-1]: #if the right one is superior
            left[p] = left[p-1] + 1 # the right get one more than the left
        p += 1
         
    # start from the right side and go to the left
    p = n-2
    while p>=0:
        if arr[p] > arr[p+1]: #if the left one is superior
            right[p] = right[p+1] + 1 # the left get one more than the right
        p -= 1
    
    #now compare both of them
    p = 0
    while p<n:
        ourCandies[p] = 1 + max(left[p], right[p])
        p += 1
     
    return(sum(ourCandies))
