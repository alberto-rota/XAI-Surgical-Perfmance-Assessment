import pandas as pd
import numpy as np
import os
import utils
import seaborn as sns
import matplotlib.pyplot as plt
from rich import print

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
        "expertise":[],
        "score":[]
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
        dfdict["score"].append(perflabels[perflabels["execution"]==fname]["total_score"].values[0])
        
    frame = pd.DataFrame(dfdict)

    return frame

def compute_medians(perf_df) :
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
        "expertise":[],
        "score":[]
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
        dfdict["mtmr_p"].append(np.median(np.linalg.norm(f[["MTM_R_pos_x","MTM_R_pos_y","MTM_R_pos_z"]],axis=1)))
        dfdict["mtmr_v"].append(np.median(np.linalg.norm(f[["MTM_R_vel_x","MTM_R_vel_y","MTM_R_vel_z"]],axis=1)))
        dfdict["mtmr_av"].append(np.median(np.linalg.norm(f[["MTM_R_rotvel_x","MTM_R_rotvel_y","MTM_R_rotvel_z"]],axis=1)))
        dfdict["mtml_p"].append(np.median(np.linalg.norm(f[["MTM_L_pos_x","MTM_L_pos_y","MTM_L_pos_z"]],axis=1)))
        dfdict["mtml_v"].append(np.median(np.linalg.norm(f[["MTM_L_vel_x","MTM_L_vel_y","MTM_L_vel_z"]],axis=1)))
        dfdict["mtml_av"].append(np.median(np.linalg.norm(f[["MTM_L_rotvel_x","MTM_L_rotvel_y","MTM_L_rotvel_z"]],axis=1)))
        dfdict["psmr_p"].append(np.median(np.linalg.norm(f[["PSM_R_pos_x","PSM_R_pos_y","PSM_R_pos_z"]],axis=1)))
        dfdict["psmr_v"].append(np.median(np.linalg.norm(f[["PSM_R_vel_x","PSM_R_vel_y","PSM_R_vel_z"]],axis=1)))
        dfdict["psmr_av"].append(np.median(np.linalg.norm(f[["PSM_R_rotvel_x","PSM_R_rotvel_y","PSM_R_rotvel_z"]],axis=1)))
        dfdict["psml_p"].append(np.median(np.linalg.norm(f[["PSM_L_pos_x","PSM_L_pos_y","PSM_L_pos_z"]],axis=1)))
        dfdict["psml_v"].append(np.median(np.linalg.norm(f[["PSM_L_vel_x","PSM_L_vel_y","PSM_L_vel_z"]],axis=1)))
        dfdict["psml_av"].append(np.median(np.linalg.norm(f[["PSM_L_rotvel_x","PSM_L_rotvel_y","PSM_L_rotvel_z"]],axis=1)))
        dfdict["expertise"].append(perflabels[perflabels["execution"]==fname]["level"].values[0])
        dfdict["score"].append(perflabels[perflabels["execution"]==fname]["total_score"].values[0])
    frame = pd.DataFrame(dfdict)
    return frame
    
def compact_lr(perf_df):
    head_kine, head_perf, head_subt, subtasks, tasks, subjects, executions, dataset_name = utils.load_json("varnames.json").values()

    dfdict = {
        "execution":perf_df["execution"],
        "mtm_p":[],
        "mtm_v":[],
        "mtm_av":[],
        "psm_p":[],
        "psm_v":[],
        "psm_av":[],
        "expertise":[],
        "score":[]
    }
    df_right = perf_df[["execution","mtmr_p","mtmr_v","mtmr_av","psmr_p","psmr_v","psmr_av","expertise","score"]].copy()
    df_right.rename(columns = {"mtmr_p":"mtm_p","mtmr_v":"mtm_v","mtmr_av":"mtm_av","psmr_p":"psm_p","psmr_v":"psm_v","psmr_av":"psm_av"},inplace=True)
    df_right["hand"]='right'
    df_left = perf_df[["execution","mtml_p","mtml_v","mtml_av","psml_p","psml_v","psml_av","expertise","score"]].copy()
    df_left.rename(columns = {"mtml_p":"mtm_p","mtml_v":"mtm_v","mtml_av":"mtm_av","psml_p":"psm_p","psml_v":"psm_v","psml_av":"psm_av"},inplace=True)
    df_left["hand"]='left'
    # print(df_right)
    # print(df_left)
    return pd.concat([df_right,df_left])

        
def plot_variances(variances):
    sns.set_theme()
    ax=sns.catplot(data=variances,x="expertise",y="mtm_p",kind="violin",hue="hand", split=True)
    ax.set(ylabel="MTM Position Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="mtm_v",kind="violin",hue="hand", split=True)
    ax.set(ylabel="MTM Velocity Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="mtm_av",kind="violin",hue="hand", split=True)
    ax.set(ylabel="MTM AngularVelocity Variance") 
    
    # ax=sns.catplot(data=variances,x="expertise",y="mtml_p",kind="violin",hue="hand", split=True)
    # ax.set(ylabel="MTML Position Variance")
    
    # ax=sns.catplot(data=variances,x="expertise",y="mtml_v",kind="violin",hue="hand", split=True)
    # ax.set(ylabel="MTML Velocity Variance")
    
    # ax=sns.catplot(data=variances,x="expertise",y="mtml_av",kind="violin",hue="hand", split=True)
    # ax.set(ylabel="MTML AngularVelocity Variance") 
    
    ax=sns.catplot(data=variances,x="expertise",y="psm_p",kind="violin",hue="hand", split=True)
    ax.set(ylabel="PSM Position Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="psm_v",kind="violin",hue="hand", split=True)
    ax.set(ylabel="PSM Velocity Variance")
    
    ax=sns.catplot(data=variances,x="expertise",y="psm_av",kind="violin",hue="hand", split=True)
    ax.set(ylabel="PSM AngularVelocity Variance") 
    
    # ax=sns.catplot(data=variances,x="expertise",y="psml_p",kind="violin",hue="hand", split=True)
    # ax.set(ylabel="PSML Position Variance")
    
    # ax=sns.catplot(data=variances,x="expertise",y="psml_v",kind="violin",hue="hand", split=True)
    # ax.set(ylabel="PSML Velocity Variance")
    
    # ax=sns.catplot(data=variances,x="expertise",y="psml_av",kind="violin",hue="hand", split=True)
    # ax.set(ylabel="PSML AngularVelocity Variance") 
    plt.show()
    
def plot_variances_scores(variances):
    sns.set_theme()
    sns.scatterplot(data=variances,x="score",y="mtm_p",) #hue="hand")
#    ax.set(ylabel="MTM Position Variance")

    sns.scatterplot(data=variances,x="score",y="mtm_v",) #hue="hand")
#    ax.set(ylabel="MTM Velocity Variance")

    sns.scatterplot(data=variances,x="score",y="mtm_av",) #hue="hand")
#    ax.set(ylabel="MTM AngularVelocity Variance") 

    # sns.scatterplot(data=variances,x="score",y="mtml_p",) #hue="hand")
    ## ax.set(ylabel="MTML Position Variance")
    
    # sns.scatterplot(data=variances,x="score",y="mtml_v",) #hue="hand")
    ## ax.set(ylabel="MTML Velocity Variance")
    
    # sns.scatterplot(data=variances,x="score",y="mtml_av",) #hue="hand")
    ## ax.set(ylabel="MTML AngularVelocity Variance") 
    
    sns.scatterplot(data=variances,x="score",y="psm_p",) #hue="hand")
#    ax.set(ylabel="PSM Position Variance")

    sns.scatterplot(data=variances,x="score",y="psm_v",) #hue="hand")
#    ax.set(ylabel="PSM Velocity Variance")

    sns.scatterplot(data=variances,x="score",y="psm_av",) #hue="hand")
#    ax.set(ylabel="PSM AngularVelocity Variance") 

    # sns.scatterplot(data=variances,x="score",y="psml_p",) #hue="hand")
    ## ax.set(ylabel="PSML Position Variance")
    
    # sns.scatterplot(data=variances,x="score",y="psml_v",) #hue="hand")
    ## ax.set(ylabel="PSML Velocity Variance")
    
    # sns.scatterplot(data=variances,x="score",y="psml_av",) #hue="hand")
    ## ax.set(ylabel="PSML AngularVelocity Variance") 
    plt.show()