import re
def isNumber(s: str) -> bool:
    pattern = re.compile(r'^[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?$')
    return bool(pattern.fullmatch(s))
print(isNumber("0"))      
print(isNumber("e"))      
print(isNumber("."))        
print(isNumber("2.3e4"))   
print(isNumber("-123.456")) 
print(isNumber("+.8e-10")) 
print(isNumber("1e"))       
print(isNumber("e9"))       
