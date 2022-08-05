#Padding and aligning strings 
#A value can be padded to a specific length.  
#Padding Character, can be space or special character 

print('{:12}'.format('PYTHON'))
#'PYTHON      ' 
print('{:>12}'.format('PYTHON') )
#'      PYTHON' 
print('{:<{}s}'.format('PYTHON',12))
#'PYTHON      ' 
print('{:*<12}'.format('PYTHON'))
#'PYTHON******' 
print('{:*^12}'.format('PYTHON'))
#'***PYTHON***' 
print('{:.15}'.format('PYTHON OBJECT ORIENTED PROGRAMMING'))
#'PYTHON OBJECT O' 

#Above, truncated 15 characters from the left side of a specified string 
print('{:.{}}'.format('PYTHON OBJECT ORIENTED',15))
#'PYTHON OBJECT O' 

#Named Placeholders 
data = {'Name':'Raghu', 'Place':'Bangalore'} 
print('{Name} {Place}'.format(**data))
#'Raghu Bangalore' 
print("I Love You")
#Datetime 
from datetime import datetime 
print('{:%Y/%m/%d.%H:%M}'.format(datetime(2018,3,26,9,57)))
#'2018/03/26.09:57' 