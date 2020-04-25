# -*- coding: utf-8 -*-

import pandas as pd

import seaborn as sns

sns.set()

topeco = pd.read_csv('topeco.csv', index_col = 0)

#used to print the entire dataset
print(topeco)

#describes the basic statistical properties of numerical attributes
print('describes statistical properties of numerical attributes')
print(topeco.describe())

#sorts the countries in descending order by population
print('')
print('Countries sorted by population')
print(topeco.sort_values(by='population',ascending=False))

#sorts the countries in descending order by density and per capita income
print('')
print('Countries sorted by population density and per capita income')
print(topeco.sort_values(by=['density','pci'],ascending=[True,False]))
print(topeco.sort_values(by=['density','pci'],ascending=[False,True]))

#states what percent of countries are from which continent
print('')
print('Country participation by continent')
print((topeco['continent'].value_counts(normalize=True))*100)

#calculates the mean per capita income of developed countries
print('')
print('Mean per capita income of developed countries')
print(topeco[topeco['developed']=='yes']['pci'].mean())

#calculates the mean per capita income of developing countries
print('')
print('Mean per capita income of developing countries')
print(topeco[topeco['developed']=='no']['pci'].mean())

#columns_to_show = ['density', 'population', 
                   #'pci']
#states the statistical properties of density, population and per capita income of developed countries

print('')
print('Percentiles of population')
print(topeco.groupby(['developed'])['population'].describe(percentiles=[]))
print('')
print('Percentiles of per capita income')
print(topeco.groupby(['developed'])['pci'].describe(percentiles=[]))


#attempts to establish a relation using relplot
#sns.relplot(x='density',y='pci',data=topeco) #between density and per capita income
#sns.relplot(x='area',y='pci',data=topeco) #between area and per capita income

#states 5 point summary of per capita income, density and area using box and whisker plot
#sns.boxplot(x = 'pci', data = topeco)
#sns.boxplot(x = 'density', data = topeco)
#sns.boxplot(x = 'area', data = topeco)

#states whether there us high chance of country being UN Security Council member if developed

sns.countplot(x='developed', hue='UNSEC member', data=topeco) 

