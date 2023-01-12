from flask import Flask, render_template, request, jsonify
import webbrowser
import subprocess
import requests

app = Flask(__name__, template_folder='D:/Python Github/python')
coccoc_location = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    input_command = request.json.get('input_command')
    subprocess.Popen(f'"{coccoc_location}" --start-minimized {input_command}',
                     creationflags=subprocess.CREATE_NO_WINDOW)
    return jsonify({"message": "Browser opened with the link"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
