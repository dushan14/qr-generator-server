import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Location

@app.route('/',methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':  
        place=request.form.get('place')
        beacon1=request.form.get('beacon1')
        beacon2=request.form.get('beacon2')
        beacon3=request.form.get('beacon3')
        try:
            location=Location(
                place=place,
                beacon1=beacon1,
                beacon2=beacon2,
                beacon3=beacon3
            )
            db.session.add(location)
            db.session.commit()
            message="Saving Success id:"+str(location.id)
            return message
        except:
            return "Operation Fail"
    return render_template("getdata.html")  



@app.route('/getData/<id_>')
def get_data(id_):
    location = Location.query.filter_by(id=id_).first()
    return jsonify({"id":location.id,"place":location.place,"beacon1":location.beacon1,"beacon2":location.beacon2,"beacon3":location.beacon3})

if __name__ == '__main__':
    app.run()
   