"""
Notes:

This script will make csv files for each block.

Orients from block_length (number of trials per category),
    and stim_dict.

Assumes dimensional stimuli are called "foo_low" and "foo_high"
    for mapping assignment.

Assumes stimuli are found in ../Stimuli/foo, will write to ../blocks/BlockX.csv

Update: dropped "Dim" from task
"""
# %%
import os
import random
from random import randrange
import pandas as pd


# %%
def main():
    """
    Set up

    Fix1/2 = fixed mapping
    Cond = conditional mapping

    stim_dict["Block1"]["Fix1"]: "School" = School
        stimuli will be used for fixed mapping in block1.
        Also, stimuli will be located in stim_dir/School
    """
    block_length = 10

    stim_dict = {
        "Block1": {"Fix1": "School", "Fix2": "Dangerous", "Cond": "Small"},
        "Block2": {"Fix1": "Old", "Fix2": "Healthy", "Cond": "Wealth"},
        "Block3": {"Fix1": "Sad", "Fix2": "Temperature", "Cond": "Smell"},
    }

    # set paths
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stim_dir = os.path.join(parent_dir, "stimuli")
    block_dir = os.path.join(parent_dir, "blocks")
    if not os.path.exists(block_dir):
        os.makedirs(block_dir)

    # %%
    """
    Make stim lists per block, for psychopy.

    Will randomize L/R for fixed and dimension mappings (ref coin_toss).
    Conditional mapping is based off preceding trial.
    Dataframe will not start with conditional trial.
    """
    for block in stim_dict:
        # block = "Block3"

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
                    os.path.join(stim_dir, stim_dict[block]["Fix1"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Fix1"])),
                        block_length,
                    )
                ],
            ],
            "Fix2": [
                [corr_B] * block_length,
                [
                    os.path.join(stim_dir, stim_dict[block]["Fix2"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Fix2"])),
                        block_length,
                    )
                ],
            ],
            "Cond": [
                ["Cond"] * block_length,
                [
                    os.path.join(stim_dir, stim_dict[block]["Cond"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Cond"])),
                        block_length,
                    )
                ],
            ],
        }

        # # Make dim list
        # dim_list = [
        #     os.path.join(stim_dir, stim_dict[block]["Dim"], x)
        #     for x in random.sample(
        #         os.listdir(os.path.join(stim_dir, stim_dict[block]["Dim"])),
        #         block_length,
        #     )
        # ]

        # # set dim corr off of coin_toss
        # #   just reuse corr_A/B
        # dim_corr = []
        # for stim in dim_list:
        #     h_corr = corr_A if "_Low." in stim else corr_B
        #     dim_corr.append(h_corr)

        # # add dim to block_dict
        # block_dict["Dim"] = [dim_corr, dim_list]

        # %%
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

        # %%
        # write df_rand to csv
        df_rand.to_csv(os.path.join(block_dir, f"{block}.csv"), index=False)


if __name__ == "__main__":
    main()

# %%
