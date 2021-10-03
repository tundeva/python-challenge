#scipt to collate election result

import os

import csv

csvpath = os.path.join("", "resources", "election_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")

    print(csvreader)

    top_line = next(csvreader)

    numlines = 0
    candidates = []
    scores = []
    lines = []


    headln = "Election Results"
    headln2 = "--------------------------"

    print(headln)
    print(headln2)

    

    # iterate through the CSV file
    for row in csvreader:

        #count rows
        numlines = numlines + 1


        # simultaneously create arrays for candidates and scores
        candidatename = row[2]    
        if candidatename not in candidates:
            candidates.append(candidatename)
            scores.append(1)
        else:
            commonindex = candidates.index(candidatename)
            scores[commonindex] = scores[commonindex] + 1

    line1 = f"Total Votes: {numlines}"
    print(line1)
    print(headln2)

    # format out the scores by one-to-one mapping of scores and candidates
    scorecard = []
    newresult = ""
    for person in candidates:
        positioninarray = candidates.index(person)
        totalscore = scores[positioninarray]
        percentagescore = (totalscore * 100) / numlines
        newresult = f"{person}: {percentagescore:.3f}% ({totalscore})"
        print(newresult)
        scorecard.append(newresult)

       
    
    print(headln2)


    highest = max(scores)
    ind = scores.index(highest)
    winner = candidates[ind]


   

    
    lastline = f"Winner: {winner}"

    print(lastline)

    print(headln2)

    textlist = [headln, headln2, line1, headln2]
    textlist2 = [headln2, lastline, headln2]

f = open('analysis/result.txt', 'w')
with open('analysis/result.txt', 'w') as f:
    for line in textlist:
        f.write(line)
        f.write('\n')
    for winn in scorecard:
        f.write(winn)
        f.write('\n')
    for line2 in textlist2:
        f.write(line2)
        f.write('\n')






