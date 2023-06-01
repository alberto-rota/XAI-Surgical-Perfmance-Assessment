# %%
import re, os
import utils
import pandas as pd
import numpy as np
from rich import print

def tgfr(booltxt):
    return "[green]True[/green]" if booltxt else "[red]False[/red]"

def generate_varname_json():
    head_kinematics = ["MTM_L_pos_x","MTM_L_pos_y","MTM_L_pos_z","MTM_L_rot_11","MTM_L_rot_12","MTM_L_rot_13","MTM_L_rot_21","MTM_L_rot_22","MTM_L_rot_23","MTM_L_rot_31","MTM_L_rot_32","MTM_L_rot_33","MTM_L_vel_x","MTM_L_vel_y","MTM_L_vel_z","MTM_L_rotvel_x","MTM_L_rotvel_y","MTM_L_rotvel_z","MTM_L_gripper_ang","MTM_R_pos_x","MTM_R_pos_y","MTM_R_pos_z","MTM_R_rot_11","MTM_R_rot_12","MTM_R_rot_13","MTM_R_rot_21","MTM_R_rot_22","MTM_R_rot_23","MTM_R_rot_31","MTM_R_rot_32","MTM_R_rot_33","MTM_R_vel_x","MTM_R_vel_y","MTM_R_vel_z","MTM_R_rotvel_x","MTM_R_rotvel_y","MTM_R_rotvel_z","MTM_R_gripper_ang","PSM_L_pos_x","PSM_L_pos_y","PSM_L_pos_z","PSM_L_rot_11","PSM_L_rot_12","PSM_L_rot_13","PSM_L_rot_21","PSM_L_rot_22","PSM_L_rot_23","PSM_L_rot_31","PSM_L_rot_32","PSM_L_rot_33","PSM_L_vel_x","PSM_L_vel_y","PSM_L_vel_z","PSM_L_rotvel_x","PSM_L_rotvel_y","PSM_L_rotvel_z","PSM_L_gripper_ang","PSM_R_pos_x","PSM_R_pos_y","PSM_R_pos_z","PSM_R_rot_11","PSM_R_rot_12","PSM_R_rot_13","PSM_R_rot_21","PSM_R_rot_22","PSM_R_rot_23","PSM_R_rot_31","PSM_R_rot_32","PSM_R_rot_33","PSM_R_vel_x","PSM_R_vel_y","PSM_R_vel_z","PSM_R_rotvel_x","PSM_R_rotvel_y","PSM_R_rotvel_z","PSM_R_gripper_ang",]
    head_performances = ["execution","level","total_score","respect_for_tissue","suture_or_needlehandling","time_and_motion","flow_of_operation","overall_performance","quality_of_final_product"]
    head_subtasks = ["start_frame","end_frame","label"]
    subtasks = ["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12","G13","G14","G15"]
    tasks = ["Suturing", "Knot_Tying", "Needle_Passing"]
    subjects = ["B", "C", "D", "E", "F", "G", "H", "I"]
    dataset_name = "JIGSAWS"
    executions = list(range(1,6))

    datadict = {
        "head_kinematics": head_kinematics,
        "head_performances": head_performances,
        "head_subtasks": head_subtasks,
        "subtasks": subtasks,
        "tasks": tasks,
        "subjects": subjects,
        "executions": executions,
        "dataset_name": dataset_name,
    }
    utils.dump_json(datadict, "varnames.json")


def parse(path):
    dataset_name = "JIGSAWS"

    with open(path, 'r') as file:
        datastr = file.read().rstrip()
    data_nows = re.sub("[^\S\r\n]{1,7}", ",",datastr)
    data_nows = re.sub("\n,", "\n",data_nows)[1:]
    save_path= os.path.join(dataset_name,"kinematics",path.split("\\")[-1].replace(".txt",".csv"))
    print(save_path)
    with open(save_path, 'w') as file:
        file.write(data_nows)
        
def parse_performances(path):
    dataset_name = "JIGSAWS"

    with open(path, 'r') as file:
        datastr = file.read().rstrip()
    data_nows = re.sub("[^\S\r\n]{1,7}", ",",datastr)
    data_nows = re.sub("\n,", "\n",data_nows)[1:]
    save_path= os.path.join(dataset_name,"performances",path.split("\\")[-1].replace(".txt",".csv").replace("meta_file_",""))
    print(save_path)
    with open(save_path, 'w') as file:
        file.write(data_nows)
        
def parse_subtasks(path):
    dataset_name = "JIGSAWS"

    with open(path, 'r') as file:
        datastr = file.read().rstrip()
    data_nows = re.sub("[^\S\r\n]{1,7}", ",",datastr)
    data_nows = re.sub("\n,", "\n",data_nows)[1:]
    save_path= os.path.join(dataset_name,"subtasks",path.split("\\")[-1].replace(".txt",".csv"))
    print(save_path)
    with open(save_path, 'w') as file:
        file.write(data_nows)
        
        
# Definitions of dataset variables
def dataset_parse():
        
    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()
    
    for t in tasks:
        for s in subjects:
            for e in executions:
                if t == "Knot_Tying" and s == "B" and e == 1:
                    continue
                path = os.path.join("JIGSAWS_Dataset",t,t,"kinematics","AllGestures",f"{t}_{s}00{e}.txt")
                # print(f"FROM: {path}")
                # print(f"TO: ",end="")
                parse(path)
                
def performance_label_parse():
    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()
    
    for t in tasks:
        path = os.path.join("JIGSAWS_Dataset",t,t,f"meta_file_{t}.txt")
        parse_performances(path)
        
def transcriptions_parse():
    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()
    
    for t in tasks:
        for s in subjects:
            for e in executions:
                path = os.path.join("JIGSAWS_Dataset",t,t,"transcriptions",f"{t}_{s}00{e}.txt")
                try:
                    parse_subtasks(path)
                except:
                    print(f"ERROR: {path}")

def dataset_check_health():
    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()
    NUM_VARS = len(head_kine)
    shapes = []
    nans = []
    for t in tasks:
        for s in subjects:
            for e in executions:
                    filepath = os.path.join(dataset_name,f"{t}_{s}00{e}.csv")
                    data = pd.read_csv(filepath,
                        sep=",", header=None, names=head_kine, index_col=False)
                    shapes.append(data.shape[1])
                    nans.append(data.isnull().sum().sum())
    vars_check = np.array(shapes) == NUM_VARS
    vars_check = np.all(vars_check)             
    nans_check = np.array(nans) == 0
    nans_check = np.any(nans_check) 
    utils.dump_json({"vars_check": str(vars_check), "nans_check": str(nans_check)}, "health.json")

    print(f"Data shape check (Tx{NUM_VARS}): ", tgfr(vars_check))
    print(f"Missing values check: ", tgfr(nans_check))
                    
def check_labelled_performance() :
    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()
    dataset_name = "JIGSAWS"
    labelpresence_dict = {}
    for t in tasks:
        filepath = os.path.join(dataset_name,"performances",f"{t}.csv")
        data = pd.read_csv(filepath, 
                           sep=",", header=None, names=head_perf, index_col=False)
        for s in subjects:
            for e in executions:
                labelpresence_dict[f"{t}_{s}00{e}"] = f"{t}_{s}00{e}" in list(data["execution"])
    print(labelpresence_dict)
    utils.dump_json(labelpresence_dict, "labelpresence.json")
    
check_labelled_performance()