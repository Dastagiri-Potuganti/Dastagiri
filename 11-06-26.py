'''1.
class Password_Manager:
    def __init__(self,password):
        self.password=password
    def password_strength(self):
        if self.password.isalnum() and len(self.password)>=8:
            return "Strong Password"
        elif self.password.isalnum() and len(self.password)<8:
            return "Medium Password"

        else:
            return "Weak Password"

password=input("Enter your Password:")
pw=Password_Manager(password)
print(pw.password_strength())'''


'''2.

class Battery:
    def __init__(self,percentage):
        self.percentage=percentage
    def battery_status(self):
        if self.percentage>=80:
            return "Full Charge"
        elif self.percentage>=50 and self.percentage<80:
            return "Medium Charge"
        else:
            return "Low Battery"


percentage=int(input("Enter your Battery Percentage"))
bp=Battery(percentage)
print(bp.battery_status())'''



'''3.
class Traffic_signal:
    def __init__(self,color):
        self.color=color

    def signal(self):
        if self.color =='red':
            return 'Stop'
        elif self.color =='orange':
            return 'Ready'
        elif self.color =='green':
            return 'Go'
        else:
            return 'Incorrect Signal Color'
color=input("Enter the Traffic Signal Color:")
signal=Traffic_signal(color)
print(signal.signal())'''


'''4.


class WaterTank:
    def __init__(self,capacity):
        self.capacity=capacity

    def waterlevel(self):
        if self.capacity>=900:
            return 'Full'
        elif self.capacity>500:
            return 'Above HAlf'
        elif self.capacity==500:
            return 'Half Full'
        elif self.capacity>=200:
            return 'Below HAlf'
        else:
            return 'empty'

capacity=int(input("Enter Water Capacity Level:"))
wl=WaterTank(capacity)
print(wl.waterlevel())'''




'''5.
class Elevator:
    def __init__(self,current,nest):
        self.current=current
        self.nest=nest

    def lift(self):
        if self.nest =='up':
            return self.current+1
        elif self.nest =='down':
            return self.current-1
        else:
            return 'Incorrect Choice'

floor=int(input("Enter current floor number:"))
nt=input("Move (up/down):")
cur=Elevator(floor,nt)
print("Current Floor:",cur.lift())'''
