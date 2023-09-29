bilangan = int(input("masukkan bilangan "))
def faktor(bilangan):
    for i in range (1, bilangan +1):
      if bilangan % i == 0:
        print("faktor bilangan ini adalah", i)
faktor(bilangan)