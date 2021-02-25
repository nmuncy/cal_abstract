"""
Notes:

    1) This script will make csv files for each block.
    2) Orients from block_length (number of trials per category),
        and stim_dict.
    3) Assumes dimensional stimuli are called "foo_low" and "foo_high"
        for mapping assignment.
    4) Assumes stimuli are found in ../Stimuli/foo, will write to ../blocks/BlockX.csv

Updates:
    1) Dropped "Dim" from task
    2) randomized category assignment
        writes blocks for e/subj to ../blocks/sub-*/BlockX.csv
        receives single subj arg
        removed "dim" syntax (for syntax - v0.1)

TODO
    1) update to receive list of subj?

Usage: python job_taskSetup.py 1
"""
import os
import sys
import random
import pathlib
from random import randrange
import pandas as pd


def main(subj):
    """
    Set up

    Fix1/2 = fixed mapping
    Cond = conditional mapping

    stim_dict["Block1"]["Fix1"]: "School" = School
        stimuli will be used for fixed mapping in block1.
        Also, stimuli will be located in stim_dir/School
    """

    # set paths
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    stim_dir = os.path.join(parent_dir, "stimuli")
    stim_p = pathlib.Path(stim_dir)
    stim_rel = pathlib.Path(*stim_p.parts[5:])

    block_dir = os.path.join(parent_dir, "blocks")
    if not os.path.exists(block_dir):
        os.makedirs(block_dir)

    """
    Make stim lists per block, for psychopy.

    Will randomize L/R for fixed and dimension mappings (ref coin_toss).
    Conditional mapping is based off preceding trial.
    Dataframe will not start with conditional trial.
    """

    # set block length
    block_length = 60

    # dict of categories
    cat_list = [
        "Dangerous",
        "Healthy",
        "Old",
        "Sad",
        "School",
        "Small",
        "Smell",
        "Soft",
        "Wealth",
    ]

    # make random stim_dict
    cat_rand = random.sample(cat_list, len(cat_list))
    stim_dict = {
        "Block1": {"Fix1": cat_rand[0], "Fix2": cat_rand[1], "Cond": cat_rand[2]},
        "Block2": {"Fix1": cat_rand[3], "Fix2": cat_rand[4], "Cond": cat_rand[5]},
        "Block3": {"Fix1": cat_rand[6], "Fix2": cat_rand[7], "Cond": cat_rand[8]},
    }

    # make individual blocks
    for block in stim_dict:
        # block = "Block1"

        # randomly assign fixed mapping
        coin_toss = randrange(2)
        corr_A = "left" if coin_toss == 1 else "right"
        corr_B = "left" if corr_A == "right" else "right"

        # set up block dictionary
        #   pull random stim of length = block_length
        block_dict = {
            "Fix1": [
                [corr_A] * block_length,
                [
                    os.path.join(stim_rel, stim_dict[block]["Fix1"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Fix1"])),
                        block_length,
                    )
                ],
            ],
            "Fix2": [
                [corr_B] * block_length,
                [
                    os.path.join(stim_rel, stim_dict[block]["Fix2"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Fix2"])),
                        block_length,
                    )
                ],
            ],
            "Cond": [
                ["Cond"] * block_length,
                [
                    os.path.join(stim_rel, stim_dict[block]["Cond"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Cond"])),
                        block_length,
                    )
                ],
            ],
        }

        # make master_dict for pandas df, randomize df,
        #   don't start with cond type
        master_dict = {f"{block}Type": [], f"{block}Stim": [], f"{block}Corr": []}
        for key in block_dict.keys():
            for ind in range(0, block_length):
                master_dict[f"{block}Type"].append(key)
                master_dict[f"{block}Stim"].append(block_dict[key][1][ind])
                master_dict[f"{block}Corr"].append(block_dict[key][0][ind])

        df = pd.DataFrame.from_dict(master_dict)
        df_rand = df.sample(frac=1).reset_index(drop=True)
        while df_rand.at[0, f"{block}Type"] == "Cond":
            df_rand = df.sample(frac=1).reset_index(drop=True)

        # Set conditional response (opposite from previous)
        for ind in range(0, df_rand.shape[0]):
            if df_rand.at[ind, f"{block}Corr"] == "Cond":
                old_val = df_rand.at[ind - 1, f"{block}Corr"]
                df_rand.at[ind, f"{block}Corr"] = (
                    "left" if old_val == "right" else "right"
                )

        # write df_rand to csv
        subj_dir = os.path.join(block_dir, f"sub-{subj}")
        if not os.path.exists(subj_dir):
            os.makedirs(subj_dir)
        df_rand.to_csv(os.path.join(subj_dir, f"{block}.csv"), index=False)


if __name__ == "__main__":
    h_subj = sys.argv[1]
    main(h_subj)
