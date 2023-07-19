from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(_name_)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html', num_students=5)

@app.route('/process', methods=['POST'])
def process():
    students = request.form.getlist('student')
    marks = request.form.getlist('mark')
    marks = [int(mark) for mark in marks]
    #bargraph
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.bar(students, marks)
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.title('Student Marks')
    plt.xticks(rotation=45)
    #piecchart
    plt.subplot(122)
    plt.pie(marks, labels=students, autopct='%1.1f%%')
    plt.title('Student Marks Distribution')
    plt.savefig('static/visualization.png')
    plt.close()
    return render_template('visualization.html')

if _name_ == '_main_':
    app.run(debug=True)