import random

# Immutable tuple with 3 values / elements
quotes = ("It's just flesh wound.", "He's not the Messiah. He's a very naughty boy!", "THIS IS AN EX-PARROT!")


# define a function to retrieve tweet
def random_python_quote():
    rand_index = random.randint(0, len(quotes)-1)
    return quotes[rand_index]


# if program is __main__ then execute the function
if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)





