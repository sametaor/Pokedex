#Importing Pandas and Matplotlib for enabling following function
import pandas as pd
import matplotlib.pyplot as plt

pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#')

#Defining HP_line to be invoked in Main.py
def HP_line():
    plt.plot(pokedexdf.HP,color='g',lw=1,ls='--',marker='+',markersize=2,markeredgecolor='k')
    plt.title("HP of pokemons")
    plt.xlabel("Pokemon no.")
    plt.ylabel("Health")
    plt.show()