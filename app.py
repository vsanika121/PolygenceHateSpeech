from flask import Flask, request, render_template, redirect, url_for  
from flask_sqlalchemy import SQLAlchemy
from model.ipynb import modeluse  
# from transformers import pipeline  
  
# pipe = pipeline("text-classification", model="Hate-speech-CNERG/bert-base-uncased-hatexplain")    
  
  
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
db = SQLAlchemy(app)  
  
class TextEntry(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    content = db.Column(db.Text, nullable=False)  
    category = db.Column(db.String(100), nullable=False)
    context = db.Column(db.Text, nullable=False)  
 #   filterprob = db.Column(db.Numeric, nullable=False)
  
@app.route("/", methods=['GET', 'POST', 'POST'])  
def home():  
    if request.method == 'POST':  
        content = request.form.get('content')  
        category = request.form.get('category')
        context = request.form.get('context')
      #  input = content + context 
      #  output = pipe(input)[0]["score"]   
        entry = TextEntry(content=content, category=category, context=context)  
        db.session.add(entry)  
        db.session.commit()  
        return redirect(url_for('home'))  
    return render_template('home.html')  
  
if __name__ == "__main__":
    with app.app_context():  
        db.create_all()  
    app.run(debug=True)  

returns = []
def outputprob(num_iterations):
    for i in range(num_iterations):
        returnprob = modeluse()
        returns.append(returnprob)

def calc_avg_100():
    for i in range(100, len(returns) + 1, 100):
        last_100_outputs = outputs[i-100:i]
        average = sum(last_100_outputs)/ 100
        print(f"Average of outputs from {i-99} to {i}: {average}")
    will_retrain = return
    if will_retrain < 0.75():
        print(f"retrain model")
outputprob(500)
calc_avg_100()