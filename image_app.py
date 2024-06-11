from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/gv/code/general_projects/changing_images/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit ('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def idex():
    if request.method == 'POST':
        image = request.files['file']

        if image.filename == '':
            print("Invalid submission")
            return redirect(request.url)

        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir, app.config['uploads'], image.filename))
            ###PERFORM OTHER OPERATIONS HERE###
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
