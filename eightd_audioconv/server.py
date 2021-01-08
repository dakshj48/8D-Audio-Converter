from flask import Flask, render_template, request, send_file, url_for, send_from_directory
from audioCon import convert
from pathlib import Path
import os
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
        # outputPath = Path(__file__).parent.parent / 'bin' / outputname
        outputPath = outputname
        converted = open(outputPath, 'rb')

        def stream_and_remove():
            nonlocal converted, outputPath, f
            yield from converted
            converted.close()
            os.remove(outputPath)
            os.remove(f.filename)

        resp = app.response_class(stream_and_remove(), mimetype='audio/mpeg')
        resp.headers.set('Content-Disposition', 'attachment', filename=outputname)
        return resp


def run():
    app.run(debug=True, threaded=True)


if __name__ == '__main__':
    run()
