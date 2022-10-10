import pywhatkit as kit
from PIL import Image

writing = input("Enter your text to convert in Handwriting: ")

kit.text_to_handwriting(writing, save_to ='Current.png')

Image.open("Current.png")