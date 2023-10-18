from transformers import BartForConditionalGeneration, BartTokenizer

text = input('Enter the text: ')

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(**inputs)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Summary:")
print(summary)