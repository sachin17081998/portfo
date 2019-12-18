from flask import Flask
from flask import render_template,request
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/info')
def blog():
    return 'i am studying mca from bit mesra'



def write_to_file(data):
    with open('server/database.txt',mode='a') as database:
        name=data['fullname']
        email=data['email']
        subject=data['subject']
        message=data['message']
        database.write(f'\nname:{name}\nemail:{email}\nsub:{subject}\nmessage:{message}\n\n')


def write_to_csvfile(data):
    with open('server/database.csv',newline='',mode='a') as csvdatabase:
        name=data['fullname']
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(csvdatabase,delimiter=',',quotechar='"' ,quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])



@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csvfile(data)
        return 'form submitted'



#we are writing this code to make debugger mode on
if __name__ == '__main__':
    app.run(debug=True)
