

class gathered_data():
    def __init__(self):
        self.change = []
        self.time = []

    def add_data(self,data,time,):
            
            self.time.append(time)
            self.change.append(data)

    def clear_data(self):

        self.change = []
        self.time = []
