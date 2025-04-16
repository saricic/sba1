import pandas as pd
import numpy as np

df = pd.read_excel("SalarySheet.xlsx")
print(df)
print(f"----------------------------------------------")

# TASK 1
print(f"length of rows : {len(df)}")
print(f"----------------------------------------------")
#Task2
print(df["Salary"].mean())

#Task3

salariesHR = df[df['Department'] == "HR"]['Salary']
salariesMarketing = df[df['Department'] == "Marketing"]['Salary']
salariesSales = df[df['Department'] == "Sales"]['Salary']
salariesFinance = df[df['Department'] == "Finance"]['Salary']
salariesSd = df[df['Department'] == "Software Development"]['Salary']
print(f"----------------------------------------------")
print(f"Hr average salary : {salariesHR.mean()}")
print(f"Marketing average salary : {salariesMarketing.mean()}")
print(f"Sales average salary : {salariesSales.mean()}")
print(f"Finance average salary : {salariesFinance.mean()}")
print(f"Software Development average salary : {salariesSd.mean()}")
print(f"----------------------------------------------")

# Task 4

salariesJun = df[df['Title']== 'Junior']['Salary'].mean()
salariesSen = df[df['Title']== 'Senior']['Salary'].mean()
salariesMid = df[df['Title']== 'Mid']['Salary'].mean()
salariesC = df[df['Title']== 'C-level']['Salary'].mean()
salariesMidS = df[df['Title']== 'Mid-Senior']['Salary'].mean()
print(f'juiniyor : {salariesJun}, mid : {salariesMid}, C-level : {salariesC}, Mid Seniyor : {salariesMidS}')

print(f"----------------------------------------------")
#task5
print(f"Average senior salary: {salariesSen}, Average junior salary: {salariesJun}")
print( f" Difference between junior and Senior salaries : {((salariesSen/salariesJun)-1)*100} %")

print(f"----------------------------------------------")

#Task 6
salariesSdSen = df[(df['Department'] == 'Software Development') & (df['Title'] == 'Senior')]['Salary'].mean()
salariesSdJun = df[(df['Department'] == 'Software Development') & (df['Title'] == 'Junior')]['Salary'].mean()


print(f"Average salary Jun Software Developer : {salariesSdJun}, Average salaray Senior Software Developer : {salariesSdSen}")


#Task 7

salariesFinanceCL = df[(df['Department'] == 'Finance') & (df['Title'] == 'C-level')]['Salary'].mean()
print(f"----------------------------------------------")
salariesFinanceMS = df[(df['Department'] == 'Finance') & (df['Title'] == 'Mid-Senior')]['Salary'].mean()

print(f"Average salary C-Level finance dep. worker {salariesFinanceCL},", f"Average salary Mid-Senior finance dep. worker {salariesFinanceMS}")
print(f"----------------------------------------------")


#Task 8
workersSdC = df[(df['Department'] == 'Software Development') & (df['Title'] == 'C-level')]
workersMarketing = df[df['Department'] == 'Marketing']

print(f" Num of C-level software dev workers {len(workersSdC)}, Num of Marketing workers {len(workersMarketing)}. 3 times more marketing workers")
