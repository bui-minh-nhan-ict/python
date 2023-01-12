from flask import Flask, render_template, request, jsonify
import os
import subprocess
import time

app = Flask(__name__, template_folder='D:/Python')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    input_command = request.json.get('input_command')
    file_name = input_command.split("-_")[-1]
    file_path = "E:\\" + file_name
    while not os.path.exists(file_path):
        time.sleep(20)
    return jsonify({"message": "File is available"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
