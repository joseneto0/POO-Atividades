from ingresso import *
from cartao_mensagem import *
from funcionario import *

#teste ingressos
ingresso1 = Ingresso(10.0)
print("Ingresso Comum")
print(ingresso1.valor)
print()
ingresso2 = IngressoVIP(10.0, 5.0)
print("Ingresso VIP")
print(ingresso2.valor)
print()

#teste cartões
lista = []
lista.append(MensagemAniversario("Zezin"))
lista.append(MensagemDiaDosNamorados("Merys"))
lista.append(MensagemNatal("Deba"))
for i in lista:
    print(i.retornarMensagem("Naruto"))

print()
#teste funcionarios
print('Funcionário: ')
funcionario = Funcionario('Zezin', 1500)
print(funcionario.exibeDados)
funcionario.adicionaAumento(500)
print(funcionario.exibeDados)
print(funcionario.ganhoAnual)
print()

print('Assistente: ')
assistente = Assistente('Zefa', 1000, 1203102301)
print(assistente.exibeDados)
print()

print('Assistente Técnico: ')
tecnico = Tecnico('Merys', 3000, 12312313, 600)
print(tecnico.exibeDados)
print(tecnico.ganhoAnual)
print()

print('Assistente Administrativo: ')
adm = Administrativo('Oliver', 5000, 1023103, 'noite')
print(adm.exibeDados)
print(adm.ganhoAnual)