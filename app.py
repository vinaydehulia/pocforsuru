from flask import Flask, request, jsonify
import json
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import google.cloud.logging
import logging

app = Flask(__name__)


@app.route('/api/data', methods=['POST'])
def receive_data():
    # Get JSON data from the request
    data = request.get_json()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Log a message with the current time
    logging.info(f'[{current_time}] Hello, Docker! endpoint was accessed.')
    logging.info(f'json data recived [{data}] at [{current_time}]')

    # Check if data is present
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # Call the json to video


#==========================
    # Video Settings
    width, height = 800, 600
    fps = 30
    output_file = "/usr/local/output_video.mp4"
    
    logging.info(f'setupu output file path [{output_file}]')
    
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
    for frame in data["frames"]:
        num_frames = int(frame["duration"] * fps)
        for _ in range(num_frames):
            img_frame = create_frame(frame["text"])
            video.write(cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR))

    # Release Video
    video.release()
    logging.warning(f'✅ Video saved as [{output_file}]')


#===========================


    # Process the data (example: echo back the received data)
    response = {
        "message": "Data received successfully-1",
        "received_data": data
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)