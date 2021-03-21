s = "248,00 Kč"

#cgetting only the number and converting the list into a string
text = []
for i in s:
    if i in ["0","1","2","3","4","5","6","7","8","9",","]:
        text.append(i)
    else:
        pass
print("".join(text))