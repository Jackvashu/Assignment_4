def create_lst():       # create list function
    lst = []            # for new list
    takeInput = int(input("Enter the size of list : "))     # taking the size of list
    for i in range(takeInput):      # iterating the list size
        takeNumber = int(input("Enter numbers : "))         # taking input from user 
        lst.append(takeNumber)      # append input into new list
    return lst      # return the list

def triple_numbers(times):      # function for tripling the number
    return times*3
lst = create_lst()      # calling create_lst() and storing in lst

result = map(triple_numbers,lst)        # using map(function, iterable)
print("Triple of list numbers: {}".format(list(result)))         # print list  result

    
# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]