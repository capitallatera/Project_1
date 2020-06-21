from flask import Flask, request, render_template, jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/login',methods=["POST"])
def login():
    content=request.form['text1']
    if len(content)>=0:
        value=[content]
        predict=model.predict(value)   
        # use without label encoding
        
        return str(predict[0])
        

if __name__=="__main__":
    app.run(debug=True)

