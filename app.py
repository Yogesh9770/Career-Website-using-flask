from flask import Flask , render_template , jsonify

app=Flask(__name__)

JOBS=[{
    'id':'1',
    'tittle':'Software Developer',
    'company':'google',
    'salary':'Rs 1,00,000'
},
{
    'id':'2',
    'tittle':'Front end developer',
    'company':'Facebook',
    'salary':'Rs 2,00,000'
},
{
    'id':'3',
    'tittle':'Back end developer',
    'company':'Amzaon',
    'salary':'Rs 3,00,000'
},
{
    'id':'4',
    'tittle':'Full stack developer',
    'company':'TCS',
    'salary':'Rs 4,00,000'
}]


@app.route('/')
def hello_world():
    return render_template('index.html', jobs=JOBS)

@app.route('/api/jobs')
def  get_all_jobs():
    return jsonify(JOBS)

if __name__=='__main__':
    app.run(debug=True) 