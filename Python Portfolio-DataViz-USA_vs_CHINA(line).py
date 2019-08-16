import matplotlib.pyplot as plt
#compare America and China's gross domestic product(gdp) over time
#visualize data using line chart
def main ():
     
     input_file = open('gdp2.txt', 'r')

     records = input_file.readlines()
     year_list = []
     usa_list = []
     china_list = []

     for each_record in records:
        each_record = each_record.rstrip('\n')
        values = each_record.split()
        year = int (values[0])
        year_list.append(year)
        usa = float (values[1])
        usa_list.append(usa)
        china = float (values [2])
        china_list.append(china)

     input_file.close()
     

     plt.plot (year_list,usa_list, marker='o', label = 'USA')
     plt.plot (year_list,china_list , marker='o', label = 'CHINA')

     plt.xlim (xmin = 2008 , xmax= 2017)
    
     plt.title ('USA vs CHINA GDP')

     plt.xlabel ('Year')
     plt.ylabel ('GDP Amount (trillions)')

     plt.legend()
     plt.grid (True)

     plt.show()
    
main()
    
        
