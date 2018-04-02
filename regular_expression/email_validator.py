import email.utils
print(email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
print(email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))
