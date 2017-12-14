number_1 = input("Nummer 1: ");
operator = input("Operator: ");
number_2 = input("Nummer 2: ");

if operator == "+":
	print("Ergebnis: ", float(number_1) + float(number_2));
elif operator == "-":
	print("Ergebnis: ", float(number_1) - float(number_2));
elif operator == "*":
	print("Ergebnis: ", float(number_1) * float(number_2));
elif operator == "/":
	print("Ergebnis: ", float(number_1) / float(number_2));
else:
        #operator != /, *, + or -
	print("Ungueltiger Operator");
print("");

#Keep console window open
input("Taste druecken um zu beenden");
