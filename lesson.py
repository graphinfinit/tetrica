"""
описание API

flask-функция принимает POST запросы на 127.0.0.1:5000  с content-type : application/json
Пример входных данных:
{"intervals":{
    "lesson": [1594663200, 1594666800],
    "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    "tutor": [1594663290, 1594663430, 1594663443, 1594666473]
    }}

Выдает ответ в json, например:
{
    "total_time": 3117
}

"""

from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

app = Flask(__name__)


def appearance(intervals):
    # список всех точек
    points = []
    for key in intervals:
        points.extend(intervals[key])
    # список всех интервалов
    spans = [(points[i], points[i+1]) for i in range(0, len(points), 2)]

    result = []
    for point in points:
        flag = 0
        for i in spans:
            if i[0] <= point <= i[1]:
                flag += 1
        if flag == 3:
            result.append(point)

    result.sort()

    total_time = 0
    for i in range(0, len(result), 2):
        total_time += result[i+1] - result[i]
    return total_time


@app.route("/", methods=['POST'])
def f_one():
    data = request.json
    print(data)
    if data:
        intervals = data["intervals"]
        total_time = appearance(intervals)
        return jsonify({"total_time": total_time})

    else:
        return abort(400)


app.run(debug=True)

