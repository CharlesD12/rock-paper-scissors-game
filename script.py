import utils
# import module random
import random

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

while True:
    print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
    player_hand = int(input('Masukkan nomor (0-2): '))

    if utils.validate(player_hand):
        # Tetapkan nomor acak antara 0 dan 2 ke computer_hand menggunakan randint
        computer_hand = random.randint(0,2)
    
        utils.print_hand(player_hand, player_name)
        utils.print_hand(computer_hand, 'Komputer')

        result = utils.judge(player_hand, computer_hand)
        print('Hasil: ' + result)

        play_again = input("Ingin bermain lagi? (Yes = y / No = n) : ")
        if play_again == "y":
            continue
        else:
            print("Terima kasih telah bermain!")
            break
    else:
        print('Mohon masukkan nomor yang benar!')
