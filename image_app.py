from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def idex():
    if request.method == 'POST':
        file = request.files['filename']
        if file:
            #save file to directory
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)

            ###PERFORM OTHER OPERATIONS HERE###
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
