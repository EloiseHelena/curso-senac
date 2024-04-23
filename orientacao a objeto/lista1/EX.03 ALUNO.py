class Aluno:
     
   def __init__(self, nome, curso, matricula):
       self.nome = nome
       self.curso = curso
       self.matricula = matricula
       
   def get_nome(self):
    return self.nome   
       
   def get_curso(self):
    return self.curso

   def get_matricula(self):
    return self.matricula

   def set_nome(self, novo_nome):
     self.nome = novo_nome
     
   def set_curso(self, novo_curso):
     self.curso = novo_curso

   def set_matricula(self, nova_matricula):
     self.matricula = nova_matricula



#Imprime nome, curso e matrícula
aluno1 = Aluno('Eloise', 'ADS', 182300648)
print(f"Aluno: {aluno1.get_nome()}")

curso = Aluno('Eloise', 'ADS', 182300648)
print(f"Curso: {curso.get_curso()}")

matricula = Aluno('Eloise', 'ADS', 182300648)
print(f"Número da matrícula: {matricula.get_matricula()}\n")

#Imprime novo nome, novo curso e nova matrícula
aluno1.set_nome("Helena")
print(f"Novo nome de aluno: {aluno1.get_nome()}")

curso.set_curso("Ciência da Computação")
print(f"Novo curso: {curso.get_curso()}")

curso.set_matricula(648300182)
print(f"Novo número de matrícula: {matricula.get_matricula()}")