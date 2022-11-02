import configparser


data = configparser.ConfigParser(inline_comment_prefixes = (';','#')) #we allow inline comments in the data file
data.optionxform = str #to keep the keys case sensitive
data.read("data.txt")

params = configparser.ConfigParser(inline_comment_prefixes = (';','#'))
params.optionxform = str
params.read("parametres.txt")

print(data.items("2021"))
print(params.items("DEFAULT"))

#thanks stack overflow: https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    
def toFloat(str):
    if "," in str:
        str = str.replace(',','.')
    return float(str)
    
d = dotdict({key: toFloat(val) for key,val in dict(data.items("2021")).items()})
p = dotdict({key: toFloat(val) for key,val in dict(params.items("DEFAULT")).items()})

print(d["Pop"], d.BelgiumSurface)#both ways of accessing the data now work
print(p.InvestissementNucleaire)

#Formulaes
def popUpdate(d,p):
    return d.Pop * (1 + p.PopGrowth)
    
#Simulation from year N to year N+1
years = [d]
startingYear = 2022
finalYear = 2050
currentYear = startingYear
N = 0

for N in range(0,finalYear-startingYear):
    d = dotdict(years[N].copy()) #same data structure as before ^
    
    #Update values
    d.Pop = popUpdate(d,p)
    
    years.append(d)

from matplotlib import pyplot as plt

def filter(data, field):
    return [d[field] for d in data]
    
plt.plot(range(startingYear,finalYear+1), filter(years,"Pop"))
plt.show()