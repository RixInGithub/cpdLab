from PIL import Image

subject = Image.open("testSubject.png").convert("RGBA")
pall = []
allCols = []
y = 0
while y != subject.height:
	x = 0
	while x != subject.width:
		col = "".join([hex(num)[2:].zfill(2) for num in subject.getpixel((x, y))]).upper()
		if col not in pall: pall.append(col)
		allCols.append(col)
		x += 1
	y += 1
cols = ""
while len(allCols) != 0:
	col = "".join([*allCols[0]])
	index = str(pall.index(col) + 1).zfill(3)
	count = 0
	try:
		while col == allCols[0]:
			allCols = allCols[1:]
			count += 1
	except: count += 1
	cols += f"{index},{count}/"
print(f"CPD_1/256/{subject.width}/{subject.height}/{str().join(pall)}/{cols}")