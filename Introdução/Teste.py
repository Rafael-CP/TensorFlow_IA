import tensorflow
import numpy as np

print('Teste')
vect = [2,5,7]
print(max(vect))

array = np.asarray(vect) #adiciona mais funçoes
print(array.max()) #maior valor
print(array.argmax()) #posicao (indice) do maior valor

num = 3
op = array * num
print(op)

t = np.arange(1, 11, 0.5) #cria array

np.linspace(1, 20, 10) #espacamento linear que vai de 1 ate 20, com 10 elementos
#%%
np.random.randint(0, 101) #numeros randomicos inteiros de 0 a 100
#%%
np.random.seed(1)   #mantem o numero randomico gerado
np.random.randint(0,101)
#%%
np.random.randint(0,101, 3) #cria uma determinada quantidade de numeros aleatorios
#%%
np.random.randint(0,101, (3,3)) #cria matriz aleatoria