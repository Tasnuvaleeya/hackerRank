import xml.etree.ElementTree as etree

N=int(input())
for _ in range(N):
    s=input()
    tree = etree.ElementTree(etree.fromstring(s))
    print(tree)
    print(len(tree))