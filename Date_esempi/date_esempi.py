print("*** DATE ESEMPI*****")

from datetime import date
from dateutil.relativedelta import relativedelta

birth = date(1970, 6, 18)
now = date.today()
age = now - birth

print("Eta=",age)


rdelta = relativedelta(now, birth)
print(rdelta)
