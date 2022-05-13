import random

def xor(chave,binario):
    resultado =[]
    if binario[0] =='0':
        for i in range (1, len(binario)):
            resultado.append(str(binario[i]))
        return ''.join(resultado)
    else:    
        for i in range(1,len(binario)):   
            if chave[i] == binario[i]:      
                resultado.append('0')
            else :
                resultado.append('1')
        return ''.join(resultado)

def verifica_zeros(aux,binario,fim):
    aux2=[]
    aux2.append(aux[1])
    aux2.append(aux[2])
    aux2.append(aux[3])
    aux2.append(binario[fim])
    fim += 1
    while aux2[0] == '0' and  fim < 19:
        aux2[0] = aux2[1]
        aux2[1] = aux2[2]
        aux2[2] = aux2[3]
        aux2[3] = binario[fim]
        fim += 1
    return ''.join(aux2),fim

def processo(binario,chave):
    #binario =1111111111111110000
    #chave =  1001
    inicio = 0
    fim = 4
    aux = binario[inicio:fim]

    while fim < 19:
        if aux[0]=='0':
            resultado,fim=verifica_zeros(aux,binario,fim)
        else:
            resultado=aux         
        aux = xor(chave,resultado) +  binario[fim]
        fim+=1
    
    resultado=aux         
    aux = xor(chave,resultado)
    return aux

def codificar(binario,chave):

    t_chave = len(chave)
    binario_sr= binario + '0'*(t_chave-1)
    resto = processo(binario_sr,chave)
    print('Resto após calculo de codificaçao: ',resto)
    binario=binario+resto
    
    return binario

def decodificar(binario,chave):
    t_chave=len(chave)
    resto = processo(binario,chave)
    binario = binario[0:len(binario)-(t_chave-1)]
    return binario,resto


def simular_erro(binario):
    chance_erro=random.randint(0,len(binario))
    binario_corrompido=''
    if chance_erro == (len(binario)-2):
        for i in range(0,len(binario)):
            if i== 1:
                binario_corrompido=binario_corrompido+'0'
            else:
                binario_corrompido=binario_corrompido+binario[i]
        return binario_corrompido
    else:
        return binario    

def simular():
    binario = '1111111111111110'
    chave = '1001'
    print('Dado sendo enviado: ', binario)
    print('Chave: ', chave)

    
    print('Dado Codificado!')
    binario_cod=codificar(binario,chave)
    print('Dado codificado: ', binario_cod)

    binario_cod=simular_erro(binario_cod)

    binario_decod,resto=decodificar(binario_cod,chave)
    print('Dado decodificado: ',binario_decod)
    print('Resto do calculo: ', resto)
    if(resto == '000'):
        print('Mensagem sem erros!')
    else:
        print('Mensagem corrompida! Favor reenviar a mensagem.')

print(simular())
