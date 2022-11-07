#Importing Pandas and Matplotlib for enabling following function
import pandas as pd
import matplotlib.pyplot as plt

pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#')

#Defining SpAtk_line to be invoked in Main.py
def SpAtk_line():
    plt.plot(pokedexdf.SpAtk,color='orange',lw=1,ls='-.',marker='D',markersize=2,markeredgecolor='k')
    plt.title("Special Attack rate of pokemons")
    plt.xlabel("Pokemon no.")
    plt.ylabel("Special Attack rate")
    plt.show()