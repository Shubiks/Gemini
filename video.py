import os
import google.generativeai as genai
from IPython.display import Markdown
from IPython.display import display
import PIL.Image
import time

os.environ['GOOGLE_API_KEY'] = "AIzaSyAjjEePyBGEcjCUsj5bfhGCl0BNBWF2j2Y"  # input your key here
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
vision_model = genai.GenerativeModel('gemini-pro-vision')

def analyze_image():
    image_path = 'frames/frame.png'
    if not os.path.exists(image_path):
        print(f"Image file {image_path} does not exist.")
        return "Image file not found."

    try:
        image = PIL.Image.open(image_path)
        image.verify()  # Verify the image is intact
        image = PIL.Image.open(image_path)  # Reopen after verify to work with image
        image = image.resize((640, 480))  # Resize image to 640x480 or any appropriate size

        if image.mode == 'RGBA':
            image = image.convert('RGB')

        response = vision_model.generate_content(
            ["Please output 2 sentences about what you see in this video frame.", image]
        )
        return response.text
    except Exception as e:
        print(f"Error processing image: {e}")
        return "Error processing image"

def main():
    while True:
        # analyze posture
        print("👀 Gemini is watching...")
        analysis = analyze_image()
        print("🎙️ Gemini says:")
        print(analysis)

        # wait for 5 seconds
        time.sleep(5)

if __name__ == "__main__":
    main()
