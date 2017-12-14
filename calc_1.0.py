number_1 = raw_input("Nummer 1: ");
operator = raw_input("Operator: ");
number_2 = raw_input("Nummer 2: ");

#if isinstance(number_1, int) and isinstance(number_2, int):

if operator == "+":
	print("Ergebnis: ", float(number_1) + float(number_2));
elif operator == "-":
	print("Ergebnis: ", float(number_1) - float(number_2));
elif operator == "*":
	print("Ergebnis: ", float(number_1) * float(number_2));
elif operator == "/":
	print("Ergebnis: ", float(number_1) / float(number_2));
else:
	print("Ungueltiger Operator");

#else:
		#print("Eine eingegebene Zahl ist keine Zahl");