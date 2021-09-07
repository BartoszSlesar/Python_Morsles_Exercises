import math
class float_range:
    def __init__(self,start,stop=None,step=1):
        if step>0 and stop==None:
            stop = start
            start = 0.0 if isinstance(stop,float) else 0
        self.start = start
        self.value = self.start
        self.stop = stop
        self.step = step

    def __iter__(self):
        value = self.start
        if self.start>self.stop and self.step>=0:
            return
        if self.step<0 and self.start<self.stop:
            return
        if self.start < self.stop:
            while(value<self.stop):
                yield value
                value+=self.step
        else:
             while(value>self.stop):
                yield value
                value+=self.step
                
    def __len__(self):
        length = 0
        if self.stop>self.start and self.step>0:
            length = (self.stop - self.start)/self.step
        elif self.stop<self.start and self.step<0:
            length = math.fabs((self.start - self.stop)/self.step)  
        return  math.ceil(length)

    def __reversed__(self):
            if self.stop>self.start and self.step>0:
                flag = 0 if self.start>0 else  1
                return iter(float_range((self.stop-self.start)-flag,(self.start-self.start)-flag,-self.step))
            else:
               flag = 0 if self.stop>0 else  1
               return iter(float_range((self.stop+self.stop)+flag,(self.start+self.stop)+flag,-self.step)) 
    def __eq__(self,other):
        try:
            if self.start == other.start:
                 first = math.fabs(self.stop/self.step)
                 second = math.fabs(other.stop/other.step)
                 return math.ceil(first) == math.ceil(second)
            else:
                return (self.start==self.stop) and (other.start == other.stop)
        except AttributeError:
            return NotImplemented
