import time

def cronometro(fun):
    def wrapper():
        start = time.time()
        fun()
        print(time.time() - start)
    
    return wrapper

@cronometro
def ciao():
    print('ciao')

ciao = cronometro(ciao)
ciao()