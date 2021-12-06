import numpy as np


fish_ages = []
with open('data.txt') as f:
    fish_ages_input = np.array(f.readline().split(","), dtype=int)

##### PART 1 #####
number_of_days = 80

fish_ages = fish_ages_input

for i in range(number_of_days):
    number_of_zeros = np.bincount(fish_ages)[0]
    reduced_by_day = fish_ages - 1
    reduced_by_day = reduced_by_day[reduced_by_day >= 0].tolist()
    if number_of_zeros != 0:
        new_fishes = [8] * number_of_zeros
        reset_fishes = [6] * number_of_zeros
        fish_ages = np.array(reduced_by_day + new_fishes + reset_fishes)
    else:
        fish_ages = np.array(reduced_by_day)

print(len(fish_ages))


##### PART 2 #####


def transcribe_bins_to_days(fishes_bin_count, bin_count_fish_ages):
    for i in range(len(fishes_bin_count)):
        if i < len(bin_count_fish_ages):
            fishes_bin_count[i] = bin_count_fish_ages[i]
    return fishes_bin_count


number_of_days = 256
fish_ages = fish_ages_input
fishes_bin_count = np.array([0] * 9)
bin_count_fish_ages = np.bincount(fish_ages)
fishes_bin_count = transcribe_bins_to_days(fishes_bin_count, bin_count_fish_ages)

for i in range(number_of_days):
    new_fishes = fishes_bin_count[0]
    shifted_bin_count = np.concatenate((fishes_bin_count[1:], np.array([0])))
    if new_fishes > 0:
        shifted_bin_count[8] += new_fishes
        shifted_bin_count[6] += new_fishes
    fishes_bin_count = shifted_bin_count

print(sum(fishes_bin_count))
