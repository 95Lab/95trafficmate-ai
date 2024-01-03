from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/execute_scripts', methods=['POST'])
def run_scripts():
    year = request.json.get('year')
    scripts = ['prepare_congestion.py', 'prepare_peopleflow.py', 'prepare_rain.py', 
               'rasterize_rain.py', 'rasterize_peopleflow.py']
    for script in scripts:
        cmd = f'python3 {script} -y {year}'
        process = subprocess.Popen(cmd, shell=True)
        process.wait()
    return {'status': 'scripts executed successfully'}

if __name__ == "__main__":
    app.run(debug=True, port=5000)