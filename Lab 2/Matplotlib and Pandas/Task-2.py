#Task 2
import matplotlib.pyplot as plt
labels=['Mortgage','Repairs','Food','Liabilities']
percent=[51.72,10.34,17.24,20.69]
fig,a=plt.subplots(figsize=(10,7))
explode = (0.1, 0.1, 0.1,0.1)
a.pie(percent,labels=labels,startangle=90,autopct='%.2f%%',shadow=True,explode=explode)
plt.title("Household Expenses")
plt.show()