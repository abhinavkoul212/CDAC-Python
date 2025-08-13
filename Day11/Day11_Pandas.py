import pandas as pd

#soul of pandas is to work with dataframes and series
#dataframes is a table with rows and columns
#series is a single column of a dataframe

#creating a dataframe
df = pd.DataFrame({
    'Name': ['John', 'Smith', 'Paul'],
    'Age': [23, 34, 45],
    'City': ['New York', 'Los Angeles', 'Miami']
})

print(df)

#creating a series
s = pd.Series([1, 2, 3, 4, 5])

print(s)

#reverse a series
print(s[::-1])
#creating a series with index
t = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(t)

#loc and iloc: loc is used to access a group of rows and columns by labels or a boolean array, iloc is used to access a group of rows and columns by integer position
print(t.loc['b'])
print(t.iloc[3])
# print(t[0])
# print(t['a'])

#creating a dataframe

emp = {
    'Name': ['John', 'Smith', 'Paul'],
    'Age': [23, 34, 45],
    'City': ['New York', 'Los Angeles', 'Miami']
}

df2 = pd.DataFrame(emp, index=['a', 'b', 'c'])
print(df2)

#accessing a column
print(df2['Name'])

#accessing a row
print(df2.iloc[1])
print()
#accessing a row
print(df2.loc['b'])
print()
#accessing a cell
print(df2.iloc[1, 1])

#accessing a cell
print(df2.iloc[1]['Name'])
print()
s2 = pd.Series(emp)
print(s2)

