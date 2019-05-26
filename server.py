from flask import Flask, render_template, request, send_file
from audioCon import convert

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        convert(f.filename)
        outputfile = f.filename[:-4] + ' - 8D.mp3'
        return send_file(outputfile, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)