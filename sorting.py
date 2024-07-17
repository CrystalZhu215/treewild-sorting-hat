from pydub import AudioSegment
from random import randint

def create_sorting(n : int):
    greymaulin = AudioSegment.from_mp3("audio/greymaulin.mp3")
    rhinebelt = AudioSegment.from_mp3("audio/rhinebelt.mp3")
    seacrest = AudioSegment.from_mp3("audio/seacrest.mp3")
    wayfaren = AudioSegment.from_mp3("audio/wayfaren.mp3")
    house_samples = [greymaulin, rhinebelt, seacrest, wayfaren]

    n_per_house = [n // 4, ] * 4
    n_leftover = n % 4

    samples = []
    for i in range(n):
        house_is_valid = False
        while not house_is_valid:
            house_index = randint(0, 3)
            house = house_samples[house_index]
            if n_per_house[house_index] > 0: 
                n_per_house[house_index] -= 1
                samples.append(house)
                house_is_valid = True
            elif n_per_house[house_index] == 0 and n_leftover > 0:
                n_leftover -= 1
                n_per_house[house_index] -= 1
                samples.append(house)
                house_is_valid = True        

    # totals to twenty seconds with the house audio
    nineteen_s_silence = AudioSegment.silent(duration=19000)

    final_audio = AudioSegment.empty()
    for sample in samples:
        final_audio += sample
        final_audio += nineteen_s_silence

    return final_audio
