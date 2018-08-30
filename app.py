import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, send_file
from flask import jsonify
from PIL import Image
import qrcode
from io import StringIO, BytesIO

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

root_link="https://beacon-data-pro.herokuapp.com/"
get_data_link=root_link+"/get/"

from models import Location

@app.route('/',methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':  
        place=request.form.get('place')
        beacon1=request.form.get('beacon1')
        beacon2=request.form.get('beacon2')
        beacon3=request.form.get('beacon3')
        beacon1x=request.form.get('beacon1x')
        beacon1y=request.form.get('beacon1y')
        beacon2x=request.form.get('beacon2x')
        beacon2y=request.form.get('beacon2y')
        beacon3x=request.form.get('beacon3x')
        beacon3y=request.form.get('beacon3y')

        try:
            location=Location(
                place = place,
                beacon1 = beacon1,
                beacon1x = beacon1x,
                beacon1y = beacon1y,
                beacon2 = beacon2,
                beacon2x = beacon2x,
                beacon2y = beacon2y,
                beacon3 = beacon3,
                beacon3x = beacon3x,
                beacon3y = beacon3y
            )
            db.session.add(location)
            db.session.commit()
            return getqr(location.id)
        except:
            return "Operation Fail"
    return render_template("getdata.html")  


@app.route('/get/<id_>')
def get_data(id_):
    location = Location.query.filter_by(id=id_).first()
    data={"id":location.id,"place":location.place,
    "beacon1":{"uuid":location.beacon1,"x":location.beacon1x,"y":location.beacon1y},
    "beacon2":{"uuid":location.beacon2,"x":location.beacon2x,"y":location.beacon2y},
    "beacon3":{"uuid":location.beacon3,"x":location.beacon3x,"y":location.beacon3y}}
    return jsonify(data)

@app.route('/getqr/<id>')
def getqr(id):
    qr_link=get_data_link+str(id)
    pil_img=qrcode.make(qr_link)
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
   