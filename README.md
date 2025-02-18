# Image-steganography-using-python
This project demonstrates image steganography using OpenCV, allowing users to hide secret messages inside an image and retrieve them later with a passcode. It modifies pixel values to encode text, making it an easy-to-use technique for basic data hiding.

# Features
1. Hide a secret message inside an image.
2. Decrypt the hidden message using the correct passcode
3. Uses OpenCV for image processing
4. ASCII-based encoding to store characters in pixel values
5. Simple and lightweight Python implementation

# Requirements
* Python 3.x
* OpenCV (pip install opencv-python)

#  Usage
1. Run the script and enter a message & passcode :
*     python steganography.py
2. The script will save an encrypted image (encryptedImage.jpg)
3. To decrypt, re-run the script and enter the correct passcode

#  How It Works
* Each character of the message is converted to its ASCII value and stored in the RGB pixel values of the image.
* The decryption process extracts these values and reconstructs the original message.
* A passcode is required to access the hidden message, providing basic security.

# Limitations
* This implementation does not use advanced encryption or compression techniques.
* The length of the message is limited by the image size.
