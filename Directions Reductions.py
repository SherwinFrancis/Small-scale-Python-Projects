def dir_reduc(arr):    
    def canceller(arr):
        for i in range(0,len(arr) -1 ):
            if arr[i] == "NORTH":
                if arr[i+1] == "SOUTH":
                    arr[i] = "CANCEL"
                    arr[i+1] = "CANCEL"   
            elif arr[i] == "SOUTH":
                if arr[i+1] == "NORTH":
                    arr[i] = "CANCEL"
                    arr[i+1] = "CANCEL"
            elif arr[i] == "WEST":
                if arr[i+1] == "EAST":
                    arr[i] = "CANCEL"
                    arr[i+1] = "CANCEL"
            elif arr[i] == "EAST":
                if arr[i+1] == "WEST":
                    arr[i] = "CANCEL"
                    arr[i+1] = "CANCEL"
    canceller(arr)
                
    while "CANCEL" in arr:
        arr.remove("CANCEL")
        canceller(arr)
            
    return arr

