def myPog(food, vegan=False):
    if(vegan):
        print("Soja" + food)
    else:
        print(food)

myPog("Mjölk", True)