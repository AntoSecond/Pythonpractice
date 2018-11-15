import string
lib={}
with open('TextFile2.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line=line.strip()
        line=line[3:line.index('/',4)]
        if line in lib:
            lib[line]+=1
        else:
            lib[line]=1
        line=open_file.readline()
print(lib)


#Working solution below - testing "readline" at top

" "
# list = open_file.splitlines()
# lib={}
# for item in list:
#     if item in lib:
#         lib[item] +=1
#     else:
#         lib[item] = 1
#
# print(lib)
