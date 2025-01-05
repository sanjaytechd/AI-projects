import os
import requests
import base64
from openai import AzureOpenAI
from mimetypes import guess_type
import re

client = AzureOpenAI(
  api_key = "your_api_key",  
  api_version = "your_api_key_version",
  azure_endpoint = "your_end_points"
)

def local_image_to_data_url(image_path):
    """
    Convert a local image file to a data URL.

    Parameters:
    -----------
    image_path : str
        The path to the local image file to be converted.

    Returns:
    --------
    str
        A data URL representing the image, suitable for embedding in HTML or other web contexts.
    """
    # Get mime type
    mime_type, _ = guess_type(image_path)

    if mime_type is None:
        mime_type = 'application/octet-stream'

    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(
            image_file.read()).decode('utf-8')

    return f"data:{mime_type};base64,{base64_encoded_data}"


if __name__ == "__main__":
    # Generate Token

        # Convert Image to Data URL
        data_url = local_image_to_data_url('your_image_path')

        # Send Request to Azure OpenAI
        response = client.chat.completions.create(
            model="your_model_name",
            messages=[{
                "role": "system",
                "content": "You are an AI helpful assistant."
            }, {
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": """
    Extract the text from the given image. The image contains hand written text.
    Please maintain the paragraph format as present in the image.
    Dont add any additional messages or comments.

    """
                }, {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url
                    }
                }]
            }],
            max_tokens=4000,
            temperature=0.7
        )

        # Extract and clean the result
        if response.choices:
            img_description = response.choices[0].message.content
            print(img_description)
