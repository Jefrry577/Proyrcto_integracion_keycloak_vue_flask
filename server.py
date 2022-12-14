from flask import Flask, jsonify, render_template
from flask_cors import CORS
import pymongo

client = pymongo.MongoClient('mongodb+srv://Jefrry:AcepRFF3o6U3HEYC@cluster.kyrkpj4.mongodb.net/?retryWrites=true&w=majority')
myDB = client["Test"]
myCollection = myDB["item"]

mytask = {"name": "estudiar pyton con flask", "date":20220403}

resoult =myCollection.insert_one(mytask)
print(resoult)



app= Flask(__name__,
    static_folder='./fronted/dist/static',
    template_folder='./fronted/dist'
    )
cors = CORS(app, resources={r"/api/*":{"origins": "*"}})
@app.route('/api/v1.0/mensaje')
def Mensaje():
    return jsonify('nuevo mensaje desde un servidor Flask')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)