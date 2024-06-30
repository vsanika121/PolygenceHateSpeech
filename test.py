from transformers import pipeline  
  
pipe = pipeline("text-classification", model="Hate-speech-CNERG/bert-base-uncased-hatexplain")  
  
sentence = "Hey! How are you doing!"
output = pipe(sentence)[0]["score"]
print(output)