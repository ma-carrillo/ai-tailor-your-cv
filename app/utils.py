def parse_cv_file(file):
    lines = file.read().decode("utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]

def extract_job_text(text):
    return text.strip().split("\n")
 