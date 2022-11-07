#Importing Pandas and Matplotlib for enabling following function
import matplotlib.pyplot as plt
import pandas as pd

pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#')
variants=["Grass","Fire","Water","Bug","Normal","Poison","Electric","Ground","Fairy","Fighting","Psychic","Rock","Ghost","Ice","Dragon","Steel","Dark","Flying"] #Defining set of Pokemon types/variants for following function

def Type_2():
    plt.title("Composition of Type 2 pokemons")
    Type2chart=plt.pie(pokedexdf['Type_2'].value_counts(),labels=variants,autopct="%1.1f%%",explode=[0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]) #Creating a pie chart which displays sectors based on value counts of values under Type_1 column, then labelling the sectors with variants list, followed by giving an explode effect of 0.2
    plt.show()