import json
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def process_data(data):
    """
    Example function to process the received JSON data.
    You can replace this with your own logic.
    """
json_data = data 
# Video Settings
width, height = 800, 600
fps = 30
output_file = "output_video.mp4"

# Choose a font (change the path if needed)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Linux/Mac
# font_path = "C:\\Windows\\Fonts\\arial.ttf"  # Windows Example

# Create Video Writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change to 'H264' if needed
video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Function to Create a Frame
def create_frame(text):
    img = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, 40)
    except IOError:
        font = ImageFont.load_default()

    # Get text dimensions using textbbox()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Center the text
    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, text, font=font, fill="white")

    return np.array(img)

# Generate Frames
for frame in json_data["frames"]:
    num_frames = int(frame["duration"] * fps)
    for _ in range(num_frames):
        img_frame = create_frame(frame["text"])
        video.write(cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR))

# Release Video
video.release()
print(f"✅ Video saved as {output_file}")

