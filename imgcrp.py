
# Import required modules
from PIL import Image
import numpy as np
  
def cmode(img):
    
    image = Image.open(img)# Load image    
    image_arr = np.array(image)# Convert image to array
    image_arr = image_arr[2070:2180, 390:690] # Crop image
    image = Image.fromarray(image_arr)    # Convert array to image
    #image.show()  # Display image
    return image

def buttonstat(img):  
    image = Image.open(img) # Load image 
    image_arr = np.array(image) # Convert image to array
    image_arr = image_arr[1770:2000, 420:655] # Crop image
    image = Image.fromarray(image_arr)  # Convert array to image
    #image.show() # Display image
    return image

def prnttym(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)