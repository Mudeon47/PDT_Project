from flask import Flask, request, jsonify
from flask_cors import CORS
from dao import DAO

app = Flask(__name__)
CORS(app)

@app.route('/make-hashtag', methods=['post'])
def makeTag():

    doc = request.form.get('text')
    print(request.form)
    print("doc print test :", doc)
    dao = DAO()
    result = dao.keyword(doc)
    response = jsonify(message=result)

    none_key = '적절한 키워드가 없습니다'
    if result != none_key:
        tag = ' '.join(result)
        print("keyword() print test :", tag)
        return response        
    else:
        print("keyword() print test :", result)
        return response

# >python controller.py
if __name__ == '__main__':
    dao = DAO()
    doc = '아무말'
    dao.keyword(doc)
    app.run(debug=True, host='0.0.0.0', port=5000)