#Gli array di NumPy forniscono un metodo mean per il calcolo della media, ma nessun metodo per calcolare mediana o moda. Scrivete due funzioni median e mode che usino le 
# funzionalità esistenti di NumPy per calcolare la mediana e la moda dei valori in un array. Le funzioni devono determinare la mediana e la moda a prescindere dalla forma
#  dell’array. Provate le vostre funzioni su almeno tre vettori di forma diversa.
#Modificate le funzioni dell’esercizio precedente per dare all’utente la possibilità di fornire un argomento denominato axis, 
# così da poter effettuare i calcoli riga per riga o colonna per colonna in un array bidimensionale.

import numpy as np
array=np.random.randint(0,30,(6,6))        #creo un array 5x5 di numeri casuali tra 0 e 99

def median(array,axis):  # Calcola la mediana di un array
    def calcolo_mediana(array):
        import numpy as np
        #modifico l'array per ordinarlo e renderlo monodimensionale
        amaca=np.sort(array.flatten()) 
        #se la lunghezza dell'array è pari
        if len(amaca)%2==0:
            #restituisci la media tra i due valori centrali.
            return (float((amaca[(len(amaca))//2]+amaca[((len(amaca))//2)-1])/2))
        else:
            #restituisci il valore centrale.
            return(float(amaca[(len(amaca)-1)//2]))
    if axis is None: #se l'asse è nullo si calcola la moda dell'intero array
        return calcolo_mediana(array)
    else:
        if axis == 0: #se si sceglie axis=0 si calcola la moda per ogni colonna
# ritorna un array che fa la moda
            return np.array([calcolo_mediana(array[:, i])# per ogni colonna i
                              for i in range(array.shape[1])])# in range del numero di colonne
        elif axis == 1:
            return np.array([calcolo_mediana(array[i, :])#per ogni riga i
                              for i in range(array.shape[0])])#in range del numero di righe

def moda(array,axis):  # Calcola la moda di un array
    def calcolo_moda(array): 
        import numpy as np
        amaca=np.sort(array.flatten())  # Ordina l'array e lo rendo monodimensionale    
        dizionario={}  # Crea un dizionario 
        for i in amaca: #per ogni elemento dell'array
            if i in dizionario: #se l'elemento è già presente nel dizionario
                dizionario[i]+=1    #incrementa il valore associato all'elemento
            else:
                dizionario[i]=1 #altrimenti crea una nuova chiave con valore 1
        for c,v in dizionario.items():  #per chiave e valore nel dizionario
            if v==max(dizionario.values()): #quando il valore è uguale al valore massimo
                moda =c  # La moda è uguale alla chiave corrispondente
        if max(dizionario.values())==1: #se il valore massimo è 1 
            return "Non esiste moda"
        return moda 
    if axis is None: #se l'asse è nullo si calcola la moda dell'intero array
        return calcolo_moda(array)
    else:
        if axis == 0: #se si sceglie axis=0 si calcola la moda per ogni colonna
# ritorna un array che fa la moda
            return np.array([calcolo_moda(array[:, i]) # per ogni colonna i
                              for i in range(array.shape[1])]) # in range del numero di colonne
        elif axis == 1:
            return np.array([calcolo_moda(array[i, :]) #per ogni riga i
                             for i in range(array.shape[0])])#in range del numero di righe

print(array)
print(moda(array,None))
print(moda(array,0))
print (median(array,None))
print (median(array,0))
