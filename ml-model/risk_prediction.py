def predict_risk(income,expense):

saving=income-expense

if saving>50000:
 return "High"

elif saving>10000:
 return "Medium"

return "Low"
