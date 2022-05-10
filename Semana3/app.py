# from email.mime import image
# from tkinter import Image
# from turtle import width
from flask import Flask, request, send_file, render_template
from PIL import Image

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/galeria/gato')
def galeria_gato():
    return render_template('galeria.html')

@app.route('/assets/gato2.jpg')
def gato():
    width = int(request.args.get('w',200))
    height = int(request.args.get('h',200))
    image = Image.open('assets/gato2.png')
    image.resize((width, height)).save('assets/gato2_resized.png')
    return send_file('assets/gato2_resized.png')

