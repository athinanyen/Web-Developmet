# isUppercase = False 
# isNumbers = False 
# isSymbols = False 

# isUppercase = bool(input("Do you want uppercase letters? "))
# isNumbers = bool(input("Do you want numbers?"))
# isSymbols = bool(input("Do you want symbols?"))
# length = int(input("How long should your password be?"))

# # string = "iwufhwidhd"
# # string = 'udhegfcueh'
# # string = '''fhecfh'''

# # print(isUppercase)
# # print(isNumbers)
# # print(isSymbols)

# import random
# def generate_password():
#     choices = list("abcdefghijklmnopqrstuwxyz")

#     if isUppercase == True:
#         choices.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#     if isNumbers == True:
#         choices.extend("0123456789")
#     if isSymbols == True:
#         choices.extend('''~!@#$%^&*()-_=+}[{]|\:;,<.>?/''')
#     mypassword = ""

#     for i in range(length):
#         mypassword +=random.choice(choices)
#     print(mypassword)

# generate_password()

# # module
# # random module
# # import random
# # print(random.randint(1,6))

import random 
from flask import render_template, Flask, request  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/fill_form')
def fill_form():
    return render_template('fill_form.html')

@app.route('/password')
def password():
    choices = list("abcdefghijklmnopqrstuvwxyz")

    isUppercase = request.args.get("uppercase")
    isNumbers = request.args.get("numbers")
    isSymbols = request.args.get("symbols")
    length = request.args.get("length")

    if int(length) == None: 
        length = 8 
    if isUppercase == '1': 
        choices.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if isNumbers == '1':
        choices.extend("0123456789")
    if isSymbols == '1':
        choices.extend('''~!@#$%^&*()_+-=){}[]\|:;"',.<>?/]''')

    mypassword = ""
    for i in range(int(length)):
        mypassword += random.choice(choices)

    return render_template('password.html', mypassword=mypassword)


if __name__ == '__main__':
    app.run(debug=True)