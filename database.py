import os
from sqlalchemy import create_engine, text

db_connectionString = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connectionString,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def add_application_db(id, data):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO applications(job_id, fullname, email, linkedin, education, workExperience, resumeUrl) VALUES (:job_id, :fullname, :email, :linkedin, :education, :workExperience, :resumeUrl)"
    )
    conn.execute(
        query, {
            "job_id": id,
            "fullname": data['fullname'],
            "email": data['email'],
            "linkedin": data['linkedin'],
            "education": data['education'],
            "workExperience": data['workExperience'],
            "resumeUrl": data['resumeUrl']
        })
