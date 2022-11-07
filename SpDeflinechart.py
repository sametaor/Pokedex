#Importing Pandas and Matplotlib for enabling following function
import pandas as pd
import matplotlib.pyplot as plt

pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#')

#Defining SpDef_line to be invoked in Main.py
def SpDef_line():
    plt.plot(pokedexdf.SpDef,color='#b08e2f',lw=1,ls=':',marker='s',markersize=2,markeredgecolor='k')
    plt.title("Special Defense rate of pokemons")
    plt.xlabel("Pokemon no.")
    plt.ylabel("Special Defense rate")
    plt.show()