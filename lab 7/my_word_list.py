#Design and write a python program name my_word_list.py . 
#You should implement a user-defined function name printWordList() that does not take any arguments.
# The function should create a new local variable named word and you should assign
#the following list to the word variable: ["Apples","Bannas","Pears","Carrots"].
#Your function should in-turn use a for-loop and loop over the list printing each value in the list.

def printMyWordList():

    variable = ["Apples", "Bannas", "Pears", "Carrots"]

    for variable in variable:

        print(variable)

    
printMyWordList()