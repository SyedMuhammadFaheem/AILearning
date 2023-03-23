#Task 4
def hurry(speed,anniversary):
    if speed<=70 or (anniversary and speed<=80):
        return "No Fine"
    elif speed>=71 and speed<=80 or (anniversary and speed>=81 and speed<=90):
        return "Less Fine"
    else:
        return "Car Seize"
    
print(hurry(91,True))
        
        
        