from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        details = request.form
        if details['form_type'] == 'add_user':
            #return add_user(details['uid'],details['fname'],details['lname'])

        elif details['form_type'] == 'add_credit':
            #return add_credit(details['uid'],details['credit'])

        elif details['form_type'] == 'view_user':
            #return view_user(details['uid'])
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0')