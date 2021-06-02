import matplotlib.pyplot as plt
year = [2006, 2007,	2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
eft = [7, 11, 32, 65, 67, 70, 87, 132, 185,	213,244, 251, 265, 276]
susy = [524, 436, 658, 729,	666, 784, 818, 712, 617, 674, 477, 434,	368, 296]
plt.plot(year, eft)
plt.plot(year, susy)
plt.title('EFT vs. SUSY')
plt.xlabel('Year')
plt.ylabel('Number of papers per month')
plt.show()