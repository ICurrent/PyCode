import sys
import os
class_work = open("sunday.txt", "wb")
print(class_work.mode)
print(class_work.name)

class_work.write(bytes("who is the gov of lagos state\n(a).buhari  (b). oshibajo (c). sanwo-olu(d). tinubu", 'UTF-8'))

class_work.close()

#class_work = open("test.txt", "r+")



#content_of_my_file = class_work.read()
#print(content_of_my_file)
