# %%
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update(matplotlib.rcParamsDefault)

import os

import utils
import parsing
import processing
from rich import print

def main():
    # Check if 'varnames.json' exists
    if not os.path.isfile("varnames.json"):
        parsing.generate_varname_json()
    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()
    # Check if 'health.json' exists
    if not os.path.isfile("health.json"):
        parsing.dataset_check_health()
    health = utils.load_json("health.json")
    assert health["vars_check"] == "True" and health["nans_check"] == "True", "Dataset didn't pass conformity test"
    # Check  if 'labelpresence.json' exists
    if not os.path.isfile("labelpresence.json"):
        parsing.check_labelled_performance()
    
    kine_kte3 = pd.read_csv(os.path.join(dataset_name, "kinematics","Knot_Tying_E003.csv"),
                   sep=",", header=None, names=head_kine, index_col=False)
    perfs = pd.read_csv(os.path.join(dataset_name, "performances","Knot_Tying.csv"),
                   sep=",", header=None, names=head_perf, index_col=False)
    
    variances = processing.compute_variances(perfs)
    medians = processing.compute_medians(perfs)
    compact_medians = processing.compact_lr(medians)
    compact_variances = processing.compact_lr(variances)
    # print(compact_variances)
    # print(compact_medians)
    processing.plot_variances_distributions(compact_variances)
    processing.plot_variances_scores(compact_variances)
    
    processing.plot_variances_distributions(compact_medians)
    processing.plot_variances_scores(compact_medians)
    plt.show()    
    
if __name__ == '__main__':
    main()
# 
# %%
