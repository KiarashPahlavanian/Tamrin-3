def TabeHerami(arr, n, i):
    BozorgTarin = i  
    chap = 2 * i + 1  
    rast = 2 * i + 2  

    
    if chap < n and arr[chap] > arr[BozorgTarin]:
        lBorozgTarin = chap

    
    if rast < n and arr[rast] > arr[BozorgTarin]:
        BozorgTarin = rast

    
    if BozorgTarin != i:
        arr[i], arr[BozorgTarin] = arr[BozorgTarin], arr[i]  

        
        TabeHerami(arr, n, BozorgTarin)

def Herami(arr):
    n = len(arr)

    
    for i in range(n // 2 - 1, -1, -1):
        TabeHerami(arr, n, i)

    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        TabeHerami(arr, i, 0)


data = [12, 11, 13, 5, 6, 7]
Herami(data)
print("Araye sort shode:", data)
