import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'J:\\vscode\\excelToweb\\upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        file = request.files['file']
        f_name= file.filename
        f_size= file.content_length
        f_type= file.content_type
        print(f_name)
        # file.save(uploads,f_name)
        # # If the user does not select a file, the browser submits an
        # # empty file without a filename.
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        #     return redirect(url_for('download_file', name=filename))
    return render_template('index.html',message= f_name, f_size= f_size,f_type= f_type)

if __name__ == '__main__':
    app.run(debug=True,port=5000)