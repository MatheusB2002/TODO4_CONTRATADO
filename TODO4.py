
palavrasAnalista = [ 'python' , 'power bi' , 'sql' , 'boa comunicação' ]
palavrasCientista  = [ 'python' , 'banco de dados' , 'machine learning' , 'resolução de problemas' , 'estatística' ]
participantesAn= {'Jobson': ['tableau','pandas','sql'],'Amanda': ['pandas','JavaScript', 'git'] }
participantesCi= {'Milena': ['banco de dados', 'python', 'pandas'],'Marcos':['sql','power bi']}
aprovadosAnalista = {}
aprovadosCientista = {}


def escolha():
    
    print(' '*8,'\nBem vindo ao sistema! \n[1] Analisar curriculos já computados \n[2] Adicionar curriculos')
    analiseOuAdd = int(input('\nColoque o numero correspondente ao que quer: '))

    if analiseOuAdd == 1:
        print('Ok mandarei o(a) Sr(a). direto para a escolha final.')

    elif analiseOuAdd == 2:
        print('\n[1] Ler um arquivo com Curriculo existente.\n[2] Criar um resumo.')
        # currOuCand = int(input('\nColoque o numero correspondente ao que quer: '))
        escolhamenu2()
            
    else:
        print('Escolha inválida, digite um número correspondente a opção:')
        escolha()
        
    print('Fim da adição.\n[1] Filtrar Candidatos.\n[2] Voltar ao menu Principal')
    analiseOuAdd = int(input('\nColoque o numero correspondente ao que quer: '))
    
    if analiseOuAdd == 1:
        filtrar()
    elif analiseOuAdd == 2:
        escolha()
        


def escolhamenu2():
    
        currOuCand = int(input('\nColoque o numero correspondente ao que quer: '))
        if currOuCand == 1:
            count = 1
            print(' '*38, '\nATENÇÂO! \nPara que seja possivel ler o arquivo, ele deve estar no mesmo diretório desse programa!')
            qtdAdd= int(input('Adicionar quantos curriculos? '))
            while count <= qtdAdd:
                print(f'candidato {count}')
                addCurriculo()
                count += 1

        elif currOuCand == 2:
            count = 1
            qtdAdd= int(input('Adicionar quantos resumos? '))
            while count <= qtdAdd:
                print(f'candidato {count}')
                addcandidatoSistema()
                count += 1
        else:
            print('Escolha Inválida')
            escolhamenu2()



def addCurriculo():

    palavrasChaves = []
    print('[1] Analista\n[2] Cientista \n')
    tipo = int(input('Digite o número correspondente: '))
    nomeCand = input('Nome do candidato: ')
    nomePasta = input('Digite o nome exato da pasta com o ".txt": ')

    with open(f'{nomePasta}','r') as f:
        listaCurriculo1 = f.readlines()
        listaCurriculo1 = str(listaCurriculo1).lower()
        for palavra in palavrasAnalista:
            if palavra in listaCurriculo1:
                palavrasChaves.append(palavra.lower())
        if tipo == 1:
            participantesAn[nomeCand] = palavrasChaves
        elif tipo == 2:
            participantesCi[nomeCand] = palavrasChaves

                 

def addcandidatoSistema():

    count = 1
    palavrasChaves = []
    
    print('[1] Analista\n[2] Cientista \n')
    tipo = int(input('Digite o número correspondente: '))
    nomeCand = input('Nome do candidato: ')
    print('-'*30)
    qtdPalavras = int(input('Quantas palavras deseja adicionar ao resumo? '))

    while count <= qtdPalavras:
        palavrasChaves.append(input('Adicione palavra: ').lower())
        count += 1
    if tipo == 1:
        participantesAn[nomeCand] = palavrasChaves
    elif tipo == 2:
        participantesCi[nomeCand] = palavrasChaves



def filtrar():

    for chave, listaValores in participantesAn.items():
        for x in listaValores:
            if x in palavrasAnalista:
                aprovadosAnalista[chave] = listaValores
    for chave, listaValores in participantesCi.items():
        for x in listaValores:
            if x in palavrasCientista:
                aprovadosCientista[chave] = listaValores  
    


def divulgação():

    print(f'Foram {len(participantesAn)} candidatos inscritos para Analista de dados e {len(participantesCi)} inscritos para Cientista de dados.\nDesses {len(participantesCi) + len(participantesAn)} inscritos em suas respectivas vagas.\n\n')
    print(f'Analista de dados: São {len(aprovadosAnalista)} candidatos que possuem pelo menos uma palavra chave.\n\nCientista de dados: São {len(aprovadosCientista)} candidatos que possuem pelo menos uma palavra chave.')
    print('\nDeseja saber quais são e saber quantas palavras cada um tem?\n[1] Sim \n[2] Não')

    desejo = int(input('Digite o número correspondente'))
    if desejo == 1:
        print('\nAnalistas de dados aprovados:\n ')
        
        for i in aprovadosAnalista:
            aprovadosAnalista[i] = str(aprovadosAnalista[i]).strip('[]')
            print(f'{i} com as palavras {aprovadosAnalista[i]}.')
        print('\nCientistas de dados aprovados:\n ')
        
        for i in aprovadosCientista:
            aprovadosCientista[i] = str(aprovadosCientista[i])[1:-1]
            print(f'{i} com as palavras {aprovadosCientista[i]}.')
    elif desejo == 2:
        print('ok, saindo do sistema.')
        exit()
            


escolha()
divulgação()