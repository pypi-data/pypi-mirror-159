import os

import pandas as pd
from pymbse.commons import text_file


def read_figures_of_merit_table(self) -> pd.DataFrame:
    output_path = os.path.join(self.root_dir, self.input_folder_rel_dir, self.output_file)
    return self.read_figures_of_merit_table_from_file(output_path)


def read_figures_of_merit_table_from_file(output_path):
    with open(output_path, 'r') as output:
        output_file_content = output.read().split('\n')
    keys = output_file_content[0].split(' ')
    keys = [key for key in keys if key != '']
    values = output_file_content[1].split(' ')
    values = [float(value) for value in values if value != '']
    key_value = {key: value for key, value in zip(keys, values)}
    return pd.DataFrame(key_value, index=[0])


def convert_figures_of_merit_to_dict(fom_df: pd.DataFrame) -> dict:
    return fom_df.to_dict('records')[0]


def prepare_force_file(self, input_force_file: str, output_force_file: str) -> None:
    """ Method preparing a force file for ANSYS from a ROXIE Lorentz force file, .force2d

    :param input_force_file: a name of a ROXIE Lorentz force file
    :param output_force_file: a name of an output file for ANSYS
    """
    input_force_file_path = os.path.join(self.root_dir, self.input_folder_rel_dir, input_force_file)
    output_force_file_path = os.path.join(self.root_dir, self.input_folder_rel_dir, output_force_file)

    convert_roxie_force_file_to_ansys(input_force_file_path, output_force_file_path)


def read_multiple_ansys_figures_of_merit(root_dir: str, n_outputs: int) -> list:
    fom_dcts = []

    for i in range(n_outputs):
        ansys_output_file = 'vallone_%d.out' % i
        ansys_output_path = os.path.join(root_dir, ansys_output_file)
        if os.path.isfile(ansys_output_path) and os.path.getsize(ansys_output_path) > 0:
            fom_df = read_figures_of_merit_table_from_file(ansys_output_path)
            if fom_df['seqv'].values[0] < 1e-6:
                fom_dct = {"seqv": float('nan')}
            else:
                fom_dct = convert_figures_of_merit_to_dict(fom_df)
        else:
            fom_dct = {"seqv": float('nan')}

        fom_dcts.append(fom_dct)

    return fom_dcts


def convert_roxie_force_file_to_ansys(input_force_file_path: str, output_force_file_path: str) -> None:
    """ Static method preparing a force file for ANSYS from a ROXIE Lorentz force file, .force2d

    :param input_force_file_path: a name of a ROXIE Lorentz force file
    :param output_force_file_path: a name of an output file for ANSYS
    """
    force_txt = text_file.readlines(input_force_file_path)

    ansys_force = []
    for force_txt_el in force_txt:
        row_float = [float(el) for el in force_txt_el.replace('\n', '').split(' ') if el != '']
        ansys_force.append('nodeNum = NODE(%f, %f, 0.0)' % tuple(row_float[:2]))
        ansys_force.append('F,nodeNum,FX, %f' % row_float[2])
        ansys_force.append('F,nodeNum,FY, %f' % row_float[3])

    text_file.writelines(output_force_file_path, ansys_force)
