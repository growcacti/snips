class Memoize:
    def __init__(self, x):
        self.x = x
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.x(*args)
        return self.memo[args]
 
