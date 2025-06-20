""" from transformers import pipeline

paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

def rewrite_text(text):
    return paraphraser("paraphrase: " + text, max_length=60, num_return_sequences=1)[0]['generated_text']
 """