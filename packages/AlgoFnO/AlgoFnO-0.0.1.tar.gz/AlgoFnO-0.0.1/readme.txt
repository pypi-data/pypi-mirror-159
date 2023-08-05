This library can make Derivative Analysis easy for the F&O stocks listed in Indian Stock Market.
It takes in input as the location of the folder where the Bhav Copy is stored for Cash Market and F&O Market.

And then it within the same folder can create the csv files for F&O Bhav copy analysis.
It shows the cumulative OI and cumulative OI change as well as in percentage.

The sample code is as below:

from AlgoFnO import *
list = ['RELIANCE','TCS','INFY']
a = BhavCopyAnalysis()
print(a.doAnalysis("/Users/<username>/Desktop/AlgoFnO Sample Data",list))

Using the above code basically we pass comma separated list of stocks and the location of the folder where the files are stored.
