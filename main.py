import configparser


data = configparser.ConfigParser(inline_comment_prefixes = (';','#')) #we allow inline comments in the data file
data.read("data.txt")

params = configparser.ConfigParser(inline_comment_prefixes = (';','#'))
params.read("parametres.txt")

print(data.items("2021"))
print(params.items("DEFAULT"))

