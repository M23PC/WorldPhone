from flask import Flask, render_template

app= Flask(__name__)


@app.route ('/')
def home():
    return render_template('index.html')

@app.route ('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route ('/catalogoIphone')
def catalogoIphone():
    return render_template('catalogoIphone.html')

if __name__ == '__main__':
    app.run(debug=True)