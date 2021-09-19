import winsound
import random

play = ['C:/Users/umur/Documents/GitHub/hekaton_2021/1.wav',
'C:/Users/umur/Documents/GitHub/hekaton_2021/2.wav',
'C:/Users/umur/Documents/GitHub/hekaton_2021/3.wav',
'C:/Users/umur/Documents/GitHub/hekaton_2021/4.wav',
'C:/Users/umur/Documents/GitHub/hekaton_2021/5.wav']

while True:
    filename = (random.choice(play))
    winsound.PlaySound(filename, winsound.SND_FILENAME)