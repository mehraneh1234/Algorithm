#Mehraneh 30062786
# AT3   01/03/2023
# Create a Linear Search method for a Tuple

#Declare a funtion to search an item in a tuple then return an index of the found item
def SearchTuple(searchTerm, tupOS):
    # for loop to read each item of a string
    for i in tupOS:
        # condition to find the item in the tuple
        if searchTerm == i:
            # return the index of the found item to where it called the function
            return tupOS.index(i);

# define a tuple with its values
tupOS = ("Windows 10", "Linux Mint", "Mac OS 11", "Android Oreo", "Android Pie",
         "Android 11", "iOS 14",)
# Display the type and values of the tuple
print("Type of the data structure is: ", type(tupOS), "\nThe Os names are:", tupOS)        
# define a variable to put the key board value int it.
searchTerm = input("Which OS name do you search? ")

# call the function with its arguments. One of them a tuple the other one is an item we
# need to find. then the result assign to a variable
index = SearchTuple(searchTerm, tupOS)
# condition to found the item in a list or not and display the outputs
if index == None:
    #Disply nothing found
    print(searchTerm, "doesn't found in the Tuple!")
else:
    # Display found the item in which index
    print(searchTerm, " found at ", index, " index.")
