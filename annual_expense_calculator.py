total_PV = 0
annual_expense = 8  # in lakhs, starting from year 31
total_corpus= 400 #350
expected_interest_rate=0.06
new_corpus=total_corpus
for year in range(31, 101):  # loop from year 31 to 100
    earning_from_corpus=new_corpus*(expected_interest_rate)

    new_corpus=new_corpus+earning_from_corpus-annual_expense
    if new_corpus>0:
        print(new_corpus,year)
    annual_expense *= 1.1  # increase the expense by 10% for next year
    
print(new_corpus)  # this gives the total amount you need to have in the bank now
