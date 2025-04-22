
from flask import Flask,render_template,jsonify

app=Flask(__name__)

JOBS =  [
    {
        'id':1,
        'title':'Data Scientist',
        'location':'Bangalore',
        'salary':'Rs.120000'
    },
    {
        'id':2.,
        'title':'Data analyst',
        'location':'Bangalore',
        'salary':'Rs.123040'
    },
    {
        'id':3,
        'title':'Data Engineer',
        'location':'Bangalore',
        'salary':'500000'
    },
    {
        'id':4,
        'title':'Big Data',
        'location':'Bangalore',
        'salary':'Rs.456787'
    }
]
@app.route('/')
def hello_world():
#return 'Hello, World! this is naga'
#without using bootstap    return render_template('home.html')
#with using bootsrap
    return render_template('home2.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')