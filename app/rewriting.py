from transformers import pipeline

paraphraser = pipeline("text2text-generation", model="google/flan-t5-small")

def rewrite_line(cv_line, job_description):

    orig_length = len(cv_line.split())
    max_new_tokens  = int(orig_length * 1.3) + 1  # +1 to round up

    prompt = (
        f"Improve the following CV bullet point to make it more professional, clear, "
        f"and aligned with the job description. If it seems irrelevant or weak, respond with REMOVE.\n\n"
        f"Job Description: {job_description}\n"
        f"CV Line: {cv_line}"
    )

    result = paraphraser(prompt, max_new_tokens=max_new_tokens, num_return_sequences=1)[0]["generated_text"].strip()

    return result


def rewrite_lines(cv_lines, job_text):

    # Rewrite each line based on the job description
    rewritten_lines = []

    for line in cv_lines:

        print("\n\nCurrent CV ine:")
        print(line)

        new_line = rewrite_line(line, job_text)

        print("\n\nModified line:")
        print(new_line)

        if "REMOVE" not in new_line:
        
            rewritten_lines.append(new_line)

    output_text = "\n".join(rewritten_lines)

    return output_text



