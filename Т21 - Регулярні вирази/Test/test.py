import re

P_YEAR = r'\b\d{3,4}'
s = '''мама у 1941-му мила раму розміру 333
рушником №2222
'''
'''
x = re.compile(P_YEAR)
res = x.findall(s)
'''

P_DATE = r'\d{2}\.\d{2}\.\d{4}'
P_DATE_GROUP = r'(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})'

s2 = '''11_22.4444

33.44_5555

66.55.6666'''

res = re.search(P_YEAR, s)

##resG = res.group()
#resS = res.start()
#resE = res.end()
#resSP = res.span()

#print(resG)
#print(resS)
#print(resE)
#print(resSP)

G = re.search(P_DATE_GROUP, s2)

resG = G.group('month')
print(resG)



