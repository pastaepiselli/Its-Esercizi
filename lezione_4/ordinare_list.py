def bubble_sort(mylist: list[int]) -> list[int]:

    for i in range(0, len(mylist)):
        
        # faccio len(mylist) - 1 perche non posso fare una comparazione con l'ultimo numero (index error!!)
        for j in range(0,  len(mylist) - 1):

            if mylist[j] > mylist[j + 1]:

                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

    return mylist

    
    
   
           
                
        



            
    

l: list[int] = [5, 3, 6, 12, 2, 4]  

print(bubble_sort(l))



      









        




