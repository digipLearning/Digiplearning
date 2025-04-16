from flask import Flask, request, render_template, jsonify
from model.inference import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    learner_data = request.json  # Expecting JSON input
    recommendations = get_recommendations(learner_data)
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
