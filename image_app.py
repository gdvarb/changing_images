from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

app.config['uploads'] = '/Users/gv/code/general_projects/changing_images/uploads'

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
