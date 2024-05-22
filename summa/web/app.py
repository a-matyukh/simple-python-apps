from summa import summa
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def vichislenie():
    print(f"текущий метод: {request.method}")
    if request.method == 'GET':
        return render_template('summa.html')
    elif request.method == 'POST':
        print(f"объекты формы: {request.form}")
        a = int(request.form['a'])
        b = int(request.form['b'])
        return str(summa(a, b))