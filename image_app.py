from flask import Flask, render_template, request, redirect, flash, url_for, render_template_string
from PIL import Image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/gv/code/general_projects/changing_images/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit ('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print(f"request path {request.path}")
    if request.method == 'POST':

        if 'filename' not in request.files:
            return redirect(request.url)
        

        file = request.files['filename']

        if file.filename == '':
            return 'No selected file'

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            workOnImage(filepath)
            return redirect(url_for('index'))

    return render_template('index.html')

def workOnImage(filepath):
    picture =Image.open(filepath)
    width, height = picture.size

    for x in range(width):
        for y in range(height):
            current_color = picture.getpixel((x,y))
            print(f'Pixel at ({x},{y}): {current_color}')
            picture.putpixel((x,y) ,(255 - current_color[0], 255 - current_color[1], 255 - current_color[2]))

           
    picture.save(filepath)




if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host = 'localhost', port=8080, debug = True)

