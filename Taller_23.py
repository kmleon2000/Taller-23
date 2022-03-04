print('***Bienvenido al tutorial de cadenas de texto*** \n\n')

userword = input('Inserta algún Valor (de cualquier tipo): ')

print('1. con el metodo srt() puedes convertir un valor de cualquier tipo a una cadena de texto:\n')

print('Ejemplo: al declarar str(True) nos devuelve la cadena "True" o si declaramos str(1000) este da como resultado "1000" es decir, estos cambian su propiedad de booleano y entero y toman las de una cadena de texto')

print('Para convertir tu dato en una cadena debes declararlo de la sig. forma: str(' + userword + ')\n\n')

print('Una vez declarada la cadena de textos, esta tiene una serie de métodos que permiten ciertas funcionalidades, como las siguientes:\n')

print('Método Upuer: Con este método tu cadena de texto identificará las letras minúsculas y las convertirá en Mayúsculas => "' + userword + '".upper() == ' + userword.upper())

print('Método Lower: Con este método tu cadena de texto identificará las letras Mayúsculas y las convertirá en minúsculas => "' + userword + '".lower() == ' + userword.lower())

print('Método Strip: Este método elimina cualquier carácter que pongas en los argumentos mientras se encuentren al inicio o al final del texto => "' + userword + '".strip("' + userword[0] + userword[-1] +'") == ' + userword.strip(userword[0] + userword[-1]))

print('StartsWith: Verifica si el inicio de la cadena coincide con el parametro que le des => "' + userword + '".startswidth("' + userword[:3] + '") == True')

print('EnsWith: Verifica si el final de la cadena coincide con el parametro que le des => "' + userword + '".endswith("' + userword[:3] + '") == True')

print('Find: Busca el valor del parámetro que le des dentro de la cadena, si lo encuentra retonara la posición donde esta el primer carácter de la palabra buscada, de lo contratio retorna -1 => "' + userword + '".find("' + userword[:3] + '") == ' + str(userword.find(userword[3:])))

print('Replace: Busca el valor del primer parámetro que le des dentro de la cadena, si lo encuentra lo replaz por el segundo parametro que le des =>"' + userword + '".replace("' + userword[:3] + '","z") == ' + userword.replace(userword[0:3],"z"))

print('Replace: Busca el valor del primer parámetro que le des dentro de la cadena, si lo encuentra lo replaz por el segundo parametro que le des =>"' + userword + '".replace("' + userword[:3] + '","z") == ' + userword.replace(userword[0:3],"z"))

print('split: Divide la cadena de texto en subcadenas, tomando como referencia de corte el parametro que le des =>"' + userword + '".replace("' + userword[:3] + '","z") == ' + '[' + ','.join(userword.split(userword[0])) + ']')

print('slice: Es una técnica que te permite acceder a porciones de la cadena de texto, y exiten varias formas => cuando quieres aceder a una cadena desde su posicion x a su posicion y :"' + userword + '"[2:-1] = "' + userword[3:5] + '" con esto le estámos diciendo a python que corte la cadena en su posición 0 hasta su posición 3, luego de la pos 5 hasta el final y me traiga como resultado la cadena del medio (Quitando los dos cortes que hizo)')

