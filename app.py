from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

@app.route('/home')
def save():
    return render_template('save.html')

@app.route('/show')
def show():
    return render_template('show.html')


@app.route('/animal', methods=['POST'])
def animal_save():
    animal = request.form['animal']
    count = request.form['count']

    doc = {
        'animal':animal,
        'count':count
    }
    db.animals.insert_one(doc)

    return jsonify({'result':'success'})


@app.route('/count', methods=['GET'])
def animal_show():
    animal = request.args.get('animal')

    if db.animals.find_one({'animal': animal}, {'_id': 0}) is not None:
        count = db.animals.find_one({'animal': animal}, {'_id': 0})['count']
        return ''+animal+'는(은) '+count+'마리 입니다!'
    else:
        return ''+animal+'는(은) 없어요 ㅠ.ㅠ'



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)