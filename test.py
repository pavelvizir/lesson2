import ephem
from pprint import pprint
from datetime import datetime
pprint(ephem._libastro.builtin_planets())
for i in list(a[2] for a in ephem._libastro.builtin_planets() if a[1] == 'Planet'):
    t = getattr(ephem, i)
    print(ephem.constellation(t(datetime.now().strftime('%Y/%m/%d'))))
