lst = [1, 2, 3, 4, 5, 3, 2, 4, 6, 7, 8, 5]
print("original list is",lst)
newlist = []
for i in lst:
    if i not in newlist:
        newlist.append(i)

print("new list is",newlist)

