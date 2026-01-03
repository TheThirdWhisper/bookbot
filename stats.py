def word_count(book_text):
    #This function will take a provided string and output an integer equal to the number of words contained in the string
    word_count = 0 #initializing word_count as an integer with value 0
    text = book_text.split() #initializing text as a list of all words in the provided string using the split method
    for word in text: #creating a for loop to step through every word in the provided string
        word_count += 1 #increase the counter +1 for every word in text
    return word_count
def character_count(book_text):
    #This function will take a provided string and ouput a dictionary of paired strings with an integer that is the count of that specific character in the provided string
    character_count = {} #initializing character_count as an empty dictionary
    character_list = [] #initalizing character_list as an empty list
    character_list = list(book_text.lower()) #creates a list of every individual character in the string and makes all letters lower case
    for char in character_list: #starting a for loop to step through every character in the list
        if char in character_count: #starting an if statement to determine if the char is already present in our dictionary
            character_count[char] +=1 #if the char already exists as a key then its integer value is increased by 1
        else:
            character_count[char] = 1 #if the char is not already a key then it gets created with an initial value of 1
    return character_count
def sort_on(items):
    return items[1]    
def character_count_sort(character_count_dict):
    #This function will sort a provided dictionary from largest to smallest number
    dict_to_sort = character_count_dict
    sorted_dict = dict(sorted(dict_to_sort.items(), key=sort_on, reverse=True))
    return sorted_dict

