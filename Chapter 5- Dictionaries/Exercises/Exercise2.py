# Exercise 2: Glossary

glossary = {'variable': 'A storage unit for holding data.',
            'function': 'A code block designed to execute a particular task.',
            'loop': 'A control structure that iterates through a series of instructions.',
            'dictionary': 'An assemblage of key-value pairs for data storage.',
            'string': 'An ordered arrangement of characters.'}

# Print the glossary
for word, meaning in glossary.items():
    print(word + ":\n" + meaning + "\n")
