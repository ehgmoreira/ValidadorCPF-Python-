import array as arr
from xmlrpc.client import Boolean

cpf ="11144477705"
VERIFICADOR = arr.array('i',[11,10,9,8,7,6,5,4,3,2])


def conversao_String(cpf: str) ->arr.array:
    result = arr.array ('i',[])
    stringList = list(cpf)
    for valor in stringList:
        result.append(int(valor))
    return result       


def multiplicar(arrayA: arr.array, arrayB: arr.array)->arr.array:
    result = arr.array('i', [])
    
    for elemA, elemB in zip(arrayA, arrayB):
        result.append(elemA * elemB) 
        
    return result


def verificaDigito1(cpf: arr.array)->bool:
    multiplicar(VERIFICADOR[1:10], cpf[0:9])   
    
    listSum = sum(multiplicar(VERIFICADOR[1:10], cpf[0:9]))
    restoDivisao = listSum % 11    
    digitoValido = 0 if restoDivisao < 2 else 11 - restoDivisao
    return cpf[9] == digitoValido 

def verificaDigito2(cpf: arr.array)->bool:
    multiplicar(VERIFICADOR[0:10], cpf[0:10])   

    listSum = sum(multiplicar(VERIFICADOR[0:10], cpf[0:10]))
    restoDivisao = listSum % 11    
    digitoValido = 0 if restoDivisao < 2 else 11 - restoDivisao
    return cpf[10] == digitoValido
    
def validaCPF(cpf: str)->str:
    formatCPF = conversao_String(cpf)
      
    return 'CPF Valido' if verificaDigito1(formatCPF) and verificaDigito2(formatCPF) else 'CPF Invalido'  


print(validaCPF('11144477705'))
