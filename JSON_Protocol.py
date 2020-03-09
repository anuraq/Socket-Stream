import pickle

class json_protocol():
    def __init__(self, sender, reciever ,type, data):
        self.sender = sender
        self.reciever = reciever
        self.type = type
        self.data = data

    def build_data(self):
        json_p = pickle.dumps({ "sender" : self.sender, "reciever" : self.reciever, "data_type" : self.type, "data" : self.data})
        return json_p

if __name__ == "__main__":
    j = json_protocol("anurag", "aditya", "text", "hello bro")
    data = j.build_data()
    buff = bytes(f'{len(data):<{10}}', 'utf-8')
    data = buff + data
    print(data)
