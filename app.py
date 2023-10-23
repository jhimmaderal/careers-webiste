from flask import Flask, json, jsonify, render_template, request
from database import load_jobs_from_db, load_job_from_db, add_application_db

webApp = Flask(__name__)
jobs = load_jobs_from_db()


@webApp.route("/")
def reddCareers():
  return render_template('home.html', jobs=jobs, company="Redd")


@webApp.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


@webApp.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  else:
    return render_template('jobpage.html', job=job), 200


@webApp.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)


@webApp.route("/job/<id>/apply", methods=['post'])
def apply_job(id):
  data = request.form
  job = load_job_from_db(id)

  add_application_db(id, data)

  return render_template('application.html', application=data, job=job)


if __name__ == "__main__":
  webApp.run(host="0.0.0.0", debug=True)
