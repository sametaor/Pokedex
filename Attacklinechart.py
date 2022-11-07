#Importing Pandas and Matplotlib for enabling following function
import pandas as pd
import matplotlib.pyplot as plt

pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#')
#Defining Atk_line to be invoked in Main.py
def Atk_line():
    plt.plot(pokedexdf.Attack,color='r',lw=1,marker='x',markersize=2, markeredgecolor='k')
    plt.title("Attack rate of pokemons")
    plt.xlabel("Pokemon no.")
    plt.ylabel("Attack rate")
    plt.show()