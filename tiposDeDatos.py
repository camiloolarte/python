# tipos de datos python

print(' ----------------------- STRINGS -------------------')

print('"Isn\'t," they said. #tilde dentro de comillas')

s = 'First line.\nSecond line.'
print(s+' #salto de linea')

print(r'C:\some\name'+' # linea sin formato') #cadenas sin formato

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
     #multiple lineas
""")

print (3*'mi' + 'ma' +' #multiplica strings')

word = 'Python'
print("""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

"""
)
print(word[5]+ '(5)', word[-4]+'(-4)', word[0:2]+'(0:2)', word[2:5]+'(2:5)')  # character in position 0) 

print(word[:2]+' (:2)')
print(word[4:]+' (4:)')
print(word[-2:]+' (-2)')
print(word[:2] + word[2:] + '(:2)+(2:)')
print(word[:4] + word[4:]+' (:4)+(4:)')

print('J' + word[1:]+' J+word[1:] #para asignar un caracter dentro de una cadena se debe crear una nueva')

print(' ----------------------- LISTAS -------------------')

squares = [1, 4, 9, 16, 25]
print('squares = ', squares)
print(squares[4], ' squares[4]')

#otra linea
