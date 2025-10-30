import openpyxl

wb = openpyxl.load_workbook('example3.xlsx')
sheet = wb['Sheet1'] 

print(sheet['A1'].value)

c = sheet['B1']
print(f'Row {c.row}, Column {c.column} is {c.value}')
print(f'Cell {c.coordinate} is {c.value}')

print(sheet['C1'].value)