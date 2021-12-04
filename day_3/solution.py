import pandas as pd
import numpy as np


def find_most_common_value_in_list(binary_list):
    gamma_rate = ""
    epsilon_rate = ""
    string_length = len(binary_list[0])
    list_length = len(binary_list)
    for i in range(string_length):
        list_aggregate = 0
        for each in binary_list:
            list_aggregate += int(each[i])

        if list_aggregate > list_length / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def most_common(df, column):
    column_as_list = [int(element) for element in df[column].to_list()]
    column_sum = np.array(column_as_list).sum()
    if column_sum >= len(column_as_list)/2:
        return 1
    else:
        return 0


def least_common(df, column):
    column_as_list = [int(element) for element in df[column].to_list()]
    column_sum = np.array(column_as_list).sum()
    if column_sum >= len(column_as_list)/2:
        return 0
    else:
        return 1


def get_most_common_in_df(df):
    # most_common_bits = ""
    for i in range(df.shape[1]):
        # most_common_bits += str(most_common(df, i))
        if df.shape[0] == 1:
            return df
        df = df[df[i] == str(most_common(df, i))]
    return df


def get_least_common_in_df(df):
    # most_common_bits = ""
    for i in range(df.shape[1]):
        if df.shape[0] == 1:
            return df

        # most_common_bits += str(most_common(df, i))
        df = df[df[i] == str(least_common(df, i))]
    return df


# PART 1
df = pd.read_csv("/Users/chwir/workspace/advent_of_code/3/data.txt", header=None, names=["bits"],
                 converters={'bits': str})

print(find_most_common_value_in_list(df.bits.to_list()))

# PART 2
df = pd.DataFrame.from_records(df.bits.to_list())

print(get_most_common_in_df(df))  # returns "010101101111"
print(get_least_common_in_df(df))  # returns "100110010111"

oxygen_generator_rating = int("010101101111", 2)
CO2_scrubber_rating = int("100110010111", 2)

life_support_rating = oxygen_generator_rating * CO2_scrubber_rating
