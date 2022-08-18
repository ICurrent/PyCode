import base64
import os
import time
import sys

pw = "password"
encode = base64.b64encode(pw)

def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    pw = str(raw_input("Enter your password for the Lock or Unlock your folder: "))
    if pw == base64.b64decode(encode):
        os.chdir("C:\Users\Current\Desktop\you")
        print("Your path Successfully changed")
        if not os.path.exists("Locker"):
            if not os.path.exists("Locker.{645ff040-5081-101b-9f08 00aa002f954e}"):
                os.mkdir("Locker")
                print("Locker Folder Successfully created")
            else:
                os.popen('attrib -h Locker.{645ff040-5081-101b-9f08 00aa002f954e}')
                os.rename("Locker.{645ff040-5081-101b-9f08 00aa002f954e}","Locker")
                print("Locker Folder has been Successfully Unlocked")
                sys.exit()

        else:
            os.rename("Locker", "Locker.{645ff040-5081-101b-9f08 00aa002f954e}")
            os.popen('attrib +h Locker.{645ff040-5081-101b-9f08 00aa002f954e}')
            print("Locker folder has been successfully locked")
            sys.exit()

    else:
        print("Wrong ppassword! Pkease Enter right password")
        time.sleep(3)
        goto()