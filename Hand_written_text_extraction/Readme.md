**Handwritten Text Extraction from Images Using LLM**

This project aims to extract handwritten text from images. 
The images are derived from pages of PDF files that contain handwritten text. 
The images are processed using a Large Language Model (LLM) to extract the text while preserving the original formatting from the images.

**Description**

This script processes images of handwritten text and extracts the text using a Large Language Model (LLM). 
The image is encoded in base64 format and sent to the LLM for text extraction.
The extracted text is returned while maintaining the paragraph format present in the image, without adding extra comments or modifications.

**Features**

1. Converts images of handwritten text into extracted text.
2. Uses a Large Language Model (LLM) for text extraction.
3. Maintains the paragraph structure as in the original image.
4. Uses base64 encoding to send image data to the LLM for processing.
   
**Requirements**

**Libraries:**

1. requests: For making HTTP requests (if required for further integration).
2. base64: For encoding image files into base64 format.
3. openai: For integrating with a large language model for text extraction.
4. mimetypes: For detecting the MIME type of images.

**Setup the LLM API Key:**

Get an API key from OpenAI or another LLM service provider.
Ensure you have the appropriate access to interact with the LLM.
Update the Script: Modify the script to provide the correct path to the image you want to process.

