from time import sleep


class TrafficLight:
    __colors = {'красный': 4, 'жёлтый': 2, 'зелёный': 3}

    def running(self):
        # while True: # если добавить то бесконечно запускает
        for color, time in TrafficLight.__colors.items():
            print(f'{color} {time} сек')
            sleep(time)
    # хотел добавить print('end'), но и так видно что зеленый висит 3 сек,
    # когда вылазит Process finished with exit code 0


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
