import nibabel as nib
import numpy as np
import scipy.io


def load_mat(file, key='scene'):
    data = scipy.io.loadmat(file)[key]
    return data


def read_file(file):
    with open(file, "r") as file:
        return [each.strip("\n") for each in file.readlines()]


def write_list(path, data_lst):
    with open(path, 'w') as file:
        for i in range(len(data_lst)):
            file.write(data_lst[i])
            if i != len(data_lst) - 1:
                file.write('\n')


def save_nii(data, path):
    """
    Convert and save as nii.
    Note that nii format needs a shape of WHD
    :param data: ndarray image
    :param path:
    """
    # [-1, -1, 1, 1] for RAI, default is LPI
    nii_file = nib.Nifti1Image(data, np.diag((-1, -1, 1, 1)))
    nib.save(nii_file, path)


def load_nii(path):
    data = nib.load(path)
    return data.get_fdata()


def save_mat(data, path, key="scene"):
    scipy.io.savemat(path, {key: data})
