from pais import País
paises = País("Brasil", "Brasilia", "20000000")
paises.adicionar_paises_fronteira("Colômbia")
paises.adicionar_paises_fronteira("Venezuela")
paises.adicionar_paises_fronteira("Paraguai")
paises.adicionar_paises_fronteira("Peru")
print(paises)