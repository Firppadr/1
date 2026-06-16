import time
import winsound
print('ZA WARUUUDOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!')
winsound.PlaySound('Faldar\\time_comence.wav',winsound.SND_FILENAME)
for sec in range(9):
    time.sleep(1)
    sec = sec+1
    print(f'{sec}')
    winsound.PlaySound('Faldar\\relojo.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
    if sec > 8:
        print('O Tempo volta a passar!')
        winsound.PlaySound('Faldar\\time_comence.wav',winsound.SND_FILENAME)