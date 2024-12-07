# 1. Elimina los espacios en blanco al principio y al final de cada nombre.
# 2. Asegúrate de que la primera letra de cada nombre sea mayúscula y el resto minúsculas.
# 3. Crea una nueva lista llamada 'nombresFormateados' con los resultados de los pasos anteriores.

nombres= [" JUan ", "peDro", "AnA ", "ricArDo", "MAria "]

nombresFormateados= [nombres[0].strip().capitalize(),
                     nombres[1].strip().capitalize(),
                     nombres[2].rstrip().capitalize(),
                     nombres[3].strip().capitalize(),
                     nombres[4].rstrip().capitalize()]
"print(nombresFormateados)"
#-------------------------------------------------------------
# 1. Calcula la longitud de cada frase y almacénalo en una nueva lista llamada 'longitudes'.
 
frases = ["Hola mundo", "Python es divertido", "Aprendiendo listas",
           "cadena de texto"]
longitudes= [len(frases[0]),
              len(frases[1]),
              len(frases[2]),
              len(frases[3])]

"print(longitudes)"

#---------------------------------------------------
# 1. Convierte todas las palabras a mayúsculas y almacénalas en la lista 'mayusculas'.
# 2. Convierte todas las palabras a minúsculas y almacénalas en la lista 'minusculas'.
# 3. Invierte las mayúsculas y minúsculas de cada palabra y almacénalas en la lista 'invertidas'.

palabras = ["manzana", "BANANA", "KiWi", "Naranja", "uva"]

mayusculas=[palabras[0].upper(),
            palabras[1].upper(),
            palabras[2].upper(),
            palabras[3].upper(),
            palabras[4].upper()]
"print(mayusculas)"
minusculas=[palabras[0].lower(),
            palabras[1].lower(),
            palabras[2].lower(),
            palabras[3].lower(),
            palabras[4].lower()]
"print(minusculas)"
invertidas=[palabras[0].swapcase(),
            palabras[1].swapcase(),
            palabras[2].swapcase(),
            palabras[3].swapcase(),
            palabras[4].swapcase()]
"print(invertidas)"
#---------------------------------------------------------------------
 # 1. Separa la oración en una lista de palabras.
 # 2. Reemplaza la palabra "increíble" por "genial" y guarda la nueva oración en la variable 'nuevaOracion'.

oracion = "Python es increíble y útil para programar"
oracion= oracion.replace('increíble','genial')
nuevaOracion=oracion.split()
"print(nuevaOracion)"
#-----------------------------------------------------------------
# 1. Verifica si cada cadena es alfanumérica y guarda los resultados
#(True/False) en una lista llamada 'esAlfanumerico'.
# 2. Verifica si cada cadena es alfabética y guarda los resultados
#(True/False) en una lista llamada 'esAlfabetico'.
# 3. Verifica si cada cadena es alfanumérica y guarda los resultados
#(True/False) en una lista llamada 'esNumerico'.


cadenas = ["Python3", "1234", "Hola_mundo", "Aprender", " "]
esAlfanumerico=[cadenas[0].isalnum(),
                cadenas[1].isalnum(),
                cadenas[2].isalnum(),
                cadenas[3].isalnum(),
                cadenas[4].isalnum()]
"print(esAlfanumerico)"         
esAlfabetico=[cadenas[0].isalpha(),
              cadenas[1].isalpha(),
              cadenas[2].isalpha(),
              cadenas[3].isalpha(),
              cadenas[4].isalpha()]
"print(esAlfabetico)"     
esNumerico=[cadenas[0].isdigit(),
             cadenas[1].isdigit(),
             cadenas[2].isdigit(),
             cadenas[3].isdigit(),
             cadenas[4].isdigit()]
"print(esNumerico)"
#-----------------------------------------------------------------------
# 1. Separa el nombre y el apellido.
# 2. Convierte el nombre y apellido a minúsculas.
# 3. Crea una lista 'usuarios' que contenga el primer nombre seguido
#del primer apellido, por ejemplo, "ana.perez".
nombres_apellidos = ["Ana Pérez", "Juan Martín", "Lucía García", "Pedro Gómez"]
separado= [nombres_apellidos[0].split(),
           nombres_apellidos[1].split(),
           nombres_apellidos[2].split(),
           nombres_apellidos[3].split()]
"print(separado)"
ambos= [nombres_apellidos[0].lower().replace(' ','.'),
      nombres_apellidos[1].lower().replace(' ','.'),
      nombres_apellidos[2].lower().replace(' ','.'),
      nombres_apellidos[3].lower().replace(' ','.')]
"print(ambos)"
#------------------------------------------------------------------------
# 1. Elimina los espacios innecesarios al principio y al final.
# 2. Reemplaza los dobles espacios por espacios simples.
# 3. Asegúrate de que solo la primera letra sea mayúscula.
# 4. Guarda el resultado en la variable 'textoLimpio'.

texto = " Python ES  Genial! "
textoLimpio= texto.replace("  "," ").capitalize().lstrip().rstrip()
"print(textoLimpio)"
           



















 
