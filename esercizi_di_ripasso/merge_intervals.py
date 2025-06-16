def merge_intervals(intervals: list[list]) -> list[list]:
    
    intervals = sorted(intervals)
    print(intervals)
    
    # se la lista e vuota ritorna una lista vuota
    if not intervals:
        return []
    
    # se ce solo un intervallo ritorna quell'intervallo
    elif len(intervals) == 1:
        return intervals
    
    
    # creo la nuova lista con il primo intervallo all'interno
    new_list: list[list] = [intervals[0]]

    
    
    for i in range(1, len(intervals)):
        # confronto gli intervalli e nel caso si interesecano vado ad allungare il range di questo intervallo
        if intervals[i][0] <= new_list[-1][1]:
            new_list[-1][1] = intervals[i][1]
        # non si intersecano aggiungo intervallo
        else:
            new_list.append(intervals[i]) 

    return new_list




intervals = [[2, 6],[1,3] , [8, 10], [15, 18]]


print(merge_intervals(intervals))


        
        
