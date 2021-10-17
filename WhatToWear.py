rainy = input("How's the weather? Is it raining? (y/n)").lower()
cold = input("Is it cold outside? (y/n)").lower()
if (rainy == 'y' and cold == 'y'):      #Rainy and cold
    print("You better wear a raincoat.")
elif (rainy == 'y' and cold != 'y'):    #Rainy, but warm
    print("Carry and umbrella with you.")
elif (rainy != 'y' and cold == 'y'):    #Dry, but cold
    print("Put on a jacket, its cold out!")
elif (rainy != 'y' and cold != 'y'):    #Warm and sunny
    print("Wear whatever you want, it's beautiful outside!")
