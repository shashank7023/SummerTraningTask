import pandas 
import numpy
import sklearn.linear_model import LinearRegression

db = pandas.read_csv('salary.csv')

x=db['YearsExperience'].values.reshape(30,1)
y=db['Salary']

model=LinearRegression
model.fit(x,y)

result=model.predict([[2.5]])

print(result)
