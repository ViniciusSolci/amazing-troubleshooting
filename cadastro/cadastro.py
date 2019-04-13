'''
id
descriçao
exceçao
data
'''
class Troubleshooting(object):
    id=0
    descricao=''
    exception=''
    date=''
    def __repr__(self):
        return str(self.__dict__)
cadastro=[]
tbs1=Troubleshooting()
tbs1.id=1
tbs1.descricao='descrição item 1'
tbs1.exception='NullPointerException'
tbs1.date='10/04/2019'
tbs2=Troubleshooting()
tbs2.id=2
tbs2.descricao='descrição item 2'
tbs2.exception='IndexArrayOutOfBoundException'
tbs2.date='10/04/2019'
cadastro.append(tbs1)
cadastro.append(tbs2)
textOpcao='Digite 1 para adicionar\nDigite 2 para listar\nDigite 3 para atualizar\nDigite 4 para deletar\nDigite 0 para sair: '
opcao=input(textOpcao)
while int(opcao)!=0:
    print(opcao)
    if int(opcao)==1:
        tbs=Troubleshooting()
        ID=input('Digite o ID: ')
        tbs.id=ID
        des=input('Digite a descrição: ')
        tbs.descricao=des
        exc=input('Digite a exceção: ')
        tbs.exception=exc
        data=input('Digite a data: ')
        tbs.date=data
        cadastro.append(tbs)
        print('Inserido com sucesso')
    elif int(opcao)==2:
        for i in range(len(cadastro)):
            print(cadastro[i])
    elif int(opcao)==3:
        idx=int(input('Digite a posição do dado: '))
        old=cadastro[idx-1]
        ID=input('Digite o ID ('+old.id+'): ')
        if ID=='':
            ID=old.id
        old.id=ID
        des=input('Digite a descrição ('+old.descricao+'): ')
        if des=='':
            des=old.descricao
        old.descricao=des
        exc=input('Digite a exceção ('+old.exception+'): ')
        if exc=='':
            exc= old.exception
        old.exception=exc
        data=input('Digite a data ('+old.date+'): ')
        if data=='':
            data=old.date
        old.date=data
        print('Atualizado com sucesso')
    elif int(opcao)==4:
        delete=int(input('Digite a posição do dado a ser excluido: '))
        del(cadastro[delete-1])
    opcao=input(textOpcao)
for i in range(len(cadastro)):
            print(cadastro[i])

