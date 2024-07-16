from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/climate_analysis')
def climate_analysis():
    result = subprocess.run(['spark-submit', 'spark_jobs/climate_analysis.py'], capture_output=True, text=True)
    return jsonify({"result": result.stdout})

@app.route('/api/climate_model')
def climate_model():
    result = subprocess.run(['spark-submit', 'machine_learning/climate_model.py'], capture_output=True, text=True)
    return jsonify({"result": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)
