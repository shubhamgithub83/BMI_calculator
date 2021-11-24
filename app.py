from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def bmi():
    data = request.get_json()
    weight = int(data['weight'])
    height = int(data['height'])
    bmi = weight / (height / 100) ** 2
    if bmi < 18:
        return jsonify({'Underweight=': bmi})
    elif bmi < 25:
        return jsonify({'Normal': bmi})
    else:
        return jsonify({'Overweight': bmi})


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug= True)