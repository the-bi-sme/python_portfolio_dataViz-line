import matplotlib.pyplot as plt
#compare America and China's gross domestic product(gdp) over time
#visualize data using line chart
def main ():
     
     inputFile = open('gdp2.txt', 'r')

     records = inputFile.readlines()
     yearList = []
     usaList = []
     chinaList = []

     for eachRecord in records:
        eachRecord = eachRecord.rstrip('\n')
        values = eachRecord.split()
        year = int (values[0])
        yearList.append(year)
        usa = float (values[1])
        usaList.append(usa)
        china = float (values [2])
        chinaList.append(china)

     inputFile.close()
     

     plt.plot (yearList,usaList, marker='o', label = 'USA')
     plt.plot (yearList, chinaList ,marker='o', label = 'CHINA')

     plt.xlim (xmin = 2008 , xmax= 2017)
    
     plt.title ('USA vs CHINA GDP')

     plt.xlabel ('Year')
     plt.ylabel ('GDP Amount (trillions)')

     plt.legend()
     plt.grid (True)

     plt.show()
    
main()
    
        
