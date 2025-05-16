# Image to Video Generator Web App

This project is a simple Flask web app that lets you upload an image and add a prompt, then generates a short zoom-in video based on the image.

## How to run

1. Clone the repo
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the Flask app
```bash
python app.py
```
4. Open `http://127.0.0.1:5000` in your browser

## Note

- The "prompt" currently does not affect the video generation (placeholder for future AI enhancement).
- Video generation uses OpenCV to create a simple zoom effect for demo purposes.
- This project is open source and free to use.