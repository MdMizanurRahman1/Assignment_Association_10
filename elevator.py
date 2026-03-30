#1
class Elevator:
    def __init__(self, bottom, top):
        self.current_floor = bottom
        self.bottom = bottom
        self.top = top

    def floor_up(self):
        self.current_floor += 1
        print("Floor Number:", self.current_floor)

    def floor_down(self):
        self.current_floor -= 1
        print("Floor Number:", self.current_floor)

    def go_to_floor(self, target):
        while self.current_floor < target:    #Moving up
            self.floor_up()

        while self.current_floor > target:    #Moving down
            self.floor_down()


#Main programme
floor_elevator = Elevator(1, 10)

floor_elevator.go_to_floor(5) #Moving up
floor_elevator.go_to_floor(1) #Moving down



