from flask import Flask, render_template, request, jsonify
import os
import time
import subprocess

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
    file_name = input_command.split("_-_")[-1]
    file_path = os.path.join("D:\One_Drive\OneDrive - nakivo.com\SB", file_name)
    attempts = 0
    while not os.path.exists(file_path):
        print(f"File {file_name} does not exist yet, checking again in 10 seconds...")
        time.sleep(10)
        attempts +=1
        if attempts > 30:
            return jsonify({"message": "File not found after 30 attempts"}), 404

    return jsonify({"message": "File is available, browser opened with the link"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
