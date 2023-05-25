class Logger:

    def __init__(self):
        self.map = {} 
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.map: 
            if self.map[message][0] <= timestamp < self.map[message][1]:
                return False
        
        self.map[message] = [timestamp, timestamp + 10] 
        return True
        