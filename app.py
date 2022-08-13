from multiprocessing import Value
import subprocess
import os
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        command_to_execute = request.form.get("command").split('::')
        last_result = subprocess.getoutput(command_to_execute)
        return render_template('index.html', last_result=last_result)