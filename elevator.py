import random
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

#for question 3

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)


#for question 4
#this car class part is copied from previous assignment

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# Race class
class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.kilometers = kilometers
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print("Reg  Max Speed Distance")
        for car in self.cars:
            print(car.registration_number,
                    car.maximum_speed,
                    car.current_speed,
                  round(car.travelled_distance, 2))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.kilometers:
                return True
        return False


#create cars list
cars_list = []

for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_speed = random.randint(100, 200)

    car = Car(reg, max_speed)
    cars_list.append(car)



#main program
race = Race("Grand Demolition Derby", 8000, cars_list)

hours = 0

while race.race_finished() == False:
    hours = hours + 1
    race.hour_passes()

    if hours % 10 == 0:
        print("\nHour:", hours)
        race.print_status()

print("\nFinal result:")
race.print_status()







#for question 2 and 3 both
# Main program
# building = Building(1, 10, 3)
#
# building.run_elevator(0, 5)
# building.run_elevator(1, 7)
#building.run_elevator(0, 1)


#for question 3

# print("FIRE ALARM RINGING!")
#
# building.fire_alarm()
