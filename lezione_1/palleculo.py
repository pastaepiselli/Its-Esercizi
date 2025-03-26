'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(0, len(my_list)):
    if i %2!= 0:

        print(my_list[i])
'''

'''

j = 4

for i in range(1, 11):
    
    stella = "*" * i 
    
    if i >= 6:
        
        stella = "*" * (j)
        j -= 1
    print(stella)

'''

# import math

# cum = "cerchio"
# niggers = 2
# def area(figura:str, *dati):
#     match figura:
#         case "cerchio":
#             area = dati[0]**2 * math.pi
#             print(area)

#         case "quadrato":
#             area = dati[0]**2
#             print(area)

#         case "rettangolo":
#             area = dati[0] * dati[1]
#             print(area)
        
#         case "triangolo":
#             area = (dati[0] * dati[1]) / 2
#             print(area)

# area(cum, niggers)


# Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

# def remove_duplicates(mylist: list):
#     new_list: list = []
#     for item in mylist:
#         if item not in new_list:
#             new_list.append(item)
    
              
#     return new_list

# print(remove_duplicates([1, 2, 3, 1, 2, 4]))
       
    
        
# Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.

# def countdown(n: int):
#     contatore: int = n
#     for i in range(0, n + 1):
#         print(contatore)
#         contatore -= 1




# countdown(5)

# Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
        
# def convert_temperature(gradi: int, conversione: bool = True):
#     if conversione:
#         Faren: float = (gradi * 1.8) + 32
#         return Faren
#     else:
#         Celsio: float  = (gradi - 32) * (5 / 9)
#         return Celsio
    
# print(convert_temperature(32))


# La funzione dovrebbe determinare se un elemento è presente in una lista.
# Un errore nell'implementazione porta a risultati inaspettati.



# def find_element(lst: list[int], element: int) -> bool:
#     for item in lst:
#         if item == element:
#             return True
#     return False

# print(find_element([1, 2 ,3], 4))


# Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
# For example:
    
# def rotate_left(elements: list, k:int):
#     new_list: list = []
#     if k > len(elements):
#         k = k - len(elements)
        


#     new_list.extend(elements[k:])
#     new_list.extend(elements[:k])
   
#     return new_list



   
# print(rotate_left([1, 2, 3, 4, 5], 8))
        
 #Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiu
        
# def check_parentheses(expression: str) -> bool:
#     parentesi: list = []
#     for chr in expression:
#         if chr == '(':
#             parentesi.append(chr)
#         elif chr == ')':
#             if '(' not in parentesi:
#                 return False    
#             else:
#                 parentesi.pop()
        
#     if len(parentesi) == 0: # controlla se una parentesi non e stata chiusa
#         return True
   
# print(check_parentheses("(()))("))


# print(check_parentheses(")("))   
   
    
# print(check_parentheses("()()"))


# print(check_parentheses("(()))("))

            

# def count_isolated(mylist: list):
#     contatore: int = 0
#     isolati: int = 0
#     for elem in mylist:
#         print(elem)
#         if elem == mylist[0]: # primo elemento
#             if elem != mylist[1]: # diverso da quello davanti
#                 isolati += 1
                
#         elif elem == mylist[-1]: # ultimo valore
#             if elem != mylist[-2]:
#                 isolati += 1
#         else:
#             if elem != mylist[contatore] and elem != mylist[contatore + 1]:
#                 isolati += 1
#         contatore += 1
#     return isolati
     
# print(count_isolated([1, 1, 2, 2, 3, 4, 4]))
	
# # print(count_isolated([1, 2, 3, 4, 5]))
           
        
# # # print(count_isolated([1, 2, 2, 3, 3, 3, 4]))



# def remove_elements(original_set: set[int], elements_to_remove: list[int]):

#     new_set: set = set()
#     for elem in original_set:
#         if elem in elements_to_remove:
#             None
#         else:
#             new_set.add(elem)
#     return new_set

    
# print(remove_elements({5, 6, 7}, [7, 8, 9]))

# def merge_dictionaries(dict1: dict, dict2: dict):
#     merged_dict = dict1  
    
#     for key, value in dict2.items():
#         if key in merged_dict:
#             merged_dict[key] += value 
#         else:
#             merged_dict[key] = value  
            
#     return merged_dict

# print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))


    










        



        
        

        


 
        