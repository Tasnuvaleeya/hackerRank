class Solution:
    pass
    # Write your code here
#     def isPalindrome(self,s):
#         # reversed_string=""
#         # for i in s:
#         #     reversed_string = i+ reversed_string
#         # return reversed_string
#         if s==s[::-1]:
#             print('True')
#         else:
#             print('False')
#
# print()


def isPalindrome(s):
    # reversed_string=""
    # for i in s:
    #     reversed_string = i+ reversed_string
    # return reversed_string
    if s == s[::-1]:
        print('True')
    else:
        print('False')
print(isPalindrome('abac'))