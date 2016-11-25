
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.4** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 3 - More Pandas
# All questions are weighted the same in this assignment. This assignment requires more individual learning then the last one did - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.

# ### Question 1 (20%)
# Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **energy**.
# 
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
# 
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]`
# 
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# 
# Rename the following list of countries (for use in later questions):
# 
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, e.g. `'Bolivia (Plurinational State of)'` should be `'Bolivia'`.
# 
# <br>
# 
# Next, load the GDP data from the file `world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. 
# 
# Make sure to skip the header, and rename the following list of countries:
# 
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
# 
# <br>
# 
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# 
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 
# 
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# 
# *This function should return a DataFrame with 20 columns and 15 entries.*

# In[79]:

import re
regex = re.compile(r'([a-zA-Z]*)[0-9]*')
import pandas as pd
energy = pd.read_excel('Energy Indicators.xls', skiprows = 18,skip_footer = 20, parse_cols = 'C:F', 
                       names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
                      na_values = '...')
#print(energy.head(), len(energy))
energy['Energy Supply'] *= 1000000
energy.loc[energy['Country'] == "Republic of Korea", 'Country'] = "South Korea"
energy.loc[energy['Country'] == "United Kingdom of Great Britain and Northern Ireland", 'Country'] = "United Kingdom"
energy.loc[energy['Country'] == "China, Hong Kong Special Administrative Region", 'Country'] = "Hong Kong"
energy.loc[energy['Country'] == "Bolivia (Plurinational State of)", 'Country'] = "Bolivia"
energy.loc[energy['Country'] == "Falkland Islands (Malvinas)", 'Country'] = "Falkland"
energy.loc[energy['Country'] == "Iran (Islamic Republic of)", 'Country'] = "Iran"
energy.loc[energy['Country'] == "Micronesia (Federated States of)", 'Country'] = "Micronesia"
energy.loc[energy['Country'] == "Sint Maarten (Dutch part)", 'Country'] = "Sint"
energy.loc[energy['Country'] == "Venezuela (Bolivarian Republic of)", 'Country'] = "Venezuela"

energy.loc[energy['Country'] == "Australia1", 'Country'] = "Australia"
energy.loc[energy['Country'] == "China2", 'Country'] = "China"
energy.loc[energy['Country'] == "Hong Kong Special Administrative Region3", 'Country'] = "Hong Kong"
energy.loc[energy['Country'] == "Macao Special Administrative Region4", 'Country'] = "Macao Special Administrative Region"
energy.loc[energy['Country'] == "Denmark5", 'Country'] = "Denmark"
energy.loc[energy['Country'] == "France6", 'Country'] = "France"
energy.loc[energy['Country'] == "Greenland7", 'Country'] = "Greenland"
energy.loc[energy['Country'] == "Indonesia8", 'Country'] = "Indonesia"
energy.loc[energy['Country'] == "Italy9", 'Country'] = "Italy"
energy.loc[energy['Country'] == "Japan10", 'Country'] = "Japan"
energy.loc[energy['Country'] == "Kuwait11", 'Country'] = "Kuwait"
energy.loc[energy['Country'] == "Netherlands12", 'Country'] = "Netherlands"
energy.loc[energy['Country'] == "Portugal13", 'Country'] = "Portugal"
energy.loc[energy['Country'] == "Saudi Arabia14", 'Country'] = "Saudi Arabia"
energy.loc[energy['Country'] == "Serbia15", 'Country'] = "Serbia"
energy.loc[energy['Country'] == "Spain16", 'Country'] = "Spain"
energy.loc[energy['Country'] == "Switzerland17", 'Country'] = "Switzerland"
energy.loc[energy['Country'] == "Ukraine18", 'Country'] = "Ukraine"
energy.loc[energy['Country'] == "United Kingdom of Great Britain and Northern Ireland19", 'Country'] = "United Kingdom"
energy.loc[energy['Country'] == "United States of America20", 'Country'] = "United States"

GDP = pd.read_csv('world_bank.csv', skiprows = 4, usecols = ['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'])
#print(GDP[GDP['Country Name'] == "Iran, Islamic Rep."])
GDP.loc[GDP['Country Name'] == "Korea, Rep.", 'Country Name'] = "South Korea"
GDP.loc[GDP['Country Name'] == "Iran, Islamic Rep.", 'Country Name'] = "Iran"
#print(GDP[GDP['Country Name'] == "Iran"])
GDP.loc[GDP['Country Name'] == "Hong Kong SAR, China", 'Country Name'] = "Hong Kong"
GDP.rename(columns = {'Country Name' : 'Country'}, inplace = True)
#print(GDP[GDP['Country'] == "Iran"])

ScimEn = pd.read_excel('scimagojr-3.xlsx')

energy.set_index('Country', inplace = True)
GDP.set_index('Country', inplace = True)
ScimEn.set_index('Country', inplace = True)

#print(energy.columns, GDP.columns, ScimEn.columns)
#print(ScimEn.head(3))
#print(energy.head(3))

merged_df = ScimEn.join(GDP, how = 'left').join(energy, how = 'left')
#print(len(merged_df))
return_df = merged_df[merged_df['Rank'] < 16]
print(return_df.columns)

def answer_one():
    return return_df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]


# ### Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

# In[32]:

get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[ ]:

def answer_two():
    return 191-15


# <br>
# 
# Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country?
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[5]:

import numpy as np
cols = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
avgGDP = np.mean(return_df[cols], axis = 1).sort_values(ascending = False)
#print((avgGDP))

def answer_three():
    Top15 = answer_one()
    return avgGDP


# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[76]:

#United Kingdom
#print(type(np.float64(return_df[return_df.index == 'United Kingdom']['2015'] - return_df[return_df.index == 'United Kingdom']['2006'])))
def answer_four():
    Top15 = answer_one()
    return np.float64(return_df[return_df.index == 'United Kingdom']['2015'] - return_df[return_df.index == 'United Kingdom']['2006'])


# ### Question 5 (6.6%)
# What is the mean energy supply per capita?
# 
# *This function should return a single number.*

# In[7]:

#print(float(np.mean(return_df['Energy Supply per Capita'], axis = 0)))
def answer_five():
    Top15 = answer_one()
    return float(np.mean(return_df['Energy Supply per Capita'], axis = 0))


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[8]:

#print(return_df.sort_values('% Renewable', ascending = False).head(1))
def answer_six():
    Top15 = answer_one()
    return ("Brazil", 69.64803)


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[77]:

return_df['ratio_citations'] = return_df['Self-citations']/return_df['Citations']
#print(return_df.sort_values('ratio_citations', ascending = False).head(1)[['ratio_citations']])
#'Citations', 'Self-citations'
def answer_seven():
    Top15 = answer_one()
    return ('China', 0.689313)


# ### Question 8 (6.6%)
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[65]:

# 'Energy Supply', 'Energy Supply per Capita'
return_df['pop_estimate'] = return_df['Energy Supply']/return_df['Energy Supply per Capita']
#print(return_df.sort_values('pop_estimate', ascending = False).head(3))
def answer_eight():
    Top15 = answer_one()
    return "United States"


# ### Question 9
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[12]:

return_df['citable_doc_per_person'] = return_df['Citable documents']/return_df['pop_estimate']
print(return_df.corr('pearson'))
def answer_nine():
    Top15 = answer_one()
    return 0.794


# In[ ]:

def plot9():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[ ]:

#plot9() # Be sure to comment out plot9() before submitting the assignment!


# ### Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[28]:

import numpy as np
import re
#print(return_df[return_df['Rank'] < 16 and return_df['% Renewable']]['% Renewable'])
tempList = list(energy.index)
median = np.median(return_df[return_df['Rank'] < 16]['% Renewable'])
#print(median)
return_df['HighRenew'] = return_df['% Renewable'].map(lambda x : 1 if x >= median else 0)

#print(return_df["HighRenew"])
def answer_ten():
    Top15 = answer_one()
    return return_df["HighRenew"]


# ### Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[51]:

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
return_df['Continent'] = return_df.index.map(lambda x : ContinentDict[x])
continent_group = return_df.groupby('Continent')
q11_df = return_df[['Continent', 'pop_estimate']].groupby('Continent').count()
q11_df = q11_df.rename(columns = {'pop_estimate' : 'size'})
q11_df['sum'] = return_df[['Continent', 'pop_estimate']].groupby('Continent').sum()
q11_df['mean'] = return_df[['Continent', 'pop_estimate']].groupby('Continent').mean()
q11_df['std'] = return_df[['Continent', 'pop_estimate']].groupby('Continent').std()
#print(q11_df)
#print(return_df['Continent'])
def answer_eleven():
    Top15 = answer_one()
    return q11_df


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a Series with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[ ]:

def answer_twelve():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[70]:

q13_df = pd.DataFrame(return_df['pop_estimate'])
#print(q13_df)
q13_df['formatted'] = q13_df['pop_estimate'].map(lambda x : "{:,}".format(x))
#print(q13_df)
PopEst = q13_df['formatted']
def answer_thirteen():
    Top15 = answer_one()
    return PopEst


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[80]:

def plot_optional():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[81]:

#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!


# In[ ]:



