from flask import Flask, render_template, request, jsonify
import subprocess
import json
import os

app = Flask(__name__)

# Load tests from JSON file
with open('tests.json') as f:
    tests = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', tests=tests)

@app.route('/run_test', methods=['POST'])
def run_test():
    group_name = request.form['group_name']
    test_name = request.form['test_name']
    test = tests.get(group_name, {}).get('tests', {}).get(test_name)
    if test:
        command = test['command']
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Save logs to a file
        report_dir = 'reports'
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        report_file = os.path.join(report_dir, f"{group_name}_{test_name}.log")
        with open(report_file, 'w') as f:
            f.write(f"stdout:\n{stdout.decode()}\n\nstderr:\n{stderr.decode()}")

        return jsonify({
            'stdout': stdout.decode(),
            'stderr': stderr.decode(),
            'returncode': process.returncode
        })
    return jsonify({'error': 'Test not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
