from math import pi
#circle (area = pi * r^2; circumference = 2*pi*r)
def circle(desired_calculation):
    def area():
        r = float(input("Enter radius: "))
        answer = pi * r**2
        print(answer)

    if desired_calculation is "area":
        area()
        
#cylinder (volume = pi*r^2*h; surface area = 2*pi*r*h)

circle('area')
