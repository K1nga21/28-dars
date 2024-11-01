# import pickle

with open('pi_million_digits(1).txt') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n','')

tyil = '13042001'
print(tyil in pi)

# pi = float(pi)

# with open('pi_float.dat','wb') as file:
#     pickle.dump(pi,file)
