identidade = input("Insira o seu n de B.I \n")
resultado = identidade.strip()
base_de_dados = {"005835741LA048":
                 {
                  "nome \n":"Tatiana Gomes \n",
                  "cursos": ["Python", "Desenvolvimento Web \n"],
                  "laptop": "PC-MEDIATECA 1"
                  },
                 "00590786LA045":
                 {
                  "nome":"Domingas Queta \n",
                  "cursos": ["Python", "Desenvolvimento Web \n"],
                  "laptop": "PC-MEDIATECA 2"
                  }
                 }

aluna = base_de_dados.get(resultado)

if aluna:
    print("Acesso permitido!\n", aluna)
else:
    print("BI:",identidade, "\nAcesso negado!",)
    print("Usuário não encontrado")
    






