##Setup##
f = open("/share/data/day5/puzzle.txt")
fragments = []
counter = 0

lines = f.readlines()
for line in lines:
	y = line.split(",")
	for x in y:
		x = x.strip()
		if x != "":
			fragments.append(x)
	   
##Get original letters##
overlap=15
matches=0
original = fragments[0]

while overlap > 0:
	add = True
	while add:
		for fragment in fragments:
			##Position variables##
			full = fragment
			beginning = original [0:overlap]
			end = original[len(original) - overlap:len(original)]
			offset = -99
			##Remove duplicate letters from the fragments and add fragments to original##
			if fragment in original:
				fragments.remove(full)

			elif beginning in fragment:
				offset = fragment.find(beginning)
				fragment = fragment[0:offset]
				original = fragment + original
				matches += 1
				fragments.remove(full)
				
			elif end in fragment:
				offset = fragment.find(end)
				fragment = fragment[overlap + offset::]
				original = original + fragment
				matches += 1
				fragments.remove(full)
		counter += 1
		if matches > 0:
			matches = 0
		elif matches == 0:
			add = False
			overlap -= 1

print(original)
blah = 0
for fragment in fragments:
	if fragment in original:
		blah += 1
	else:
		blah += 0
if blah == 325:
	print("It works!")
else:
	print("Boohoo :(") 
