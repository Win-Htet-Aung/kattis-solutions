import re
st = input()
pt = r'[a-z]'
st = st.lower()
dict = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3',
		'f':'#', 'g':'6', 'h':'[-]', 'i':'|', 'j':'_|',
		'k':'|<', 'l':'1', 'm':'[]\/[]', 'n':'[]\[]', 'o':'0',
		'p':'|D', 'q':'(,)', 'r':'|Z', 's':'$', 't':"']['",
		'u':'|_|', 'v':'\/', 'w':'\/\/', 'x':'}{', 'y':'`/',
		'z':'2'}
ans = ''
for i in st:
	if re.match(pt, i):
		ans = ans + dict[i]
	else:
		ans = ans + i
print(ans)