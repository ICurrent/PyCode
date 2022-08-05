# Converting text to bytes
# Converting a strings to byte object is termed as encoding
'''# Converting a strings to byte object is termed as encoding.
There are numerous forms of encoding, most common ones are: PNG; JPEG, MP3, WAV, ASCII, UTF-8 etc. 
Also this(encoding) is a format to represent audio, images, text, etc. in bytes. '''

 # Python Code to demonstrate string encoding 
  
 # Initialising a String 
x = 'TutorialsPoint' 
  
 #Initialising a byte object 
y = b'TutorialsPoint' 
 # Using encode() to encode the String 
 # encoded version of x is stored in z using ASCII mapping 
z = x.encode('ASCII') 
  
 # Check if x is converted to bytes or not 
  
if(z==y): 
    print('Encoding Successful!') 
else: 
    print('Encoding Unsuccessful!') 
 
print(z)