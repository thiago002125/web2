from app import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nascimennto =db.Column(db.Date, nullable=False)


    def __init__(self, nome, nascimento) :
        self.nome = nome
        self.nascimennto = nascimento

    def __repr__(self):
        str= "<Aluno{} {}.".format(self.id, self)  
        return str

    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            'nascimento': self.nascimennto
        }