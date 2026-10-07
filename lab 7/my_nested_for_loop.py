# Taking your solution from problem 2 above, design and write a python program named my_nested_for_loop.py
# that uses a nested for-loop over the same list and print the values in the nested for-loop to see how this behaves.

words = ["Apples", "Bananas", "Pears", "Carrots"]

for word in words:
    print(word)

    for char in word:
        print(char)