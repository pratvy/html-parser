import re

f = open("/home/prateek/codeasylum/amazon.html",'r')
s=f.read()
f.close()
empty = []
count = {}
level = {}
stack =[]

alltagsregx = re.compile(r'<(/?\w+)')
opentagsregx = re.compile(r'<(\w+)')
closetagsregx =re.compile(r'</(\w+)')

alltags = alltagsregx.findall(s)
opentags = opentagsregx.findall(s)
closetags = closetagsregx.findall(s)

for i in set(opentags):
	if i not in set(closetags):
		empty.append(i)

for i in opentags:
	if i not in count.keys():
		count[i] = 1
	else:
		count[i] = count[i]+1


for i in alltags:
	if i not in empty:
		if i[0]!='/':
			stack.append(i)
			if i in level.keys():
				level[i]=level[i]+","+str(len(stack))
			else:
				level[i]=str(len(stack))
		else:
			stack.pop()

print("Tags and their respective levels:-")
for i in level:
	print(i+"\t\t"+level[i])
print("\n\n\n")

print("\n\n\nTags and their respective counts:-")
for i in count:
	print(i+"\t\t"+str(count[i]))
print("\n\n\n")
print("empty tags are")
print(empty)


