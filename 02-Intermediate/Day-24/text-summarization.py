from transformers import pipeline

# Sample text
text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines,
    in contrast to the natural intelligence displayed by humans and animals.
    Leading AI textbooks define the field as the study of "intelligent agents":
    any device that perceives its environment and takes actions that maximize
    its chance of successfully achieving its goals.
    Colloquially, the term "artificial intelligence" is often used to describe
    machines (or computers) that mimic "cognitive" functions that humans associate
    with the human mind, such as "learning" and "problem-solving".
"""

# Initialize the summarizer
summarizer = pipeline("summarization")

# Generate the summary
summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
print("Summary:")
print(summary[0]['summary_text'])