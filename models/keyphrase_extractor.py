from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("beogradjanka/bart_finetuned_keyphrase_extraction")
model = AutoModelForSeq2SeqLM.from_pretrained("beogradjanka/bart_finetuned_keyphrase_extraction")

def extract(text: str):
    tokenized_text = tokenizer(text, return_tensors='pt')
    translation = model.generate(**tokenized_text)
    translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
    formatted_texts = [phrase.strip() for phrase in translated_text.split(",")]
    return list(set(formatted_texts))
