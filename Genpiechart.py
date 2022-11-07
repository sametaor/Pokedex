#Importing Pandas and Matplotlib for enabling following function
import matplotlib.pyplot as plt
import pandas as pd

pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#')
Gens=[1,2,3,4,5,6]

def Generations():
    Type1chart=plt.pie(pokedexdf['Generation'].value_counts(),labels=Gens,autopct="%1.1f%%",explode=[0.1,0.1,0.1,0.1,0.1,0.1])
    plt.title("Composition of Generations of pokemons")
    plt.show()