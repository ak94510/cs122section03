# ----------------------------------------------------------------------
# Name:        hw5_functions
# Purpose:     Lambda Expression, Decorator, and Generator Practices
#
# Date:       2/24/2019
# ----------------------------------------------------------------------
"""
Lambda Expression, Decorator, and Generator Practices

Contains 5 functions
- most_e: finds a string with the most occurrences of the letter 'e'
-top_midterm: finds the top n students with the highest midterm grade
-shout: (decorator) converts the return value to uppercase
        and add '!!!' at the end
-repeat_character: (generator) repeats each character in a string n times
-alpha_labels: (infinite generator) generates increasing alphabet labels
"""

def most_e(*strings):
    """
    Find a string with the most occurrences of the letter 'e'
    :param strings: (tuple) arbitrary number of strings
    :return: string with the most occurrences of the letter 'e'
    """
    return max(strings, key = lambda str: str.lower().count('e')) \
           if strings else None

def top_midterm(grades, n = 4):
    """
    Find the top n students with the highest midterm grade
    :param grades: (dictionary) student names and lists of grades
    :param n: (integer) the number of top students to select
    :return: list containing the names of the top n students
    """
    return sorted(grades, key = lambda name: grades[name][2],
                  reverse = True)[:n]

def shout(function):
    """
    Decorator that convert the return value to uppercase
    and add !!! at the end.
    :param function: (function)
    :return: (string)
    """
    def wrapper(*args):
        return function(*args).upper() + '!!!'
    return wrapper

@shout
def greet(name):
    """
    Return a personalized hello message.
    :param name: (string)
    :return: (string)
    """
    return f'Hello {name}'

@shout
def repeat(phrase, n):
    """
    Repeat the specified string n times
    with a space character in between.
    :param phrase: (string)
    :param n: (integer) number of times the phrase will be repeated
    :return: (string)
    """
    words = phrase.split()
    return ' '.join(n * words)

def repeat_character(str, n):
    """
    Generator that repeats each character in a string n times
    :param str: (string) sequence of characters
    :param n: (integer) number of characters to repeat
    :return: yield each character n times
    """
    for ch in str:
        yield ch * n

def alpha_labels(str = 'A'):
    """
    Infinite generator that generates labels alphabetically,
    starting with the starting label - then increasing the length
    after reaching Z.
    :param str: (string) string representing the starting label
    :return: yield each alphabet in increasing length
    """
    import string
    n = len(str)
    label = string.ascii_uppercase
    yield from (repeat_character(label[label.index(str[0]):], n))
    while True:
        n += 1
        yield from(repeat_character(label, n))

def main():
    # most_e function test
    print(most_e())
    print(most_e('Go', 'Spartans', 'Take', 'Selfies', 'eat', 'APPLES'))
    print(most_e('Go', 'Spartans', 'APPLES'))
    print(most_e('Go', 'Spartans', 'Eat'))
    print(most_e('Go', 'Spartans', 'Take', 'Selfies', 'degree'))
    print(most_e('Spartans'), '\n')

    # top_midterm function test
    empty_class = {}
    cs122 = {'Zoe':[90, 100, 75], 'Alex':[86, 90, 96],
             'Dan':[90, 60, 70], 'Anna':[60, 80, 100],
             'Ryan':[100, 95, 80], 'Bella':[79, 70, 99]}
    print(top_midterm(cs122, 2))
    print(top_midterm(cs122))
    print(top_midterm(cs122, 10))
    print(top_midterm(empty_class, 6))
    print(cs122, '\n')

    # shout function test
    print(greet('Rula'))
    print(repeat('Python is fun!', 3))
    print(repeat('Go Spartans!', 5), '\n')

    # repeat_character function test
    # Uncomment below for test
    """ 
    vocabulary = repeat_character('ACGT', 3)
    print(next(vocabulary))
    print(next(vocabulary))
    print(next(vocabulary))
    print(next(vocabulary))
    print(next(vocabulary))
    """
    import string
    labels = repeat_character(string.ascii_uppercase, 2)
    for each_label in labels:
        print(each_label)

    # alpha_labels function test
    # Uncomment below for test
    """
    print()
    labels = alpha_labels('XX')
    for each_label in labels:
        print(each_label)
    """

if __name__ == '__main__':
    main()
