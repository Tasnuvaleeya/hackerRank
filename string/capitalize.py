def string_title(s):
    # return s.title()
    # return ''.join(map(min, s, s.title()))
    # return "string is %s" % (s.title())
    return ' '.join([w.capitalize() for w in s.split(' ')])
print(string_title('1 w 2 r 3g'))