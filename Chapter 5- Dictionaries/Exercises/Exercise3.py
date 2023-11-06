# Exercise 3: Glossary 2

glossary = {'variable': 'A storage unit for holding data.',
            'function': 'A code block designed to execute a particular task.',
            'loop': 'A control structure that iterates through a series of instructions.',
            'dictionary': 'An assemblage of key-value pairs for data storage.',
            'string': 'An ordered arrangement of characters.'}

# Add five more Python terms to the glossary
glossary['list'] = 'An ordered collection of items.'
glossary['module'] = 'A file that contains reusable Python code.'
glossary['tuple'] = 'An ordered list of things that are immutable.'
glossary['boolean'] = 'A basic data type with only two choices: True or False.'
glossary['conditional statement'] = 'A command that tells the program what to do based on a specific condition.'

# Print the glossary using a loop
for word, meaning in glossary.items():
    print(word + ":\n" + meaning + "\n")
