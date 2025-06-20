from flask import render_template, request
from app import app
""" from app.utils import parse_cv_file, extract_job_text
from app.matching import get_matches
from app.rewriting import rewrite_text
 """
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    cv_file = request.files["cv_file"]
    
    job_text = request.form["job_description"]

    print(str(job_text))



    output_text = "Hello"
    return render_template("result.html", tailored_cv=output_text)


""" def process():
    cv_file = request.files["cv_file"]
    job_text = request.form["job_description"]
    
    cv_lines = parse_cv_file(cv_file)
    job_lines = job_text.strip().split("\n")
    
    matches = get_matches(cv_lines, job_lines)
    rewritten = [(line, rewrite_text(line)) for line, _, score in matches if score < 0.7]

    return render_template("result.html", matches=matches, rewrites=rewritten) """
