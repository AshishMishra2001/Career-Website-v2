from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db

app=Flask(__name__)
# JOBS=[
#   {
#     'id':1,
#     'title':'Data Analyst',
#     'location':'Delhi,India',
#     'salary':'Rs. 120000'
#   },
#   {
#     'id':2,
#     'title':'Data Analyst',
#     'location':'Delhi,India',
#     'salary':'Rs. 120000'
#   },
#   {
#     'id':3,
#     'title':'Data Analyst',
#     'location':'Delhi,India',
#     'salary':'Rs. 120000'
#   },
#   {
#     'id':4,
#     'title':'Backend Developer',
#     'location':'Delhi,India',
#     'salary':'Rs. 120000'
#   },
#   {
#     'id':5,
#     'title':'Frontend Developer',
#     'location':'Delhi,India'
#   }
# ]


   # print(result_dicts)


@app.route("/")
def hello_world():
  jobs=load_jobs_from_db()
  return render_template('home.html',jobs=jobs, company_name="Career")

@app.route("/api/jobs")
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)

@app.route("/jobs/<id>")
def show_job(id):
  job=load_jobs_from_db(id)
  return jsonify(job)


# @app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
# def apply(job_id):
#     job = next((job for job in JOBS if job["id"] == job_id), None)
#     if not job:
#         return "Job not found", 404

#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
#         print(f"New application for {job['title']} from {name} ({email}): {message}")
#         return f"<h3>Thank you {name}! Your application for {job['title']} has been submitted.</h3>"

#     return render_template('apply.html', job=job)

#     return "Application sent successfully!"
if __name__== "__main__":
  app.run(host='0.0.0.0',debug='True')

