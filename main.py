import os.path
import sys
import glob

from src.utilities import convert_to, get_bit_per_sample_rates

input_folder = "input"
output_folder = "output"

all_wav_files = glob.glob(input_folder + "/*.wav")


def types() -> None:
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

        print("INFO: Input folder created >> " + os.getcwd() + "\\" + input_folder)

    for file in all_wav_files:
        file_name = file[len(input_folder + '/'):]

        get_bit_per_sample_rates(file_name=file_name, input_directory=input_folder)


def convert() -> None:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in all_wav_files:
        file_name = file[len(input_folder + '/'):]

        convert_to(file_name=file_name,
                   bits_per_sample=16,
                   input_directory=input_folder,
                   output_directory=output_folder)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
