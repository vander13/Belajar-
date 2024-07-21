import random
print("SELAMAT DATANG DI GAME ULAR GOA")
posisi_ular = random.randint(1, 4)
nama_user = input (f"masukan nama anda :")

print(f'''selamat datang {nama_user } coba perhatikan dibawah ini
      (_) (_) (_) (_)''')
pilih_ular = int (input(f'''silahkan masukan goa yang mana ada ularnya :'''))

while True:
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() in ["yes", "y"]:
        print(f"Continuing nomor ular {posisi_ular}")
        break
    elif user_input.lower() in ["no", "n"]:
        print("Exiting...")
        break
    else:
        print("Invalid input. Please enter yes/no.")
        
        
# if pilih_ular == posisi_ular :
#     print(f'''SELAMAT {nama_user} anda telah memilih nomer {pilih_ular} goa yang ada ular {posisi_ular}''')
# else:
#     print(f'''ANDA GAGAL memilih ular {nama_user} posisi yang anda pilih {pilih_ular} anda akan ketemu ular
#           jika memilih posisi {posisi_ular}''')