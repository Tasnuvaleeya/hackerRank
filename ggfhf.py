def simple_prob(n):
    if n % 2 != 0 or (n%2 == 0 and n in range(6,21)):
        return 'Weird'
    # elif n % 2 == 0 and n in range(2, 5) or(n %2 == 0 and n > 20):
        # return 'Not Weird'
    else:
        return 'Not Weird'

print(simple_prob(20))
