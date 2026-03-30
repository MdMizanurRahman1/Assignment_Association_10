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



#Main program
# floor_elevator = Elevator(1, 10)
#
# floor_elevator.go_to_floor(5) #Moving up
# floor_elevator.go_to_floor(1) #Moving down





#2 Building class
class Building:
    def __init__(self, bottom, top, number_of_elevators):
        self.elevators = []

        for i in range(number_of_elevators):
            elevator_object = Elevator(bottom, top)
            self.elevators.append(elevator_object)

    def run_elevator(self, number, target_floor):
        elevator = self.elevators[number]
        elevator.go_to_floor(target_floor)


# Main program
building = Building(1, 10, 3)

building.run_elevator(0, 5)
building.run_elevator(1, 7)
building.run_elevator(0, 1)
