from aluno import Aluno
zezin = Aluno(200231231, "Zezin")
for i in range(3):
    zezin.adicionar_notas(float(input(f"Digite sua {i+1}° nota: ")))
print(zezin.matricula)
print(zezin.media())