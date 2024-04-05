class Aluno: 
    def __init__(self, matricula, sexo, nome, idade):
        self.matricula = matricula
        self.sexo = sexo
        self.nome = nome 
        self.idade = idade
if __name__=="__main__":
    aluno1 = Aluno("12345", "m", "ricardo", "17")
    print(aluno1.nome)
    print(aluno1.sexo)
    print(aluno1.matricula)
    print(aluno1.idade)