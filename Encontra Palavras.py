def GeraDicionario():
    """
    Carrega o arquivo com a lista de palavras e com isso
    gera um dicionário, que é uma lista contendo todas as
    palavras, e a devolve
    """
    palavras = open('PALAVRAS.txt','r')
    lista = []
    cont = 0
    for palavra in palavras:
        cont += 1
        adicionar = palavra.split('\n')
        lista.append(adicionar[0])
        if cont%6000 == 0:
            print('Carregando lista de palavras.')
    palavras.close()
    return lista

def RecebeFrase():
    """
    Das letras que recebemos temos que garantir nenhuma tenha
    acento ou ç
    """
    while True:
        frase = input('Digite uma frase para ser procurada com * nos caracteres a serem buscados:\n')
        erro = False
        for i in frase:
            if i != ' ' and i != '*' and not i.isalpha():
                erro = True
                print("Entrada inválida.")
                break
        if erro == False:
            break
    return frase.upper()
    
def ProcuraPalavra(dicionario, palavra):
    """
    Procura as possíveis palavras para substituir
    a palavra passada, e as devolve numa lista
    """
    palpites = []
    contador = 0
    for palavra_dic in dicionario:
        contador += 1
        eh = True
        if len(palavra_dic) != len(palavra):
            eh = False
        while eh:
            for i in range(len(palavra)):
                if palavra[i] != '*' and palavra[i] != palavra_dic[i]:
                    eh = False
                    break
            if eh:
                palpites.append(palavra_dic)
                break
        if contador % 7000 == 0:
            print('Adicionando palavras.')
            print('Adicionando palavras..')
            print('Adicionando palavras...')
    return palpites

def GeraFrasesPossiveis(dicionario, frase):
    #é necessário obter uma lista de variáveis para anotar as palavras possíveis de cada palavra da frase buscada
    frase_lista = frase.split()
    arquivo = open('Auxiliar.py','w')

    arquivo.write('def GeraVariavel(dicionario,frase_lista,ProcuraPalavra):\n')
    for i in range(len(frase_lista)):
        arquivo.write('\tvariavel%i = ProcuraPalavra(dicionario,frase_lista[%i])\n'%(i+1,i))
    
    arquivo.write('\tarquivo = open(\'FrasesPossiveis.txt\',\'w\')\n')
    
    for i in range(1,len(frase_lista)+1):
        arquivo.write('\t'*i+'for palavra%i in variavel%i:\n'%(i,i))
    
    arquivo.write('\t'*(len(frase_lista)+1)+'arquivo.write(\'')
    
    for i in range(len(frase_lista)):
        if i != (len(frase_lista)-1):
            arquivo.write('%s ')
        else:
            arquivo.write('%s\\n\'%(')

    for i in range(len(frase_lista)):
        arquivo.write('palavra%i'%(i+1))
        
        if i != len(frase_lista)-1:
            arquivo.write(',')
        else:
            arquivo.write('))\n\tarquivo.close()')
    arquivo.close()
    
    from Auxiliar import GeraVariavel
    GeraVariavel(dicionario,frase_lista,ProcuraPalavra)
    
    return print('Arquivo Gerado com sucesso')
    
def main():
    frase = RecebeFrase()
    dicionario = GeraDicionario()
    GeraFrasesPossiveis(dicionario,frase)
    

main()

    
