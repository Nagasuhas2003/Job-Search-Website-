from flask import Flask,render_template,jsonify
from  database import engine
from sqlalchemy import text

app=Flask(__name__)


def load_jobs_from_db ():

    with engine.connect() as conn:
        result =conn.execute(text("select * from jobs"))

        jobs=[]
        for row in result.all():
            jobs.append(row._mapping)
        return jobs
@app.route('/')
def hello_world():
#return 'Hello, World! this is naga'
#without using bootstap    return render_template('home.html')
#with using bootsrap
    jobslist=load_jobs_from_db()
    return render_template('home2.html',jobs=jobslist)    

@app.route("/api/jobs")
def list_jobs():
    jobslist=load_jobs_from_db()
    return jsonify(jobs=jobslist)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')