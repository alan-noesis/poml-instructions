import utils

# context definition
context = {"item_count": 6}

# output captured
output = utils.load("kindle.poml", context)

# output copied to clipboard
utils.copy(output)
