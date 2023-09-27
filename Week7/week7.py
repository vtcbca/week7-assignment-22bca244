import csv
import pandas as pd

with open('C:\\22bca244\\python\\prod_sell.csv','w',newline='')as f:
    obj1=csv.writer(f)
    col=['Prod_No', 'Prod_Name',' Jan','Feb','Mar','Apr','May','Jun']
    obj1.writerow(col)
    
with open('C:\\22bca244\\python\\prod_sell.csv','a',newline='')as cf:
    obj1=csv.writer(cf)
    list=[]
    for i in range(6):
        Prod_No=int(input("Enter product number:"))
        Prod_Name=input("Enter Product Name:")
        Jan=int(input("Enter product sales in January:"))
        Feb=int(input("Enter product sales in February:"))
        Mar=int(input("Enter product sales in March:"))
        Apr=int(input("Enter product sales in APril:"))
        May=int(input("Enter product sales in May:"))
        Jun=int(input("Enter product sales in June:"))
        tup=( Prod_No,Prod_Name,Jan,Feb,Mar,Apr,May,Jun)
        list.append(tup)
    obj1.writerows(list)


# 2. Create dataframe
df=pd.read_csv('C:\\22bca244\\python\\prod_sell.csv')
df

#3.Change Column Name Product No, Product Name, January, February, March, April, May,June:
df.rename(columns={'Prod_No':'Product No','Prod_Name':'Product Name',' Jan':'January','Feb':'February','Mar':'March','Apr':'April','May':'May','Jun':'June'},inplace=True)
df

#4.Add column Total Sell to count total of all month and Average Sell:
total_sell=df['January']+df['February']+df['March']+df['April']+df['May']+df['June']
df['Total']=total_sell
avg_sell=df['Total']/6
df['Average']=avg_sell
df

#7.Print first 5 row:
df.head()

#8.Print Last 5 row:
df.tail()

#9.Print row 6 to 10:
df.loc[5:9]

#10.Print only product name:
print(df["Product Name"])

#11.Print sell of January month with product id and product name:
print(df[["Product No","Product Name","January"]])

#12.Print only those product id , product name where january sell is > 5000 and  and February sell is >8000")      February sell is >8000")
print(df[(df["January"]>5000)& (df["February"]>8000)][["Product No","Product Name"]])

#13.Print record in sorting order of Product name:
df["Product Name"].sort_values()

#14.Display only odd index number column record:
df.iloc[1::2]

#15.Display alternate row:-
df.iloc[::2]



