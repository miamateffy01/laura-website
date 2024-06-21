from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact me")
def contactme():
    return render_template("contactme.html")
@app.route("/my work")
def work():
    return render_template("work.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    #SEND IT TO THE RECEIVING MAIL WHICH I HAVE NOT SET UP YET
    flash("Your message has been sent successfully!")

    return redirect(url_for('contactme'))


if (__name__=="__main__"):
  app.run(host="0.0.0.0",debug=True)
    
    