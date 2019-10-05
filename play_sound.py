from playsound import playsound
import random


def play_random_happy():
    happy_folder = "sounds/happy/"
    playsound(happy_folder + gen_random_mp3_name("happy_", 1, 3), False);


def play_random_sad():
    happy_folder = "sounds/sad/"
    playsound(happy_folder + gen_random_mp3_name("sad_", 1, 3), False);


def gen_random_mp3_name(first_part, min_number, max_number):
    file_number = random.randint(min_number, max_number)
    return '{}{}.mp3'.format(first_part, file_number)