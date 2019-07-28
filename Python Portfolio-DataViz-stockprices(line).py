import matplotlib.pyplot as plt
#Google-Amazon-Microsoft stockprices over the course of several days
#read data from file
#clean data
#visualize data using matplot library
def main():

    infile = open('stockPrices1.txt','r')

    records = infile.readlines()
    yearList = []
    googleList = []
    amazonList = []
    microsoftList = []
      

    for eachr in records:
        eachr = eachr.rstrip('\n')
        values = eachr.split()
        year = values[0]
        yearList.append(year)
        google = (float(values[1]))
        googleList.append(google)
        amazon = (float(values[2]))
        amazonList.append(amazon)
        microsoft = (float(values[3]))
        microsoftList.append(microsoft)

    infile.close()

    plt.title ('Google-Amazon-Microsoft Stockprices')
    plt.xlabel ('YEAR')
    plt.ylabel ('STOCKPRICE')
    

    plt.plot(yearList, googleList,marker = 'o', label = 'Google')
    plt.plot(yearList, amazonList,marker = 'o' ,label = 'Amazon')
    plt.plot(yearList, microsoftList,marker = 'o', label = 'Microsoft')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid (True)
    

    plt.show()

main()
    
