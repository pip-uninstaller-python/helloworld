'''
print("hello Word!")
print('Hello Again')
print("I like typing this.")
print("This is fun.")
print("YAy! Printing.")
print("I'd much rather you 'not'.")
print("I 'said' do not touch this.")
print("I will now count my chickes:")
print("Hens", 25 + 30/6)
print("Roosters",100-25*3%4)
print("Now I will count the edds:")
print(3+2+1-5+4%2-1/4+6)
print("Is it true that 3+2<5-7?")
print(3+2<5-7)
print("What is 3+2?",3+2)
print("What is 5-7?",5-7)
print("oh， that's why it's False.")
print("How about some more.")
print("Is it greater?",5>-2)
print("Is it greater or equal?",5>=-2)
print("Is it less or equal?",5<=-2)

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print("There are",cars,"cars available.")
print("There are only", drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport ", carpool_capacity,"people today.")
print("We have ",passengers,"to carpool today.")
'
my_name = "Rao A. Shaw"
my_age = 21
my_height = 76
my_weight = 175
my_eyes = 'black'
my_teeth = 'yellow'
my_hair = 'Brown'
print("Let's talk about %s."%my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." %my_teeth)
print("If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height +
my_weight))

x="There are %d types of people."%10
binary = "binary"
do_not = "dont"
y= "Those who know %s and tose who %s."%(binary,do_not)
print(x)
print(y)
print("I said:%r."%x)
print("I also said: '%s'."%y)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)
w = "This is the left side of..."
e ="a string with a right side."
print(w+e)

formatter = "%r %r %r %r"
print(formatter%(1,2,3,4))
print(formatter%('one','two','three','four'))
print(formatter%(True,'False','three','four'))
print(formatter%(formatter,'formatter','three','four'))

print("How old are you?"),
age = input()
print("How tall are you?"),
height = input()
print("How much do you wight?"),
weight = input()
print("So, you're %d old, %d tall and %d heavy."%(age,height,weight))

bicycles = ['trek','cannondale','redline','specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
'''
# alien_0 = {'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])
