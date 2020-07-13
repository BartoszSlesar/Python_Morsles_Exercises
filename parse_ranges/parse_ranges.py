import re
def parse_ranges(val):
    pattern = '[a-zA-Z]+|(->)?'
    value =  re.sub(pattern,'',val).split(',')
    pairs = [val.split('-') if '-' in val else (val,val) for val in value]
    return(
            val for start, stop in pairs
            for val in range(int(start),int(stop)+1)
        )
        
