import numpy as np
import json
import os


def enum(**named_values):
    return type('Enum', (), named_values)


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def bin_data(data, bin_size):
    """
    Returns data where each successive bin_amount data points
    are grouped together
    """

    if bin_size == 1:
        return data

    # It lets binning occur of the first axis for any 2D or 1D array
    if len(data.shape) == 1:
        data2 = np.zeros((data.shape[0] // bin_size))
    else:
        # print('bin size: ', bin_size, '\nshape:', data.shape)
        data2 = np.zeros((data.shape[0] // bin_size, data.shape[1]))

    for i in range(data.shape[0] // bin_size):
        data2[i] = np.mean(data[i * bin_size:(i + 1) * bin_size], axis=0)

    return data2


def save_data(data, filename, filepath):
    """
    Writes experimental data to TSV file
    """

    variables = 'Time (s)\tGeneration (V)\tPC (V)\tPL (V)'
    full_path = os.path.join(filepath, filename + '.tsv')
    np.savetxt(full_path, data, delimiter='\t', header=variables)


def save_metadata(metadata_dict, file_dir, file_name):
    """
    Writes experimental metadata to JSON file
    """
    print(metadata_dict, type(metadata_dict))
    assert type(metadata_dict) is dict

    print("data: ", metadata_dict)

    full_path = os.path.join(file_dir, file_name + '.json')
    serialised_json = json.dumps(
        metadata_dict,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )

    with open(full_path, 'w') as text_file:
            print("path: ", full_path)
            text_file.write(serialised_json)


def load_metadata(filename, filepath):
    """
    Loads metadata file and returns a python dictionary
    """
    full_filepath = os.path.join(filename, filepath)

    with open(full_filepath, 'r') as f:
        file_contents = f.read()
        metadata_dict = json.loads(file_contents)

    return metadata_dict


def load_data(full_filepath):
    """
    Loads data file and returns a numpy structured array
    """

    data_record = np.loadtxt(
        full_filepath,
        skiprows=1
    )
    # TODO: better integrate this into the data object.
    data_record.view(np.float64).reshape(data_record.shape + (-1,))
    return data_record
