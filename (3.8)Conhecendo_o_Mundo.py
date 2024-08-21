locais = ['Japão','Dysney','Canadá','París','Egito']

print (locais,'\n')

print ('Lista em ordem alfabética:\n',sorted(locais),'\n')

print('Lista original:\n',locais,'\n')

print('Lista em ordem alfabética reversa:\n', sorted(locais, reverse=True),'\n')

print('Lista original:\n', locais,'\n')

locais.reverse()
print('Lista em ordem reversa:\n',locais,'\n') 

locais.reverse()
print('Lista normal novamente:\n', locais,'\n')

locais.sort()
print('Lista alterada para ordem alfabética permante:\n',locais,'\n')
