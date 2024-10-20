from flask import Flask, render_template, request, jsonify, redirect, url_for
import subprocess
import json
import os
import webbrowser

app = Flask(__name__)

# Load tests from JSON file
with open('tests.json') as f:
    tests = json.load(f)

# Load settings from settings.py
def load_settings():
    settings = {}
    with open('settings.py') as f:
        exec(f.read(), settings)
    return settings

settings = load_settings()

@app.route('/')
def index():
    return render_template('index.html', tests=tests)

@app.route('/settings', methods=['GET', 'POST'])
def settings_page():
    if request.method == 'POST':
        with open('settings.py', 'w') as f:
            f.write(f"res_file = '{request.form['res_file']}'\n")
            f.write(f"token = '{request.form['token']}'\n")
            f.write(f"requestid = {request.form['requestid']}\n")
            f.write(f"blistRegionCodes = {request.form['blistRegionCodes']}\n")
            f.write(f"bregionCode = {request.form['bregionCode']}\n")
            f.write(f"brole = '{request.form['brole']}'\n")
            f.write(f"main_path = '{request.form['main_path']}'\n")
            f.write(f"sand_token = '{request.form['sand_token']}'\n")
        return redirect(url_for('settings_page'))
    return render_template('settings.html', settings=settings)

@app.route('/run_test', methods=['POST'])
def run_test():
    group_name = request.form['group_name']
    test_name = request.form['test_name']
    test = tests.get(group_name, {}).get('tests', {}).get(test_name)
    if test:
        parameters = {key: request.form.get(key, value) for key, value in test['parameters'].items()}
        command = test['command']

        # Save parameters to JSON file
        with open('test_args.json', 'w') as f:
            json.dump(parameters, f)

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Save logs to a file
        log_path = parameters.get('log_path', 'reports')
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        report_file = os.path.join(log_path, f"{group_name}_{test_name}.log")
        with open(report_file, 'w') as f:
            f.write(f"stdout:\n{stdout.decode()}\n\nstderr:\n{stderr.decode()}")

        return jsonify({
            'stdout': stdout.decode(),
            'stderr': stderr.decode(),
            'returncode': process.returncode,
            'log_path': log_path,
            'report_file': report_file
        })
    return jsonify({'error': 'Test not found'}), 404

@app.route('/open_folder', methods=['POST'])
def open_folder():
    log_path = request.form['log_path']
    webbrowser.open(log_path)
    return jsonify({'message': 'Folder opened'})

if __name__ == '__main__':
    app.run(debug=True)
