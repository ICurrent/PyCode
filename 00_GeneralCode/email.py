import re


message = """
These are Emmanuel Ogunleye email addresses 
emmaleye77@gmail.com, eoogunleye169@gmail.com and ogunnuel@gmail.com"""

pattern = '[\w\d]+@[\w]+\.com'
print(re.findall(pattern, message))

choose_pwd = input("Enter your password: ")
#print(re.match(pattern, choose_pwd))
if re.match(pattern, choose_pwd):
    print("Password is Okay")
else:
    print("Choose a stong password!")