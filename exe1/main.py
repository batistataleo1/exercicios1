from pessoa import Pessoa 

p1 = Pessoa("João", 25, "Rua A, 123", "Masculino")
p2 = Pessoa("Maria", 30, "Rua B, 456", "Feminino")
p3 = Pessoa("Pedro", 35, "Rua C, 789", "Masculino")

print(f"Nome: {p1.getNome()}")
print(f"Idade: {p1.getIdade()}")
print(f"Endereço: {p1.getEndereco()}")
print(f"Sexo: {p1.getSexo()}")
print(f"Nome: {p2.getNome()}")
print(f"Idade: {p2.getIdade()}")
print(f"Endereço: {p2.getEndereco()}")
print(f"Sexo: {p2.getSexo()}")
print(f"Nome: {p3.getNome()}")
print(f"Idade: {p3.getIdade()}")
print(f"Endereço: {p3.getEndereco()}")
print(f"Sexo: {p3.getSexo()}")