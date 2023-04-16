import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
# Load the image
image_path = "image2.jpeg"  # Replace with the path to your image file
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to extract text from the image
text = pytesseract.image_to_string(gray_image)

# Save the extracted text to a text file
text_file_path = "output2.txt"  # Replace with the desired path for the output text file
with open(text_file_path, "w") as f:
    f.write(text)

print("Text extracted from the image and saved to:", text_file_path)
