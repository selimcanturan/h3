import random

fb = int(random.randint(0, 10))
gs = int(random.randint(0, 10))

if fb>gs:
    print("fb yendi skor")
    print("fb: ",fb)
    print("gs: ",gs)
elif gs>fb:
    print("gs kazandı:")
    print("fb: ",fb)
    print("gs: ",gs)
else:
    print("berabere")