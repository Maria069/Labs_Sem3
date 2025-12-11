class Unique(object):
    
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            item = next(self.items)
            
            # ignore_case
            if isinstance(item, str) and self.ignore_case:
                key = item.lower()
            else:
                key = item
            
            if key not in self.seen:
                self.seen.add(key)
                return item
