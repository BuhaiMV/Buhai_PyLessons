class TrafficLight:
    def __init__(self):
        self.__color = 'green'

    def __str__(self):
        return f'Hi I`m traffic_light instance, and my current color_status is {self.__color}'


traffic_light_1 = TrafficLight()
print(traffic_light_1)
