from sqlalchemy import create_engine, text # type: ignore
import os
from dotenv import load_dotenv
load_dotenv()
# db_connection_string=os.getenv('connection_string')
db_connection_string = "mysql+pymysql://root:1234@localhost:3306/Careers"
engine = create_engine(db_connection_string)
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("Database connection successful!")
except Exception as e:
    print("Database connection failed:", e)


def load_jobs_from_db ():

    """Load all jobs from the database."""
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = [row._mapping for row in result.fetchall()]
        return jobs
    
def load_job_from_db(id):

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
        #: is string formatting , val name of variable can be anything in sqlachemy
    rows=[]
    for row in result.all():
        rows.append(row._mapping)
    if len(rows) == 0 :
        return None
    else:
        return row
    


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("""
            INSERT INTO application (
                job_id, full_name, email, linkedin_url,
                education, work_experience, resume_file_path
            ) VALUES (
                :job_id, :full_name, :email, :linkedin_url,
                :education, :work_experience, :resume_file_path
            )
        """)

        conn.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_file_path': data['resume_url']
        })
        conn.commit()

def load_application_from_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM application WHERE id = :id")
        result = conn.execute(query, {"id": id}).fetchone()
        return result



