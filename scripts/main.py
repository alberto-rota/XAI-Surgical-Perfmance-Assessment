import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update(matplotlib.rcParamsDefault)

import os

import utils
import parsing




def main():
    # Check if 'varnames.json' exists
    if not os.path.isfile("varnames.json"):
        parsing.generate_varname_json()

    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()
    
    if not os.path.isfile("health.json"):
        parsing.dataset_check_health()
        
    health = utils.load_json("health.json")
    assert health["vars_check"] == "True" and health["nans_check"] == "True", "Dataset didn't pass conformity test"

    parsing.transcriptions_parse()

    kine_kte3 = pd.read_csv(os.path.join(dataset_name, "kinematics","Knot_Tying_E003.csv"),
                   sep=",", header=None, names=head_kine, index_col=False)
    perfs = pd.read_csv(os.path.join(dataset_name, "performances","Knot_Tying.csv"),
                   sep=",", header=None, names=head_perf, index_col=False)
    print(perfs)
    return

    plt.figure(figsize=(15,6))
    plt.subplot(3,1,1)
    plt.plot(data["MTM_L_pos_x"])
    plt.grid("on")
    plt.ylabel("RotX")
    plt.subplot(3,1,2)
    plt.plot(data["MTM_L_pos_y"])
    plt.grid("on")
    plt.ylabel("RotY")
    plt.subplot(3,1,3)
    plt.plot(data["MTM_L_pos_z"])
    plt.grid("on")
    plt.ylabel("RotZ")
    plt.xlabel("Time (frames)")
    plt.show()
        
if __name__ == '__main__':
    main()