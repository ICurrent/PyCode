subject = input("enter your subject ")
f = open("{}.txt".format(subject),"r")
print(f.readline())
f.close()
f = open("option.txt","r")

for line in f:
    print(line, end ='')
f.close()

