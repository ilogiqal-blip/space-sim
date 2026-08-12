class gathered_data():
    def __init__(self,type):
        self.type = type
        self.data = []

    def add_data(self,type,data,time,):

        if type == self.type:
            self.data.append([time,data])
