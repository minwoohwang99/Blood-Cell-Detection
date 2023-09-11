from flask import render_template, request, jsonify
from your_app import app

# Route to render HTML template
@app.route('/')
def index():
    return render_template('your_template.html')

# Route to process image
@app.route('/process_image', methods=['POST'])
def process_image():
    # ... your image processing code ...

    # Return processed image URL
    return jsonify({"processed_image_url": "/static/processedImage.jpg"})
