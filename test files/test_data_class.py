class gathered_data():
    def __init__(self,type):
        self.type = type
        self.data = [0,]
        self.entry_no = 0

    def add_data(self,type,data,time):

        if type == self.type:

            self.entry_no += 1
            self.data[0] = self.entry_no
            self.data.append([time,data])

test_data = gathered_data("test")

test_data.add_data("test",0.5,1)
test_data.add_data("test",0.6,2)
test_data.add_data("test",0.7,4)
print(test_data.data[0])


for i in range(test_data.data[0]):
    print(test_data.data[i+1])
