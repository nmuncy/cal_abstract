"""
Notes:

    1) Creates subject-specific Block?.csv files in
        blocks/sub-??

    2) Randomizes theme assignments to each block,
        response mapping, and stimulus order.

    3) Currently uses 3 themes for each of 3 blocks.

    4) Orients from cwd for stimuli, blocks

Usage: python job_taskSetup.py 1
"""

# %%
import os
import sys
import random
import pathlib
from random import randrange
import pandas as pd
import itertools


# %%
def main(subj):

    # set paths
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    stim_dir = os.path.join(parent_dir, "stimuli")
    stim_p = pathlib.Path(stim_dir)
    stim_rel = pathlib.Path(*stim_p.parts[5:])

    block_dir = os.path.join(parent_dir, "blocks")
    if not os.path.exists(block_dir):
        os.makedirs(block_dir)

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
        "Block1": {"Fix1": cat_rand[0], "Fix2": cat_rand[1], "Fix3": cat_rand[2]},
        "Block2": {"Fix1": cat_rand[3], "Fix2": cat_rand[4], "Fix3": cat_rand[5]},
        "Block3": {"Fix1": cat_rand[6], "Fix2": cat_rand[7], "Fix3": cat_rand[8]},
    }

    # %%
    # make individual blocks
    for block in stim_dict:
        # block = "Block1"

        # make all permutations of map/type,
        #   select one at random for map_dict
        map_options = ["A", "B", "C"]
        type_options = ["Fix1", "Fix2", "Fix3"]

        all_comb = []
        h_permut = itertools.permutations(type_options, len(map_options))
        for comb in h_permut:
            h_zip = zip(comb, map_options)
            all_comb.append(dict(list(h_zip)))

        rand_num = randrange(len(all_comb))
        map_dict = all_comb[rand_num]

        # %%
        # set up block dictionary
        #   make list of random stim of length = block_length
        #   for each type (Fix1-3), attach with mapping in format
        #   Fix1: [[mapping],[stimuli]]
        block_dict = {
            "Fix1": [
                [map_dict["Fix1"]] * block_length,
                [
                    os.path.join(stim_rel, stim_dict[block]["Fix1"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Fix1"])),
                        block_length,
                    )
                ],
            ],
            "Fix2": [
                [map_dict["Fix2"]] * block_length,
                [
                    os.path.join(stim_rel, stim_dict[block]["Fix2"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Fix2"])),
                        block_length,
                    )
                ],
            ],
            "Fix3": [
                [map_dict["Fix3"]] * block_length,
                [
                    os.path.join(stim_rel, stim_dict[block]["Fix3"], x)
                    for x in random.sample(
                        os.listdir(os.path.join(stim_dir, stim_dict[block]["Fix3"])),
                        block_length,
                    )
                ],
            ],
        }

        # %%
        # make master_dict for pandas df, randomize df
        master_dict = {f"{block}Type": [], f"{block}Stim": [], f"{block}Corr": []}
        for key in block_dict.keys():
            for ind in range(0, block_length):
                master_dict[f"{block}Type"].append(key)
                master_dict[f"{block}Stim"].append(block_dict[key][1][ind])
                master_dict[f"{block}Corr"].append(block_dict[key][0][ind])

        # %%
        # make df, randomized df
        df = pd.DataFrame.from_dict(master_dict)
        df_rand = df.sample(frac=1).reset_index(drop=True)

        # make sure same type not presented > 4 times in a row
        # TODO: instead of regenerating random dfs, could look
        #   ahead to find new response, and swap?
        status = True
        while status:

            # start counting repeats, loop through rows
            count_rep = 1
            for ind, row in df_rand.iterrows():

                # skip first row
                if ind == 0:
                    continue

                # If Corr == preceding Corr, increase counter.
                #   reshuffle df, start over if 4 repeat in a row
                if (
                    df_rand.loc[ind, f"{block}Corr"]
                    == df_rand.loc[ind - 1, f"{block}Corr"]
                ):
                    count_rep += 1
                    if count_rep == 4:
                        df_rand = df.sample(frac=1).reset_index(drop=True)
                        break
                else:
                    # reset counter when Corr changes
                    count_rep = 1

                if ind == len(df_rand) - 1:
                    status = False

        # %%
        # write df_rand to csv
        subj_dir = os.path.join(block_dir, f"sub-{subj}")
        if not os.path.exists(subj_dir):
            os.makedirs(subj_dir)
        df_rand.to_csv(os.path.join(subj_dir, f"{block}.csv"), index=False)


if __name__ == "__main__":
    h_subj = sys.argv[1]
    main(h_subj)
