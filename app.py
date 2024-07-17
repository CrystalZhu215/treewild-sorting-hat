import os

from flask import Flask, request, render_template, send_file
from sorting import create_sorting

app = Flask(__name__)
app.config["DOWNLOAD_FOLDER"] = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def run():
    return render_template("index.html", path=None)

@app.route('/', methods =["POST"])
def loading():
    num_kids = request.form.get("nkids")
    return render_template("loading.html", n=num_kids)

@app.route('/generate_audio/<num_kids>')
def generate_audio(num_kids):
    audio = create_sorting(int(num_kids))
    path = os.path.join(app.config['DOWNLOAD_FOLDER'], "sorting.mp3")
    audio.export(path, format="mp3")
    return render_template("download.html", path=path)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename): 
    # Must take filename as argument
    return send_file("sorting.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run()