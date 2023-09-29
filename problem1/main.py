# input
student_score = 80

# Process: Your Solution Code Here
nilai_mhs = int(input("masukkan nilai mahasiswa "))

# for nilai_mhs in range (100):
if 80 <= nilai_mhs <= 100:
    print("nilai anda adalah A")
elif 65 <= nilai_mhs <= 79:
        print("nilai anda adalah B+")
elif 50 <= nilai_mhs <= 64:    
        print("nilai anda adalah B")
elif 35 <= nilai_mhs <= 49:
        print("nilai anda adalah C")
else:
        print("nilai anda adalah D")

# Output "Nilai A"