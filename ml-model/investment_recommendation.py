def investment(profile):

plans={
"High":"Stocks and Equity Funds",
"Medium":"Balanced Mutual Funds",
"Low":"FD and Bonds"
}

return plans.get(profile)
