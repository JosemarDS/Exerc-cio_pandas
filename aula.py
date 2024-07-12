import pandas as pd  
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import statistics as st


# O quanto o grau de instrução dos pais impacta no 
# desempenho do aluno

dados = pd.read_csv('dados.csv')
vendedor = dados['vendedor'].to_list()
valores = dados['vendas'].to_list()
V1 = np.array(vendedor)
v2 = np.array(valores)
# fig, grafico= plt.subplots()
plt.pie(valores, labels= vendedor)
plt.show()

