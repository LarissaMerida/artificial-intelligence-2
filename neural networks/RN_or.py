def regraAvaliacao(u):
	if(u > 0):
		return 1
	return 0

def regraPropagacao(entrada, pesos):
	u = 0
	for i in range(len(entrada)):
		u += entrada[i] * pesos[i]
	
	return regraAvaliacao(u)

def atualizarPesos(n, erro, entrada,pesos):
	for i in range(len(entrada)):
		pesos[i] = (pesos[i] + n*erro*entrada[i])

def iniciarPesosZero(pesos, amount_rn):
	for i in range(amount_rn):
		pesos.append(0)

print("Digite a quantidade de variaveis:")
amount_rn = int(input())
print("Digite a quantidade de entradas:")
amount = int(input())
ent, out= [], []


for i in range(amount):
	print("Digite as variaveis em binario da operacao ", i)
	line = [int(x) for x in input().split()]
	line.append(1)
	ent.append(line)
	
for i in range(amount):
	print("Digite a saída esperada da operacao ", i)
	out.append(int(input()))

amount_rn += 1
pesos = []
iniciarPesosZero(pesos, amount_rn)


n = 0.5
parar = 0
cont = 0
ciclo = 1
while(not parar == 1):
	print("-------- CICLO: " , ciclo)
	cont = 0
	for i in range(amount):
		print()
		print("Entrada " , i+1)
		saida = regraPropagacao(ent[i],pesos)
		erro = out[i] - saida
		print("erro =", erro)
		if(not erro == 0):
			atualizarPesos(n, erro, ent[i], pesos)
		else:
			cont+=1
	if(cont == amount ):
		parar = 1
		print("parando.....")
		print()
	ciclo += 1

print("------ SAIDA -------")

print("-> Pesos")
for i in range(len(pesos)-1):
	print(" Entrada " , i+1, " tem peso: ", pesos[i])

line = []
for i in range(len(ent)):
	for j in range(len(ent[i])-1):
		line.append(ent[i][j])
	ent[i] = line
	line = []

print()
print("-> Operacao or")
for i in range(len(out)):
	print(" " , ent[i], "resulta : ", out[i])

	
	
