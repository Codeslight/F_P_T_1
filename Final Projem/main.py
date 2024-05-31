# Import
from flask import Flask, render_template,request, redirect
import k

app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler

@app.route('/', methods=['POST'])
def process_form():
    button_chat = request.form.get('button_chat')
    return render_template('index.html', button_chat=button_chat)

    
@app.route('/s_a')
def s_a():
    s=k.tr_konusma()
    return render_template(".html", s=s)


if __name__ == "__main__":
    app.run(debug=True)
