def parse_time(time):
    if len(time.split(':'))==3:
        h,m,s = time.split(':')
        return int(h)*3600+int(m)*60+int(s)
    else:
        m,s = time.split(':')
        return int(m)*60+int(s)
    
def format_time(time):
    m,s = divmod(time,60)
    h,m = divmod(m,60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    else:
        return f"{m:01d}:{s:02d}"

def sum_timestamps(time):
    total_time=0
    for t in time:
       total_time+=parse_time(t) 
    return format_time(total_time)
            
            
print(sum_timestamps(['2:01']))
