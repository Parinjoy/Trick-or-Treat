#Encode the text
string=input('Enter some text: ')
code=''
for i in string.lower():
	if ord(i)==32:
		code+=chr(32)
		continue
	code+=chr(ord(i)-50)
print (code)