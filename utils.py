import cv2
import numpy as np
import os

def generate_video_from_image_and_prompt(image_path, prompt, output_path):
    '''
    Simplified video generation based on image and prompt.
    This demo creates a zoom-in video effect on the uploaded image.
    '''

    try:
        img = cv2.imread(image_path)
        if img is None:
            print("Failed to read image")
            return False

        height, width, _ = img.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 24
        duration = 3  # seconds
        total_frames = fps * duration
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        for i in range(total_frames):
            scale = 1 + 0.1 * (i / total_frames)  # zoom from 1 to 1.1
            center_x, center_y = width // 2, height // 2
            new_w, new_h = int(width / scale), int(height / scale)
            x1 = max(center_x - new_w // 2, 0)
            y1 = max(center_y - new_h // 2, 0)
            x2 = x1 + new_w
            y2 = y1 + new_h
            cropped = img[y1:y2, x1:x2]
            frame = cv2.resize(cropped, (width, height))
            out.write(frame)

        out.release()
        print(f"Video saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error generating video: {e}")
        return False