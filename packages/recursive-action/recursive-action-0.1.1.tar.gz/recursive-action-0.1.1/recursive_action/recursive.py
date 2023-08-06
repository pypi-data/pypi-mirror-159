class recursionHandler:
    def __init__(self, *, methods=True, classes=True):
        self.okMethods = methods
        self.okClasses = classes
        self.methods = {}
    def __call__(self, hash: str):
        return self.methods[hash]
    def recursiveMethod(self, name: str):
        
        def Inner(func):
            self.methods[name] = func
            return func
        
        return Inner
    def recursiveClass(self, name:str):
        def Inner(cls):
            self.methods[name] = cls
            return cls
        return Inner