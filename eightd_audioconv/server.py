from flask import Flask, render_template, request, send_file, url_for
from audioCon import convert
app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        period = request.form['period']
        if period == "":
            period = 200
        outputname = request.form['outputname']
        if outputname == "":
            outputname = f.filename[:-4] + ' - 8D.mp3'
        if outputname[-4:] != '.mp3':
            outputname += '.mp3'
        f.save(f.filename)
        convert(f.filename, outputname, int(period))
        return send_file(outputname, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
