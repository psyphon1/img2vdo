from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from utils import generate_video_from_image_and_prompt

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files or request.files['image'].filename == '':
            return "No image uploaded", 400
        image = request.files['image']
        prompt = request.form.get('prompt', '')
        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)
        output_path = os.path.join(OUTPUT_FOLDER, f"output_{os.path.splitext(image.filename)[0]}.mp4")
        # Generate video from image and prompt
        success = generate_video_from_image_and_prompt(image_path, prompt, output_path)
        if not success:
            return "Video generation failed", 500
        return redirect(url_for('download_video', filename=os.path.basename(output_path)))
    return render_template('index.html')

@app.route('/download/<filename>')
def download_video(filename):
    path = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(path):
        return "File not found", 404
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)