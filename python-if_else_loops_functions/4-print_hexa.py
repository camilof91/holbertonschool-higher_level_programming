#!/usr/bin/python3
for i in range(99):
    print("{:d} = 0x{:x}".format(i, i))
    ''' 
    "{:d} = 0x{:x}" especifica a format(i,i) que formato retorna
    {:d} indica que debe ser decimal
    {:x} indica que debe ser hexadecimal
    '''
