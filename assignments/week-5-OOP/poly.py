class Car:
    def move(self):
        return 'driving'
    
class Ship:
    def move(self):
        return 'sailing'

class Plane:
    def move(self):
        return 'flying'

for transport in [Car(),Ship(),Plane()]:
    print(transport.move())
