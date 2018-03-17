def mutation_string(string,position,character):
    """
# string='abcd'
# string = 'abracadabra'
# string= string[:5] +"k"+string[6:]
# print(string)
#     return string[:position]+character+string[position+1:]

    """

    l=list(string)
    l[5]='k'
    return ''.join(l)
print(mutation_string('abracadabra',5,'k'))