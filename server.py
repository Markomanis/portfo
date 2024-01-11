from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data.get('email', '')
        message = data.get('message', '')
        file = database.write(f'\n{email},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data.get('email', '')
        message = data.get('message', '')
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='')
        csv_writer.writerow([email, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')
      except:
          return "did not save to database"
    else:
        return 'something went wrong! Try to contact me manually!'
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)