from collections import UserDict
class EasyDict(UserDict):
    def __init__(self,dictionary={},*,normalize=False,**kwords):
        d = {}
        self.normalize = normalize
        if not dictionary:
            dictionary = kwords
        if normalize:
            for key in dictionary:
                d[key] = dictionary[key]
                d[key.replace(' ','_')]=dictionary[key]
            dictionary = d     
        super().__init__(dictionary)
        #self.__dict__.update(dictionary)
    def  __getitem__(self,key):
        return getattr(self,key)
    def  __getattr__(self,key):
        if key in self.keys():
            return self[key]
        else:
            raise AttributeError() 
    def  __setattr__(self,key,data):
        if ' ' in key and self.normalize:
           self.__dict__[key.replace(' ','_')] = data
        if '_' in key and self.normalize:
           self.__dict__[key.replace('_',' ')] = data
        self.__dict__[key] = data
    def  __setitem__(self,key,data):
         if ' ' in key and self.normalize:
           self.__dict__[key.replace(' ','_')] = data
         if '_' in key and self.normalize:
           self.__dict__[key.replace('_',' ')] = data
         self.__dict__[key] = data
    def __eq__(self,dictionary):
        return self.__dict__==dictionary
    def get(self,key,default=None):
        try:
          val =  getattr(self,key) 
        except AttributeError:
          val = default
        return val

