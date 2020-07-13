def sum_timestamps(time):
    m = 0
    s = 0
    h = 0
    for t in time:
        if len(t.split(':'))==3:
            temp_h,temp_m,temp_s = t.split(':')
            h+=int(temp_h)
        else:
            temp_m,temp_s = t.split(':')
        m+=int(temp_m)
        s+=int(temp_s)
    m+=int(s/60)
    s=int(s%60)
    if s<10:
        s = '0{}'.format(s)
    
    if m>=60 or m<10:
        h += int(m/60)
        m = int(m%60)
        if m<10 and h!=0:
            m = '0{}'.format(m)

    if h!=0:
        time = '{}:{}:{}'.format(h,m,s)
    else:
        time = '{}:{}'.format(m,s)
        
    return time
            
            
print(sum_timestamps(['2:01']))
