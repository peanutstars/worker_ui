

class BotStatus:
    _instance = None
    
    dbg_have_job = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        pass
    
    
    def debug_have_job(self):
        self.dbg_have_job ^= True
        return self.dbg_have_job