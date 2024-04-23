class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
     #Getters
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def get_sexo(self):
        return self.sexo
           
    def set_nome(self, novo_nome):
        self.nome = novo_nome
     #Setters   
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    
    def set_sexo(self, novo_sexo):
        self.sexo = novo_sexo
    #Método
    def apresentar(self):
        print(f'Nome: {self.get_nome()}')
        print(f'Idade: {self.get_idade()}')
        print(f'Sexo: {self.get_sexo()}')
        
        
class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, matricula):
       
     super().__init__(nome, idade, sexo)
     self.matricula = matricula
     
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, nova_matricula):
        self.matricula = nova_matricula
    
    def apresentar(self):
        super().apresentar()
        print(f'Matrícula: {self.get_matricula()}')
        
#Objetos
pessoa1 = Pessoa('Eloise', 29, 'Feminino') 
aluno1 = Aluno('Eloise Helena', 30,'Feminino', 901492188)

#Chamada
print("Pessoa 1:")
pessoa1.apresentar()

print("\nAluno 1:")
aluno1.apresentar()

aluno1.set_matricula(881294109)
print("\nNova matrícula do aluno 1:", aluno1.get_matricula())
       
         
        
        