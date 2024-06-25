import pytesseract
from PIL import Image

# Open image file
image = Image.open("image2.png")

# Extract text from image
text = pytesseract.image_to_string(image)

# Print extracted text
print(text)