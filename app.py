from flask import Flask, request, render_template, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Define allowed file extensions
audio_extensions = {'mp3', 'wav', 'ogg'}
text_extensions = {'txt'}

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if both files are uploaded
    if 'audioFile' not in request.files or 'textFile' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('index'))
    
    audio_file = request.files['audioFile']
    text_file = request.files['textFile']

    # If no file is selected, return error
    if audio_file.filename == '' and text_file.filename == '':
        flash('No selected file', 'error')
        return redirect(url_for('index'))

    # Handle audio file upload
    if audio_file.filename != '' and allowed_file(audio_file.filename, audio_extensions):
        audio_filename = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(audio_filename)
        flash('Audio file uploaded successfully', 'success')
        return redirect(url_for('index'))

    # Handle text file upload
    elif text_file.filename != '' and allowed_file(text_file.filename, text_extensions):
        text_filename = os.path.join(app.config['UPLOAD_FOLDER'], text_file.filename)
        text_file.save(text_filename)
        flash('Text file uploaded successfully', 'success')
        return redirect(url_for('index'))

    # If uploaded file type is not allowed
    else:
        flash('File type not allowed', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
