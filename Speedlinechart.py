#Importing Pandas and Matplotlib for enabling following function
import pandas as pd
import matplotlib.pyplot as plt

pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#')

#Defining Speed to be invoked in Main.py
def Speed():
    plt.plot(pokedexdf.Speed,color='c',lw=1,marker='>',markersize=2,markeredgecolor='k')
    plt.title("Speed of pokemons")
    plt.xlabel("Pokemon no.")
    plt.ylabel("Speed")
    plt.show()