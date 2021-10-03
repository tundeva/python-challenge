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
line1 = f"Total Votes: {numlines}"

print(headln)
print(headln2)
print(line1)
    
    # create array to hold candidates
    for row in csvreader:
         numlines = numlines + 1
         candidatename = row[2]    
         if candidatename not in candidates:
             candidates.append(candidatename)

    # count votes for each candidate
    for name in candidates:
        totalscore = 0
        for row in csvreader:
            nextvote = row[2]
            if nextvote == name:
                totalscore = totalscore + 1

    scores.append(totalscore)


    for score in scores:
       indy = scores.index(score)
       actualcandidate = candidates[indy]
       percentagescore = (score * 100) / numlines
       print(f"{actualcandidate}: {percentagescore:.3f}% {score}")
       lines.append(f"{actualcandidate}: {percentagescore:.3f}% {score}")
       




    highest = max(scores)
    ind = scores.index(highest)
    winner = candidates[ind]



    







lastline = f"Winner: {winner}"






textlist = [headln, headln2, line1, lines[], headln2, lastline]

f = open('analysis/result.txt', 'w')
with open('analysis/result.txt', 'w') as f:
    for line in textlist:
        f.write(line)
        f.write('\n')

