from flask import Flask, render_template,request,url_for,redirect
# this makes a new flask a application
app = Flask(__name__)

# this line makes a empty url which looks like 127.0.0.2.8080/
@app.route('/')
def index(): # making a fubnnction to write the logic for the home page
    return render_template('index.html') # its showing index.html on the url mentioned

##as a single user can send multiple messages so we store it in a list of messages
messages = []

# it makes a url 127.0.o.8080/submit and method post means it is containing data
# and its sending the data to the server
@app.route('/submit', methods=['POST'])
def submit(): #making a function to write logic for the homepage
    name = request.form["name"] # its taking the user input from the name field
    email = request.form["email"] # its taking the user input from the email field
    message = request.form["messages"] #its taking the user input from the message field

    messages.append({"name": name, "email":email,"message": message})

#it is showing thee thank_you message after submitting the form
    return redirect(url_for("thank_you"))

#we are making a url 127.0.o.8080/thNK_YOU
@app.route('/thank_you')
def thank_you():
    #its just displaying this message
    return "Thank you for contacting us!"

if __name__=='__main__':
    app.run(debug=True)