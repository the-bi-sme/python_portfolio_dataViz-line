import matplotlib.pyplot as plt
#Google-Amazon-Microsoft stockprices over the course of several days
#read data from file
#clean data
#visualize data using matplot library
def main():

    in_file = open('stockPrices1.txt','r')

    records = in_file.readlines()
    year_list = []
    google_list = []
    amazon_list = []
    microsoft_list = []
      

    for each_record in records:
        each_record = each_record.rstrip('\n')
        values = each_record.split()
        year = values[0]
        year_list.append(year)
        google = (float(values[1]))
        google_list.append(google)
        amazon = (float(values[2]))
        amazon_list.append(amazon)
        microsoft = (float(values[3]))
        microsoft_list.append(microsoft)

    in_file.close()

    plt.title ('Google-Amazon-Microsoft Stockprices')
    plt.xlabel ('YEAR')
    plt.ylabel ('STOCKPRICE')
    

    plt.plot(year_list, google_list,marker = 'o', label = 'Google')
    plt.plot(year_list, amazon_list,marker = 'o' ,label = 'Amazon')
    plt.plot(year_list, microsoft_list,marker = 'o', label = 'Microsoft')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid (True)
    

    plt.show()

main()
    
