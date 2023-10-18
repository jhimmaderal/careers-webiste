from flask import Flask, jsonify, render_template
from database import load_jobs_from_db

webApp = Flask(__name__)
jobs = load_jobs_from_db()


@webApp.route("/")
def reddCareers():
  return render_template('home.html', jobs=jobs, company="Redd")


@webApp.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  webApp.run(host="0.0.0.0", debug=True)
