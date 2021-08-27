class Funcionario:
  def __init__(self, nome):
    self.nome = nome
    
  def registrar_horas(self,horas):
    print('Horas registradas...')

  def mostrar_tarefas(self):
    print('Fez muita coisa...')


class Caelum(Funcionario):
  def mostrar_tarefas(self):
      print('Fez muita coisa, Caelumer')

  def busca_curso_do_mes(self, mes=None):
    print(f'Mostrando cursos - {mes}' if mes else 'Mostrando curso desse mês')

class Alura(Funcionario):
  def mostrar_tarefas(self):
    print('Fez muita coisa, Alurete!')

    
  def busca_perguntas_sem_resposta(self):
    print('Mostrando perguntas não repondidas do fórum')


class Hipster:
  def __str__(self):
    return f'Hipster, {self.nome}'

class Junior(Alura):
  pass

class Pleno(Alura, Caelum):
  pass

class Senior(Alura, Caelum, Hipster):
  pass

jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

print('-----------------------')

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_curso_do_mes()

print('-----------------------')

carlos = Senior('Carlos')
print(carlos)