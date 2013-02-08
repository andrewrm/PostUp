from django.utils import simplejson

class EncodeJSON():
        
    def __init__(self):
        self._store = {}
        self._document = ''
        
    def add(self,key,value=''):
        self._store[key] = value
    
    def remove(self,key):
        self._store[key] = None
        
    def encode(self):
        self._document = simplejson.dumps(self._store)
        return self._document
        
class DecodeJSON():
    
    def __init__(self, document=''):
        self._store = {}
        self._document = document
        
    def decode(self):
        self._store = simplejson.loads(self._document)
        return self._store
        
        
        
        