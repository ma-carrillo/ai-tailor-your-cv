""" from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_matches(cv_lines, job_lines, threshold=0.3):
    results = []
    for cv in cv_lines:
        for job in job_lines:
            sim = util.cos_sim(model.encode(cv), model.encode(job))[0][0]
            if sim > threshold:
                results.append((cv, job, float(sim)))
    return results """