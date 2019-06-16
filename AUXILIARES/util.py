from math import degrees, acos

def format_number(n, accuracy=6):
    """Formats a number in a friendly manner (removes trailing zeros and
       unneccesary point.
    """    
    fs = "%."+str(accuracy)+"f"
    str_n = fs%float(n)
    if '.' in str_n:
        str_n = str_n.rstrip('0').rstrip('.')
    if str_n == "-0":
        str_n = "0"
    #str_n = str_n.replace("-0", "0")
    return str_n
    
def truncaNumero(num, digits):
    """Funcao para truncar o numero conforme a quantidade de digitos informada,
       
       truncaNumero(numero, quantidadeDigitos)
       
       return str->Numero
    """
    if (is_number(num) and type(digits)== int):     
        sp = format(float(num), 'f').split('.')   
        if len(sp[1][:digits]) < digits:
            sp[1] = sp[1][:digits]+"0"*(digits-len(sp[1][:digits]))      
        return '.'.join([sp[0], sp[1][:digits]])
    else:
        raise ValueError("O primeiro parametro deve ser um numero e o segundo \
        parametro deve ser do tipo int")
   
def lerp(a, b, i):
    """Linear enterpolate from a to b."""
    return a+(b-a)*i

def is_number(s):
    """Verifica se uma string e um numero, int ou float
    """
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def GetAnguloTextosTubos(Cx, Cy):
    """Funcao que retorna o angulo correto para que os Textos das Labels dos
       Tubos nao fiquem de cabeca para baixo ou de tras para frente.
    """
    if (Cx >=0 and Cy >=0):
        return degrees(acos(Cx))
    elif (Cx <0 and Cy >=0):
        return float(degrees(acos(Cx)))+180
    elif (Cx <0 and Cy <0):
        return float(degrees(acos(-Cx)))
    elif (Cx >0 and Cy<0):
        return float(degrees(acos(-Cx)))+180

def GetPath():
    pass
    
if __name__ == "__main__":
    print (truncaNumero(1.1234, 10))
    
    

