user_url = []
user_nick = []
user_curso = []
user_univ = []

nomearq = raw_input("Nome do arquivo CVS: ")

arquivo = open(nomearq, "r")

n_users = 0;
for linha in arquivo:
	temp = linha.split(",", 4)
	user_url.append(temp[0]);
	user_nick.append(temp[1]);
	user_curso.append(temp[2]);
	user_univ.append(temp[3]);
	n_users = n_users + 1

arquivo_out = open("esse_arquivo_golden.txt", "w")

for i in range(n_users):
	arquivo_out.write(" :seta: [url="+str(user_url[i])+"]"+str(user_nick[i])+"[/url] - "+str(user_curso[i])+" - "+str(user_univ[i]))
	print(" :seta: [url="+str(user_url[i])+"]"+str(user_nick[i])+"[/url] - "+str(user_curso[i])+" - "+str(user_univ[i]))

arquivo.close()
arquivo_out.close()
