import glob

from src.utilities import convert_to, get_bit_per_sample_rates

input_folder = "input"
output_folder = "output"

all_wav_files = glob.glob(input_folder + "/*.wav")

for file in all_wav_files:
    file_name = file[len(input_folder + '/'):]

    # get_bit_per_sample_rates(file_name=file_name, input_directory=input_folder)

    convert_to(file_name=file_name,
               bits_per_sample=16,
               input_directory=input_folder,
               output_directory=output_folder)
