#https://github.com/Fcrentsil
#6934121
#List of availabel cars and their prices
cars ={
'Lamborghini':105600,'Honda Civic':200500,'Toyota Camry':700098, \
'Tesla Model 3':800950,'Toyota Rav 4': 60500,'Honda CR-V':268800,\
'Tesla Model Y': 56589000,'Kia EV6':10000000,'2021 Tesla Model 3': 4000457,\
'Mercerdes-Benz C-Class':478930,'Toyota Yaris':5378202,'BMW 3 series':367403738,\
'Kia Sportage':5373837,'Hyundai Tuscon':3000000,'Audi Q3':400000,
'Honda Accord':10333000,'BMWi4': 4000890,
'Volkswagen Tiguan':470000,'Mercedes-Benz GLA':5000000,'Ferrari LaFerrari':6600000,\
'De Tomaso P72':3000200,'McLaren Elva':600900,'Czinger 21C':1200000,'Ferrari Monza':50005000,\
'Hennessey Venom F5':400500,'Bentley Bacalar':3900000,'Aston Martin Vulcan':320000,\
'Gordon Murray T.50':7000900,'Lamborghini Countauch':5600000,'Mercedes-AMG Project One':40006000}

#Get user input for for car name
prompt=input('Enter a car_name ')
#Check if car name is in the list of cars available
if prompt  in cars:
    print('Yes,the car you requested is available '  )
    #if car name is present, get its price
    price= cars[prompt]
    print(' The price of the car is Dollars ' + str(price))
else:
    #if car name is not present, inform the customer
    print('Sorry,that car is currently not available. ' ' These are the cars currently available: ' )
    a = cars.keys()
    print(a)
    