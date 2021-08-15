user_input = str(input("Enter a Phrase: "))
text = user_input.split()
acronym = " "
for i in text:
    acronym = acronym+str(i[0]).upper()
print("The acronym for","'",user_input,"'","is "+"'"+acronym,"'")
