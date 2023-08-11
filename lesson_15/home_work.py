class Train:
    def __init__(self):
        self.train_cars = ['Locomotive']

    def __add__(self, other):
        self.train_cars.append(other)

    def __len__(self):
        return len(self.train_cars) - 1

    def travel_to(self, station:str):
        for train_car in range(len(self.train_cars)):
            if train_car == 0:
                continue
            for passenger in range(len(self.train_cars[train_car])):
                if self.train_cars[train_car][passenger]["destination"] == station:
                    print(f'train leave passenger from train car: {train_car}, his name: {self.train_cars[train_car][passenger]["name"]}')
                    self.train_cars[train_car].leave_passenger(passenger-1)

    def new_passenger(self, name_value, destination_value, train_car_number, place):
        print(f'To train coming passenger, they have {place} place in train car №{train_car_number}, his name:  {name_value}, ')
        self.train_cars[train_car_number].add_passenger(name_value, destination_value, place)



class TrainCar:
    def __init__(self, number_of_train_car):
        self.number_of_train_car = number_of_train_car
        self.passengers = []

    def add_passenger(self, name_value, destination_value, place):
        self.passengers.append(
            {'name': name_value, 'destination': destination_value, 'place': place})

    def leave_passenger(self, value):
        self.passengers.pop(value)

    def __getitem__(self, item):
        return self.passengers[item - 1]

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        answer = ''
        for i in range(len(self.passengers)):
            answer += f'passenger №{i+1}:\n"name": {self.passengers[i]["name"]}\n"destination": {self.passengers[i]["destination"]},\n"place": {self.passengers[i]["place"]}\n'
        return answer


train = Train()
train_car1 = TrainCar('1')
train_car1.add_passenger('Tom', 'London', 1)
train_car1.add_passenger('Tomas', 'Manchester', 2)
train_car2 = TrainCar('2')
train_car2.add_passenger('Tom', 'London', 1)
train_car2.add_passenger('Tomas', 'Manchester', 2)
train + train_car1
train + train_car2
print(len(train))
print(len(train_car1))
print(train.train_cars[1])
train.travel_to('London')
print(train.train_cars[1])
train.new_passenger('Tom', 'Liverpool', 1, 1)
print(train.train_cars[1])
print(train.train_cars[2])

