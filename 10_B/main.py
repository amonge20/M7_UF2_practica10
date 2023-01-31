import matplotlib.pyplot as plt

# Datos ficticios para las funciones
data_1 = [20, 30, 40, 10]
data_2 = [10, 20, 30, 40]
data_3 = [30, 10, 40, 20]

# Funciones que devuelven los datos
def func_1():
	return data_1

def func_2():
	return data_2

def func_3():
	return data_3

# Función principal que llama a las funciones y muestra las gráficas circulares
def main():
	data_1 = func_1()
	data_2 = func_2()
	data_3 = func_3()

	# Crear gráficas circulares
	fig, ax = plt.subplots(1, 3, figsize=(15, 5))
	ax[0].pie(data_1, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
	ax[0].set_title('Gráfica circular para función 1')
	ax[1].pie(data_2, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
	ax[1].set_title('Gráfica circular para función 2')
	ax[2].pie(data_3, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
	ax[2].set_title('Gráfica circular para función 3')

	# Mostrar gráficas
	plt.show()

if __name__ == '__main__':
	main()


