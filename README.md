This browser-based application is created to be used in health sector to fetch a patient's prior medical reports.
This can be used in the following manners:
 1)A patient can fetch his previous medical reports in any hospital using this application.
 2)In the case of an accident, the doctor can get to know the medical details of a patient so that he can operate further on him/her.

To run this application, firstly setup a virtual environment "env" and activate it using "env\Scripts\activate" in command prompt terminal.
After that, install opencv, flask, opencv-contrib-python, flask_sqlalchemy, and pillow.
Now, to run the application, type the following commands in cmd:
"set FLASK_ENV=development"
"set FLASK_APP=flask_webservice.py"
"flask run"
Then, open the generated URL.

In the application,
Scrolling down the homepage, upload the image of the patient and click on submit.
The application would recognise the face and fetch the data accordingly.


I have trained my application for 3 faces as of now.
The data for training the face recognition application is stored in the directory "Dataset".
For using your face, firstly you would have to run these commands in cmd under virtualenv:
"python face_data.py"  and type the integer starting from 4 (as 3 users are already trained) #-- Keeping your face in front of your webcam --#
"python face_train.py"
 and then add your name in <17>line of face_site.py  #-- names = ['None', 'Archi', 'Shruti', 'Rohit', 'your_name'] --#
 your face can be recognised now.
 Now, enter your details in the database using lines<61><62><63> in flask_webservice.py
 Now follow the steps from line 8 to 16 mentioned above. 
 
 
 Upgrades in the application I couldn't manage to execute:
 1) Uploading a new patient through the web browser itself.
 2) Capturing the image with live webcam instead of uploading an image.
 3) Enhancing the UI\UX.
  
