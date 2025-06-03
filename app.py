from flask import Flask,render_template,jsonify,request,redirect,url_for,flash
from  database import engine , load_jobs_from_db,load_job_from_db,load_application_from_db,add_application_to_db
from sqlalchemy import text,create_engine
import os
#mailing to reciepiant
from flask_mail import Mail, Message 

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get("sendermail")
app.config['MAIL_PASSWORD'] = os.environ.get("password")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get("sendermail")

#Conformation Message
mail=Mail(app)


@app.route('/home')
def hello_world():

    jobslist=load_jobs_from_db()
    return render_template('home2.html',jobs=jobslist) 

@app.route('/')  
def index():
    jobslist=load_jobs_from_db()
    return render_template('home2.html',jobs=jobslist)

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method =="POST":
        pass 
    return render_template('register.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method =="POST":
        pass 
    return render_template('login.html')


@app.route("/job/<id>")
def load_job(id):
    jobsingle = load_job_from_db(id)
    if not jobsingle:
        return render_template('404.html'), 404  # Render a custom 404 page if job not found
    return render_template('jobpage.html', job=jobsingle)


@app.route("/job/<id>/apply", methods=["GET","POST"])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
     
    add_application_to_db(id, data)
    
    name=request.form.get("full_name")
    email=request.form.get("email")
    
    # Send confirmation email
    msg = Message('Application Confirmation',
                sender=os.environ.get("sendermail"),
                recipients=[email])
    msg.body = f"hello {name}, your application for the job has been submitted successfully"
    mail.send(msg)
        
    return render_template('application_submitted.html', application=data, job=job)

#provide json data /api endpoints for scrapping job listings
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify([dict(job) for job in jobs])


@app.route("/api/jobs/<id>")
def got_job_by_id(id):
    jobs=load_jobs_from_db()
    return jsonify(dict(jobs))

@app.route("/api/application/<id>")
def got_application_by_id(id):
    application_data = load_application_from_db(id)
    if application_data:
        return jsonify(dict(application_data))  # ✅ Convert RowMapping to dict
    else:
        return jsonify({"error": "Application not found"}), 404


if __name__ == '__main__':
    
    
    app.run(debug=True, host='0.0.0.0')