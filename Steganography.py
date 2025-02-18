import cv2  # Import OpenCV library
import os   # Import OS module for opening the image

# Read the image (Make sure the image is in the same directory or provide the full path)
img = cv2.imread("1.jpg")
# Get user inputs
msg = input("Enter the secret message: ")
password = input("Set a passcode: ")

# Create two dictionaries for character-to-number and number-to-character mapping
d = {chr(i): i for i in range(256)}  # Maps characters to numbers
c = {i: chr(i) for i in range(256)}  # Maps numbers back to characters

# Variables to track pixel positions
n, m, z = 0, 0, 0

# Encoding message into the image
for char in msg:
    img[n, m, z] = d[char]  # Store ASCII value of the character in the pixel
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through RGB channels

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
print("Message encrypted successfully!")
# Open the encrypted image
os.system("start encryptedImage.jpg")  # Use 'start' for Windows, 'open' for MacOS

# Decryption process
decrypted_message = ""
n, m, z = 0, 0, 0
# Ask for passcode
pas = input("Enter passcode for decryption: ")

if pas == password:
    # Extract the message from the image
    for _ in range(len(msg)):  
        decrypted_message += c[img[n, m, z]]  # Convert pixel value back to character
        n += 1
        m += 1
        z = (z + 1) % 3  

    print("Decrypted message:", decrypted_message)
else:
    print("YOU ARE NOT AUTHORIZED!")
