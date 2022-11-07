#Importing Pandas and Matplotlib for enabling following function

import pandas as pd
import matplotlib.pyplot as plt

pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#')
#Defining Def_line to be invoked in Main.py
def Defense_line():
    plt.plot(pokedexdf.Defense,color='y',lw=1,ls=':',marker=',',markersize=2,markeredgecolor='k')
    plt.title("Defense rate of pokemons")
    plt.xlabel("Pokemon no.")
    plt.ylabel("Defense rate")
    plt.show()