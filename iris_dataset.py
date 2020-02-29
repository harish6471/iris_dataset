from sklearn.datasets import load_iris
from urllib.request import urlretrieve
import pandas as pd
from pandas.plotting import scatter_matrix
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns


#iris = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris="https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"

urlretrieve(iris)
data=pd.read_csv(iris,sep=',')


sheets="Sheet1","Sheet2","Sheet3","Sheet4"



attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]



data.columns = attributes

df1=pd.DataFrame(data,columns=['sepal_length','sepal_width'])
df2=pd.DataFrame(data,columns=['petal_length','petal_width'])

# print(df1.head())
# print(df2.head())#print upto 5 rows 
# print(df.shape)#print (rows,colums)
# print(df.describe())

# print(df.groupby("class").size())

# df1.sort_values("sepal_length",axis=0,ascending=True,inplace=True,na_position='last')# axis=1 for column sorting
# #print(df1.head())
# # df2.sort_values("petal_length",axis=0,ascending=True,inplace=True,na_position='last')
# writer=pd.ExcelWriter("C:\\Users\\harish647\\Desktop\\iris.xlsx",engine='xlsxwriter')
# df1.to_excel(writer,sheet_name='Sheet1')
# df2.to_excel(writer,sheet_name='Sheet2')


# #print(df1.boxplot(by='sepal_length',column=['sepal_width'],grid=True))
# #df1.hist()#histogram plot
# #plt.show()#univarient plot

# tips=sns.load_dataset('iris')
# print(tips.head())

# sns.set_style("whitegrid")
# #sns.boxplot(x='sepal_length',y='sepal_width',hue='species',data=tips,palette='deep')#boxplot
# sns.despine()
# sns.set_context('poster',font_scale=2)#setFont

# sns.lmplot(x='sepal_length',y='sepal_width',size=2,data=tips)#regression plot


##multivarient plot

data.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)#whisker plot and box which is mainly for univarient
scatter_matrix(data)#scatter matrix plot how one effetced by other


plt.show()

#writer.save()
# wb=openpyxl.load_workbook("C:\\Users\\harish647\\Desktop\\iris.xlsx")
# print(wb.sheetnames())

#print(df)