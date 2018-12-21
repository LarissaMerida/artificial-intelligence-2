import math
import queue
'''
In:
3
2
0 1 
1 1
0 1
'''
q_species , q_features, matrix , tree = 0, 0, [], []
DEBUG = False
USER = False

def calculates_cost():
	global q_species, matrix
	amount = []
	for i in range(q_species):
		 amount.append([sum(matrix[i]), i])
	amount.sort()

	if(DEBUG):
		print(amount)
	return amount

def search_amount(vector, size, element):
  start, end= 0, size

  for i in range(len(vector)):
  	if(vector[i][1] == element):
  		return i

def generate_search_graph(amount):
	global matrix
	graph = [[]]*(q_species*q_features)
	for i in range(q_features*q_species):
		graph[i] = []
	
	for i in range(q_species):
		k = search_amount(amount, len(amount), i)
		graph[0].append([amount[k][0], matrix[i], i+1])

		for j in range(q_species):
			if(not j == i):
				graph[j+1].append([amount[k][0], matrix[i], i+1])
				#print(j+1, i+1, matrix[i], graph[j+1][i+1], amount[i][1]+1)
	graph[0].sort()
	if(DEBUG):
		print(graph)
	return graph

def check_constraints(node_previous, node_current):
	#print(node_previous, node_current)
	sum = 0
	for i in range(len(node_previous[1])):
		if(node_previous[1][i] == 1 and node_previous[1][i] == node_current[1][i]):
			sum += 1
	if(sum == node_previous[0]):
		return True
	return False

def generate_search_tree(node_previous, node_current):
	global tree
	#print(node_previous[2], node_current)
	tree[ node_previous[2] ].append([node_current[2] ,node_current[1]])
	
def cost_sensitive_search(graph, fr):
	global q_species, q_features, matrix

	vstd, tree = [], []*(q_features*q_species)
	for i in range(q_features*q_species):
		vstd.append(False)
	vstd[fr], ant = True, 0
	q = queue.PriorityQueue()
	q.put( [0, [0], fr] )

	while not q.empty():
		u = q.get()
		#print( "Vértice " + str(u[2]))

		for w in graph[ int(u[2]) ]:
			if (ant == 0 or ant == w[0]) and vstd[ int(w[2]) ] == False :
				if(w[0] > 0 and check_constraints(u, w)):
					ant = w[0]
					vstd[ int(w[2]) ] = True
					generate_search_tree(u, w)
					q.put(w)

			if not u[2]== 0  and vstd[ int(w[2]) ] == False :
				if(w[0] > 0 and check_constraints(u, w)):
					ant = w[0]
					vstd[ int(w[2]) ] = True
					generate_search_tree(u, w)
					q.put(w)

def B(specie):
	global tree
	found = 0
	for i in range(len(tree)):
		for j in range(len(tree[i])):
			if(tree[i][j][0] == specie):
				print("B(%d) =" %specie, tree[i][j][1],";" )
				found = 1
				break;
		if( found == 1):
			break;

def print_out():
	global tree
	print("----------------------------------")
	print("Phylogenetic tree F = (X, Y, A, B)")
	print("X (Species):", [ x for x in range(q_species)])
	print("Y (features):",[x for x in range(q_features)])
	print()
	for i in range(len(tree)):
		if( not tree[i] == []):
			for j  in tree[i]:
				print(i , "generated", j[0])
	print()
	for i in range(q_species):
		B(i+1)

if(USER):
	print('Quantity of species:')
q_species = int(input())

if(USER):
	print('Number of features:')
q_features = int((input()))

matrix = [-1]*(q_species)
for i in range(q_species):
	if(USER):
		print('Type %d features on the same line:' %q_features)

	line = [int(x) for x in input().split()]
	matrix[i] = line

if(DEBUG):
	print(q_features, q_species)
	print(matrix)

amount = calculates_cost()
graph = generate_search_graph(amount)

tree = [[]]*(q_species+1)
for i in range(q_species+1):
	tree[i] = []

cost_sensitive_search(graph, 0)
print_out()