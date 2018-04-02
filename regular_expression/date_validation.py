import re
date_validator = r'\d\d\.[\d\d\]{11}.\d\d\d\d'

if re.match(date_validator, '15.02.2019'):
    print('True')
else:
    print('False')
