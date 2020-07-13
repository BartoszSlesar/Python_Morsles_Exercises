def compact(values):
    check=object()
    for val in values:
        if val != check:
           check=val
           yield val
