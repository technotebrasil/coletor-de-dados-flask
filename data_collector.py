#Importar dependências
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String


#Cria instância flask
app = Flask(__name__)

#Conecta com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://usuario:senha@localhost/nomedobanco'
db = SQLAlchemy(app)

class Data(db.Model):
    #cria a tabela
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    shoesize = db.Column(db.Integer)
    sex = db.Column(db.String)

    

    def __init__(self, height, weight, shoesize, sex):
        self.height = height
        self.weight = weight
        self.shoesize = shoesize
        self.sex = sex

#Define rota e página de conteúdo
@app.route("/")
def index():
    return render_template("index.html")

#Define 2 rota e página de conteúdo
@app.route("/success", methods = ['POST'])
def success():
    if(request.method == 'POST'):
        height_ = request.form["height"]
        weight_ = request.form["weight"]
        shoesize_ = request.form["shoesize"]
        sex_ = request.form["sex"]
        data = Data(height_,weight_,shoesize_,sex_)
        db.session.add(data)
        db.session.commit()
        return render_template("sucesso.html")    

#Executando e controlando o script
if (__name__ =="__main__"):
    app.run(debug=True)
