tal1=0
tal2=1
tal=1
for a in range(20):
    print(tal, "\t:", tal1)
    tal+=1
    print(tal, "\t:", tal2)
    tal+=1
    tal1+=tal2
    tal2+=tal1