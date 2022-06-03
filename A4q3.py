
def create_lst():       # create list function
    lst = []            # for new list
    takeInput = int(input("Enter the size of list : "))     # taking the size of list
    for i in range(takeInput):      # iterating the list size
        takeNumber = int(input("Enter numbers : "))         # taking input from user 
        lst.append(takeNumber)      # append input into new list
    return lst      # return the list

def squareList(sq):     # function for square
    return sq **2   

lst = create_lst()      # calling create_lst() and storing in lst
resultSq = map(squareList,lst)      # using map(function, iterable)
print("Square the elements of the list : {}".format(list(resultSq)))        # print list





# Sample List: [4, 5, 2, 9]

# Square the elements of the list:    [16, 25, 4, 81]