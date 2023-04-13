
import csv             
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Step One
    fileCSV = open('Data.csv', mode = 'r');
    fCSV = csv.reader(fileCSV)
    
    yearInfo = {}
    x = []
    y = []

    with open('stats.txt', mode = 'w') as f: # step two 

        for i, line in enumerate(fCSV):
            print(line)             # Printing CSV file contents         
            if i == 0:
                continue
            year = 0
            total = 0
            for index, cell in enumerate(line):
                if index == 0:
                    year = int(cell)
                    yearInfo[year] = []
                else:
                    yearInfo[year].append(int(cell))
                    total += int(cell)

            x.append(year)
            y.append(total)
            f.write(str(year) + ": " + str(total) + '\n')
    
    # Step Three
    plt.figure(1)
    plt.bar(x, y)
    plt.title("Yearly Sale Totals") # Writing plot title
    plt.xlabel("Year")      # Writing x-axis label
    plt.ylabel("Quantity Sold")  # Writing y-axis label

    plt.show()
    

    # Step 4
    a = 0 # sales from the first 6 months of 2022
    for index, value in enumerate(yearInfo[2022]):
        if index < 6:
            a += value
    b = 0 # sales from the first 6 months of 2021
    for index, value in enumerate(yearInfo[2021]):
        if index < 6:
            b += value
    sgr = (a-b)/a

    l6m = []
    for i in range(6):
        c = yearInfo[2021][i+6]
        l6m.append(c+(c*sgr))

    with open('stats.txt', mode = 'a') as f: # step two 
        f.write("Calculate Sales Growth Rate for the first 6 Months of 2021: " + str(sgr)+'\n')
        f.write("Estimated Sales for the last 6 months of 2022" + str(l6m) +'\n')

    x = ['J', 'A', 'S', 'O', 'N', 'D']
    y = l6m
    plt.figure(2)
    plt.barh(x, y)
    plt.title("Estimated Sale for last 6 Months of 2022") # Writing plot title
    plt.xlabel("Month")      # Writing x-axis label
    plt.ylabel("Quantity Estimated")  # Writing y-axis label

    fileCSV.close
    plt.show()
