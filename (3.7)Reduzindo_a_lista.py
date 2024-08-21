pessoas = ['Myazaki','Tappei','Silvio']

print(f'Olá {pessoas[0]}, {pessoas[1]}, {pessoas[2]}, vocês estão convidados para o meu jantar\n')

print ('Consegui encontrar uma mesa maior para o jantar\n')

pessoas.insert(0,'Ronaldinho')
pessoas.insert(1, 'Gojo')
pessoas.append('Guanabara')

print (f'por isso voces, tambem estão convidados {pessoas[0]}, {pessoas[1]}, e {pessoas[5]}!!\n')


print ('Oh não! Acabo de receber uma mensagem do restaurante, e só posso levar duas pessoas!\n')

pessoa_removida1 = pessoas.pop(4)
print (f'Lamento {pessoa_removida1}, mas não posso convida-lo desta vez!\n')

pessoa_removida2 = pessoas.pop(4)
print(f'Lamento {pessoa_removida2}, mas não posso convida-lo desta vez!\n')

pessoa_removida3 = pessoas.pop(1)
print(f'Lamento {pessoa_removida3}, mas não posso convida-lo desta vez!\n')

pessoa_removida4 = pessoas.pop(0)
print(f'Lamento {pessoa_removida4}, mas não posso convida-lo desta vez!\n')

print(f'{pessoas[0]}, e {pessoas[1]}, vocês ainda estão convidado\n')

print('Acho melhor cancelarmos o jantar!\n')

del pessoas[1]
del pessoas[0]
print (pessoas)
