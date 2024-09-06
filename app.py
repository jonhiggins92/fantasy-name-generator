from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Define syllable groups
beginnings = ['An', 'Lo', 'Is', 'Tar', 'Ur', 'Jen', 'Mor', 'Al', 'Sen']
middles = ['dre', 'fal', 'gor', 'las', 'net', 'rak', 'sav', 'vin', 'zul']
ends = ['dar', 'ius', 'moth', 'wen', 'thor', 'ion', 'on', 'an', 'el']

def generate_name():
    syllables_count = random.randint(1, 3)  # 1, 2, or 3 syllables

    if syllables_count == 1:
        return random.choice(beginnings)
    elif syllables_count == 2:
        return random.choice(beginnings) + random.choice(ends)
    else:
        return random.choice(beginnings) + random.choice(middles) + random.choice(ends)

@app.route('/')
def home():
    name = generate_name()
    return render_template('index.html', name=name)

@app.route('/generate')
def generate():
    name = generate_name()
    return jsonify(name=name)

if __name__ == "__main__":
    app.run(debug=True)
