import os
import os.path
from unicodedata import name
import cv2

from face_site import Predict
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///patientrec.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#creating database
class patientrec(db.Model):
         sno = db.Column(db.Integer, primary_key=True)
         name = db.Column(db.String(50), nullable=False)
         age = db.Column(db.Integer)
         address = db.Column(db.String(200))
         diseases = db.Column(db.String(200))
         operations = db.Column(db.String(300))
         date_created = db.Column(db.DateTime, default=datetime.utcnow)

         def __repr__(self) -> str:
            return f"{self.name} - {self.age} - {self.diseases} - {self.operations}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])

#uploading the image for face recognition
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        filename = upload.filename
        destination = "/".join([target, filename])
        upload.save(destination)
    execution_path = target
    print(execution_path)

    #Fetching the data of the patient
    id = Predict(os.path.join(execution_path, filename))
    print("the name:", id)

    #upload = patientrec(name="Rohit", age="22", address="New Delhi", diseases="skin cancer", operations ="Mohs surgery")
    #upload = patientrec(name="Archi", age="19", address="Near Hospital, Hanumangarh, Rajasthan", diseases="Hypermetropia, Allergic to pollen")
    #db.session.add(upload)
    #db.session.commit()
    show = patientrec.query.filter_by(name=id).all()
    return render_template("result.html", show=show)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=True, port =8000)