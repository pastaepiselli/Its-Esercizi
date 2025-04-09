def prime_factors(n: int) -> list[int]:
   div: int = 3
   mylist: list[int] = []
   
   while n != 1:
    
    if n % div == 0:
        
        n = n // div 
         
        mylist.append(div)
    
    else:
       
       div += 2
      
   return mylist

 
        
 	
print(prime_factors(99999999999999999999))