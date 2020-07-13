def get_earliest(date1, date2):
    tdate1 = [int(el) for el in date1.split("/")]
    tdate2 = [int(el) for el in date2.split("/")]
    for element in range(-1,2,1):
        if(tdate1[element] > tdate2[element]):
            return date2
        elif tdate1[element] < tdate2[element]:
            return date1