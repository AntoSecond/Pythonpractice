import string
happylist=[]
overlaplist=[]
with open('primenumbers.txt', 'r') as primenumbers:
    with open('happynumbers.txt', 'r') as happynumbers:
        happy=happynumbers.readline()
        while happy:
            happylist.append(happy)
            happy=happynumbers.readline()
        line=primenumbers.readline()
        while line:
            if line in happylist:
                overlaplist.append(line)
            line=primenumbers.readline()
with open('overlap.txt', 'w') as overlap:
    for items in overlaplist:
        overlap.writelines(items)



#       while line:
#             print(line)
#             if line in happy:
#                 print(line)
#                 Items.add(line)
#             line=primenumbers.readline
#             print("end")
# print(Items)

