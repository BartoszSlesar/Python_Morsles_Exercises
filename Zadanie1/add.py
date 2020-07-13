def add(*matrix):
    result = []
    for m in zip(*matrix):
       result.append([sum(value) for value in zip(*m)])       
    return result
    
    
def add(*matrix):
    result = []
    for m in zip(*matrix):
       print(m)
    return result    

