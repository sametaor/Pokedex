#import modules for project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import internal files and functions
from Type1piechart import Type_1
from Type2piechart import Type_2
from HPlinechart import HP_line
from Attacklinechart import Atk_line
from Defenselinechart import Defense_line
from SpAtklinechart import SpAtk_line
from SpDeflinechart import SpDef_line
from Speedlinechart import Speed
from Genpiechart import Generations


pokedexdf = pd.read_csv("pokemon_data.csv", index_col='#') #Accessing csv file to create Pandas DataFrame object and displaying it
print(pokedexdf)

name_full_input=str(input("Would you like to show the names of all the Pokemons?(yes/no) "))
if name_full_input=="yes":
    x=pd.Series(pokedexdf.Name)
    Pokemon_names=x.sort_values()
    print(Pokemon_names) #Creating a Pandas Series Object to display names of all pokemons in pokedexdf DataFrame

#Using imported functions to display respective charts for each non-index column from pokedexdf after taking suitable input from the user(as well as refining input from user in some cases)
Type_1_full_input=str(input("Would you like to show a Series consisting of all Type 1 variants along with a pie chart?(yes/no) "))
if Type_1_full_input=="yes":
    print(pokedexdf['Type_1'].value_counts())
    Type_1()

Type_2_full_input=str(input("Would you like to show a Series consisting of all Type 2 variants along with a pie chart?(yes/no) "))
if Type_2_full_input=="yes":
    print(pokedexdf['Type_2'].value_counts())
    Type_2()

HP_full_input=str(input("Would you like to view a line chart displaying HP of all Pokemons?(yes/no) "))
if HP_full_input=="yes":
    HP_filter_bool_input=str(input("Would you like to filter the HP by value?(yes/no) "))
    if HP_filter_bool_input=="yes":
        HP_filter_input=str(input("What comparison operator to be applied?(=/>/</>=/<=) "))
        if HP_filter_input=="=":
            HP_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'HP{HP_filter_input}{HP_filter_input}{HP_number_input}'))
        if HP_filter_input==">":
            HP_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'HP{HP_filter_input}{HP_number_input}'))
        if HP_filter_input=="<":
            HP_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'HP{HP_filter_input}{HP_number_input}'))
        if HP_filter_input==">=":
            HP_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'HP{HP_filter_input}{HP_number_input}'))
        if HP_filter_input=="<=":
            HP_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'HP{HP_filter_input}{HP_number_input}'))
    else:
        HP_line()

Atk_full_input=str(input("Would you like to view a line chart displaying Attack of all Pokemons?(yes/no) "))
if Atk_full_input=="yes":
    Atk_filter_bool_input=str(input("Would you like to filter the Attack by value?(yes/no)" ))
    if Atk_filter_bool_input=="yes":
        Atk_filter_input=str(input("What comparison operator to be applied?(=/>/</>=/<=)"))
        if Atk_filter_input=="=":
            Atk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Attack{Atk_filter_input}{Atk_filter_input}{Atk_number_input}'))
        if Atk_filter_input==">":
            Atk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Attack{Atk_filter_input}{Atk_number_input}'))
        if Atk_filter_input=="<":
            Atk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Attack{Atk_filter_input}{Atk_number_input}'))
        if Atk_filter_input==">=":
            Atk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Attack{Atk_filter_input}{Atk_number_input}'))
        if Atk_filter_input=="<=":
            Atk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Attack{Atk_filter_input}{Atk_number_input}'))
    else:
        Atk_line()

Defense_full_input=str(input("Would you like to view a line chart displaying Defense of all Pokemons?(yes/no) "))
if Defense_full_input=="yes":
    Defense_filter_bool_input=str(input("Would you like to filter the Attack by value?(yes/no)" ))
    if Defense_filter_bool_input=="yes":
        Defense_filter_input=str(input("What comparison operator to be applied?(=/>/</>=/<=)"))
        if Defense_filter_input=="=":
            Defense_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Defense{Defense_filter_input}{Defense_filter_input}{Defense_number_input}'))
        if Defense_filter_input==">":
            Defense_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Defense{Defense_filter_input}{Defense_number_input}'))
        if Defense_filter_input=="<":
            Defense_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Defense{Defense_filter_input}{Defense_number_input}'))
        if Defense_filter_input==">=":
            Defense_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Defense{Defense_filter_input}{Defense_number_input}'))
        if Defense_filter_input=="<=":
            Defense_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Defense{Defense_filter_input}{Defense_number_input}'))
    else:
        Defense_line()

SpAtk_full_input=str(input("Would you like to view a line chart displaying Special Attack of all Pokemons?(yes/no) "))
if SpAtk_full_input=="yes":
    SpAtk_filter_bool_input=str(input("Would you like to filter the Attack by value?(yes/no)" ))
    if SpAtk_filter_bool_input=="yes":
        SpAtk_filter_input=str(input("What comparison operator to be applied?(=/>/</>=/<=)"))
        if SpAtk_filter_input=="=":
            SpAtk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpAtk{SpAtk_filter_input}{SpAtk_filter_input}{SpAtk_number_input}'))
        if SpAtk_filter_input==">":
            SpAtk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpAtk{SpAtk_filter_input}{SpAtk_number_input}'))
        if SpAtk_filter_input=="<":
            SpAtk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpAtk{SpAtk_filter_input}{SpAtk_number_input}'))
        if SpAtk_filter_input==">=":
            SpAtk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpAtk{SpAtk_filter_input}{SpAtk_number_input}'))
        if SpAtk_filter_input=="<=":
            SpAtk_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpAtk{SpAtk_filter_input}{SpAtk_number_input}'))
    else:
        SpAtk_line()

SpDef_full_input=str(input("Would you like to view a line chart displaying Special Defense of all Pokemons?(yes/no) "))
if SpDef_full_input=="yes":
    SpDef_filter_bool_input=str(input("Would you like to filter the Attack by value?(yes/no)" ))
    if SpDef_filter_bool_input=="yes":
        SpDef_filter_input=str(input("What comparison operator to be applied?(=/>/</>=/<=)"))
        if SpDef_filter_input=="=":
            SpDef_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpDef{SpDef_filter_input}{SpDef_filter_input}{SpDef_number_input}'))
        if SpDef_filter_input==">":
            SpDef_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpDef{SpDef_filter_input}{SpDef_number_input}'))
        if SpDef_filter_input=="<":
            SpDef_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpDef{SpDef_filter_input}{SpDef_number_input}'))
        if SpDef_filter_input==">=":
            SpDef_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpDef{SpDef_filter_input}{SpDef_number_input}'))
        if SpDef_filter_input=="<=":
            SpDef_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'SpDef{SpDef_filter_input}{SpDef_number_input}'))
    else:
        SpDef_line()

Speed_full_input=str(input("Would you like to view a line chart displaying Speed of all Pokemons?(yes/no) "))
if Speed_full_input=="yes":
    Speed_filter_bool_input=str(input("Would you like to filter the Attack by value?(yes/no)" ))
    if Speed_filter_bool_input=="yes":
        Speed_filter_input=str(input("What comparison operator to be applied?(=/>/</>=/<=)"))
        if Speed_filter_input=="=":
            Speed_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Speed{Speed_filter_input}{Speed_filter_input}{Speed_number_input}'))
        if Speed_filter_input==">":
            Speed_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Speed{Speed_filter_input}{Speed_number_input}'))
        if Speed_filter_input=="<":
            Speed_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Speed{Speed_filter_input}{Speed_number_input}'))
        if Speed_filter_input==">=":
            Speed_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Speed{Speed_filter_input}{Speed_number_input}'))
        if Speed_filter_input=="<=":
            Speed_number_input=int(input("What is the number to be pitted against? "))
            print(pokedexdf.query(f'Speed{Speed_filter_input}{Speed_number_input}'))
    else:
        Speed()

Gen_full_input=str(input("Would you like to view a chart showing the Generation distribution of Pokemons in a pie chart?(yes/no) "))
if Gen_full_input=="yes":
    Generations()

#Showing only Water type Pokemons:
print("Type 1 Water Pokemons:")
print(pokedexdf.query('Type_1=="Water"'))
print("\nType 2 Water Pokemons:")
print(pokedexdf.query('Type_2=="Water"'))

#Showing Pokemons having more than 100 :
print("Pokemons with more than 100 HP:")
print(pokedexdf.query('HP>100'))

#Showing bar graph of Fire Pokemons:
pokedexdf2=pokedexdf[["Type_1","Type_2"]].values=="Fire"
firepokedex=pokedexdf.loc[pokedexdf2]
plt.bar(firepokedex.Attack, firepokedex.Defense,color='r',label="Normal")
plt.bar(firepokedex.SpAtk, firepokedex.SpDef,color='g',label="Special")
plt.bar(firepokedex.HP, firepokedex.Speed,color='b',label="HP/Speed")
plt.title("Ratings for Fire Pokemons for different properties")
plt.xlabel("Atk/SpAtk/HP")
plt.ylabel("Def/SpDef/Speed")
plt.legend(loc="upper left")
plt.show()

#Showing max Attack Power in Pokemons:
Max_Atk=pokedexdf['Attack'].max()
print(f"The Maximum Attack Power in Pokemons is: {Max_Atk}")