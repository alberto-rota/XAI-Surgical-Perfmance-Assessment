import pandas as pd
import numpy as np
import os
import utils
import seaborn as sns
import matplotlib.pyplot as plt

def compute_variances(perf_df) :
    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()

    dfdict = {
        "execution":perf_df["execution"],
        "mtmr_p":[],
        # "mtmr_r":[],
        "mtmr_v":[],
        "mtmr_av":[],
        "mtml_p":[],
        # "mtml_r":[],
        "mtml_v":[],
        "mtml_av":[],        
        "psmr_p":[],
        # "psmr_r":[],
        "psmr_v":[],
        "psmr_av":[],
        "psml_p":[],
        # "psml_r":[],
        "psml_v":[],
        "psml_av":[],
        "expertise":[]
    }
    
    perflabels = pd.concat([
        pd.read_csv(os.path.join("JIGSAWS", "performances", "Knot_Tying.csv"),names=head_perf),
        pd.read_csv(os.path.join("JIGSAWS", "performances", "Needle_Passing.csv"),names=head_perf),
        pd.read_csv(os.path.join("JIGSAWS", "performances", "Suturing.csv"),names=head_perf),
        ])
    
    # print(perflabels)
    # print(perflabels[perflabels["execution"]=="Knot_Tying_B001"]["level"])
    
    for fname in perf_df["execution"]:
        f = pd.read_csv(os.path.join("JIGSAWS", "kinematics", f"{fname}.csv"),
                        sep=",", header=None, names=head_kine, index_col=False)
        dfdict["mtmr_p"].append(np.var(np.linalg.norm(f[["MTM_R_pos_x","MTM_R_pos_y","MTM_R_pos_z"]],axis=1)))
        dfdict["mtmr_v"].append(np.var(np.linalg.norm(f[["MTM_R_vel_x","MTM_R_vel_y","MTM_R_vel_z"]],axis=1)))
        dfdict["mtmr_av"].append(np.var(np.linalg.norm(f[["MTM_R_rotvel_x","MTM_R_rotvel_y","MTM_R_rotvel_z"]],axis=1)))
        dfdict["mtml_p"].append(np.var(np.linalg.norm(f[["MTM_L_pos_x","MTM_L_pos_y","MTM_L_pos_z"]],axis=1)))
        dfdict["mtml_v"].append(np.var(np.linalg.norm(f[["MTM_L_vel_x","MTM_L_vel_y","MTM_L_vel_z"]],axis=1)))
        dfdict["mtml_av"].append(np.var(np.linalg.norm(f[["MTM_L_rotvel_x","MTM_L_rotvel_y","MTM_L_rotvel_z"]],axis=1)))
        dfdict["psmr_p"].append(np.var(np.linalg.norm(f[["PSM_R_pos_x","PSM_R_pos_y","PSM_R_pos_z"]],axis=1)))
        dfdict["psmr_v"].append(np.var(np.linalg.norm(f[["PSM_R_vel_x","PSM_R_vel_y","PSM_R_vel_z"]],axis=1)))
        dfdict["psmr_av"].append(np.var(np.linalg.norm(f[["PSM_R_rotvel_x","PSM_R_rotvel_y","PSM_R_rotvel_z"]],axis=1)))
        dfdict["psml_p"].append(np.var(np.linalg.norm(f[["PSM_L_pos_x","PSM_L_pos_y","PSM_L_pos_z"]],axis=1)))
        dfdict["psml_v"].append(np.var(np.linalg.norm(f[["PSM_L_vel_x","PSM_L_vel_y","PSM_L_vel_z"]],axis=1)))
        dfdict["psml_av"].append(np.var(np.linalg.norm(f[["PSM_L_rotvel_x","PSM_L_rotvel_y","PSM_L_rotvel_z"]],axis=1)))
        dfdict["expertise"].append(perflabels[perflabels["execution"]==fname]["level"].values[0])
    frame = pd.DataFrame(dfdict)

    return frame
    
def plot_variances(variances):
    sns.set_theme()
    ax=sns.catplot(data=variances,x="expertise",y="mtmr_p",kind="violin")
    ax.set(ylabel="MTMR Position Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="mtmr_v",kind="violin")
    ax.set(ylabel="MTMR Velocity Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="mtmr_av",kind="violin")
    ax.set(ylabel="MTMR AngularVelocity Variance") 
    
    ax=sns.catplot(data=variances,x="expertise",y="mtml_p",kind="violin")
    ax.set(ylabel="MTML Position Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="mtml_v",kind="violin")
    ax.set(ylabel="MTML Velocity Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="mtml_av",kind="violin")
    ax.set(ylabel="MTML AngularVelocity Variance") 
    
    ax=sns.catplot(data=variances,x="expertise",y="psmr_p",kind="violin")
    ax.set(ylabel="PSMR Position Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="psmr_v",kind="violin")
    ax.set(ylabel="PSMR Velocity Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="psmr_av",kind="violin")
    ax.set(ylabel="PSMR AngularVelocity Variance") 
    
    ax=sns.catplot(data=variances,x="expertise",y="psml_p",kind="violin")
    ax.set(ylabel="PSML Position Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="psml_v",kind="violin")
    ax.set(ylabel="PSML Velocity Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="psml_av",kind="violin")
    ax.set(ylabel="PSML AngularVelocity Variance") 
    plt.show()
