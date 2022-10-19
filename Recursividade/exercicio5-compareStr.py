def compareStr(str1:str, str2:str,resultado=None)->int:
    print(str1,str2)
    
    if len(str2)==0 and len(str1)>0:
        resultado= -1 #str2 é maior que str1;
    elif len(str1)==0 and len(str2)>0:
        resultado= 1 #str1 é maior que str2;
    
    elif len(str1)==0 and len(str2)==0:
        resultado= 0 #str1 é igual a str2;
    
    elif str1[0] == str2[0]:
        resultado= compareStr(str1[1:], str2[1:])
    return resultado #não são semelhantes

palavra1=input('Digite a primeira palavra: ')
palavra2=input('Agora, digite a segunda palavra: ')
print(compareStr(palavra1,palavra2))