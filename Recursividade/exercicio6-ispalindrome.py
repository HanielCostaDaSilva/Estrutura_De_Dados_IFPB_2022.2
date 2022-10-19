def ispalindrome(string:str):
    if string.find(' ')>-1:
        string= ''.join(string.split(' '))
    if len(string)<2:
        return True
    if string[0]==string[-1]:
        return ispalindrome(string[1:-1])
    return False
    
flag=True
string=input('digite uma string: ')

while flag:
    print(ispalindrome(string))
    print('digite Break, para encerrar')
    string=input('digite uma string: ')
    flag= not(string.lower()=='break')