class Pessoa:
  def __init__(self, nome, idade, endereco, sexo):
      self.nome = nome
      self.idade = idade
      self.endereco = endereco
      self.sexo = sexo
      
  def setNome(self, nome):
      self.nome = nome
  def setIdade(self, idade):
      self.idade = idade
  def setEndereco(self, endereco):
      self.endereco = endereco
  def setSexo(self, sexo):
      self.sexo = sexo
  def getNome(self): 
      return self.nome
  def getIdade(self):
      return self.idade
  def getEndereco(self):
      return self.endereco
  def getSexo(self):
      return self.sexo 