from flask import render_template, request
from app import app
from app.utils import parse_cv_file, extract_job_text
from app.rewriting import rewrite_lines

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():

    # Process CV
    cv_file = request.files["cv_file"]
    cv_lines = parse_cv_file(cv_file)

    # Process job text
    job_text = request.form["job_description"]

    # Rewrite the CV based on the job description
    output_text = rewrite_lines(cv_lines, job_text)

    return render_template("result.html", tailored_cv=output_text)