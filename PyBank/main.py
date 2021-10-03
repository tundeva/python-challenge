import os

import csv

csvpath = os.path.join("", "resources", "budget_data.csv")


with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")

    print(csvreader)

    top_line = next(csvreader)
    

    numlines = 0

    profitsum = 0

    oldprofit = 0
    newprofit = 0
    worstday = ""
    bestday = ""
    profitvariance = 0
    profitvariancesum = 0
    profitvariancemean = 0
    profitvariancemeansum = 0

    greatestboom = 0
    greatestdepression = 0

    for row in csvreader:
        numlines = numlines + 1

        newprofit = int(row[1])
        profitsum = profitsum + newprofit
        
        # place first line profit in variable
        if numlines == 1:
            oldprofit = newprofit

        #place first variance in variable
        if numlines == 2:
            oldvariance = profitvariance
                
        #ensure calculations begin on second line
        if numlines > 1:
            profitvariance = newprofit - oldprofit
            profitvariancesum = profitvariancesum + profitvariance
            profitvariancemean = profitvariancesum / (numlines - 1)        
            oldprofit = newprofit

            
            if profitvariance > greatestboom:
                greatestboom = profitvariance
                bestday = str(row[0])
            elif profitvariance < greatestdepression:
                greatestdepression = profitvariance
                worstday = str(row[0])
            

        
headln = "Financial Analysis"
headln2 = "--------------------------"
line1 = f"Total Months: {numlines}"
line2 = f"Total: {profitsum}"
line3 = f"Average Change: ${profitvariancemean:.2f}"
line4 = f"Greatest Increase in Profits: {bestday} {greatestboom}"
line5 = f"Greatest Decrease in Profits: {worstday} {greatestdepression}"


print(headln)
print(headln2)
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)

textlist = [headln, headln2, line1, line2, line3, line4, line5]

f = open('analysis/result.txt', 'w')
with open('analysis/result.txt', 'w') as f:
    for line in textlist:
        f.write(line)
        f.write('\n')








