from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Pagina_web.html')

@app.route('/Formulario.html')
def formulario():
    return render_template('Formulario.html')

@app.route('/Taller_web.html')
def tallerweb():
    return render_template('Taller_web.html')    

if __name__ == '__main__':
    app.run()
