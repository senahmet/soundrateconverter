import wavfile


def get_bit_per_sample_rates(file_name, input_directory) -> None:
    file, sample_rate, bits_per_sample = wavfile.read(input_directory + "/" + file_name, fmt="float")

    print(file_name + " >> " + str(bits_per_sample) + " bps")


def convert_to(file_name, bits_per_sample, input_directory, output_directory) -> None:
    file, sample_rate, bps = wavfile.read(input_directory + "/" + file_name, fmt="float")

    wavfile.write(output_directory + "/" + file_name[:-4] + ".wav",
                  file,
                  bits_per_sample=bits_per_sample,
                  sample_rate=sample_rate)
