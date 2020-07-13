from dataclasses import dataclass
import datetime
def last_day(date):
    t_date = date
    c_date = (t_date+datetime.timedelta(days=31)).replace(day=1)
    return (c_date-t_date).days
    
@dataclass(order=True,frozen=True)
class Month:
    __slots__ = ['year','month']
    year: int
    month: int

    @property
    def first_day(self):
        return datetime.date(self.year,self.month,1)
    @property
    def last_day(self):
        return datetime.date(self.year,self.month,last_day(self.first_day))
    @classmethod
    def from_date(cls,adate):
        return Month(adate.year,adate.month)
    def strftime(self,string):
        s = '{:'+string+'}'
        return s.format(self.first_day)
    def __str__(self):
        return f'{self.year}-{self.month:02d}'
    def __iter__(self):
        yield from astuple(self.first_day)
    def _dict_(self):
        raise AttributeError("can't set attribute")



        


        
        
