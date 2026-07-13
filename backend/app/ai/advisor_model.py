def advisor(question):

question=question.lower()

if "invest" in question:
 return "Consider diversified mutual funds based on your risk profile."

elif "save" in question:
 return "Maintain emergency savings and track monthly expenses."

else:
 return "I can help with wealth planning and financial goals."
