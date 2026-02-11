import utils

# input obtained
utils.clear()
name = utils.input("Hello, what is your name? ").strip()

# context definition
context = {"name": name}

# output captured
output = utils.load("example.poml", context)

# output copied to clipboard
utils.copy(output)
