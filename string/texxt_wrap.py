import textwrap

def wrap(string,max_width):
    # return textwrap.fill(string,max_width)
    return textwrap.wrap(string,max_width)
print(wrap('this is a very very very very long sentence',8))