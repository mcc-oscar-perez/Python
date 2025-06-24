import datetime

# create an object thas shows the time
# datetime.time(hour, minute, second, microsecond)
mi_hora = datetime.time(17,35)
print(type(mi_hora)) 
print(mi_hora)

#%%
import datetime

# create an object that shows the date
# datetime.date(year, month, day)

mi_fecha = datetime.date(2025, 6, 23)
print(type(mi_fecha))
print(mi_fecha)
print(mi_fecha.year)
print(mi_fecha.month)
print(mi_fecha.day)
print(mi_fecha.ctime())
print(mi_fecha.today())
# %%

from datetime import datetime

mi_fecha = datetime(2025, 6, 23, 17, 35, 2, 2500)
print(type(mi_fecha))
print(mi_fecha)

# We can replace the date and time in the previous object 

mi_fecha = mi_fecha.replace(year=2024, month=5, day=20, hour=10, minute=30,          second=15, microsecond=5000)
print(mi_fecha)

# %%

from datetime import date

nacimiento = date(1990, 1, 1)
defuncion = date(2025, 6, 23)
diferencia = defuncion - nacimiento
print(type(diferencia))
print(diferencia)  

# %%
# Practical excercises 

# 1
import datetime
mi_fecha = datetime.date(1999,2,3)
print(mi_fecha.year)  # 1999
print(mi_fecha.month) # 2 
print(mi_fecha.day)   # 3

# 2
from datetime import date
hoy = date.today()
print(hoy.year)  # Current year
print(hoy.month) # Current month

# 3 
from datetime import datetime
minutos = datetime.now().minute
