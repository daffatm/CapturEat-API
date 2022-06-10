from flask import Flask, request, jsonify, flash, redirect
from werkzeug.utils import secure_filename
from configuration import load_model
from recommend import get_result
import os
import cv2

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'logs/uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return "<p>Server OK!</p>"

@app.route('/predict', methods=['POST', 'GET'])
def load():
    if request.method == "POST":
        CLASSES = ['BG', 'bakso', 'sate', 'rendang']
        
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        image_file = request.files['image']
        if image_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(file_path)
            
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        model = load_model()
        
        r = model.detect([image], verbose=1)[0]
        
        try:
            food = CLASSES[r['class_ids'][0]]
            recommendation = get_result(food)
        except:
            recommendation = 'Unknown'
            
        return jsonify(recommendation)
    return "<p>Get from Predict!</p>"
if __name__ == '__main__':
    app.run(debug=True, threaded=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
