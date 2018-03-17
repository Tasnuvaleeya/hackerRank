# w1 = raw_input()
# w2 = raw_input()
#
# total = 0
# for letter in "abcdefghijklmnopqrstuvwxyz":
#     sum = len(w2)+len(w1)
#     total = sum - (len([i for i in w1, w2]))
# print total
w1 = input()
w2 = input()

res = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    res +=abs(w1.count(letter)-w2.count(letter))
print(res)
