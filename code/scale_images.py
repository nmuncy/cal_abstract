# %%
from PIL import Image
import os
import sys


def func_job(work_dir, image_list, base_dim):
    for i in image_list:

        # get image dimensions
        image = Image.open(os.path.join(work_dir, i))
        im_width = image.size[0]
        im_height = image.size[1]

        # if largest dim is not correct
        if max(im_width, im_height) != base_dim:

            # if width is largest
            if im_width > im_height:

                # determine proportion of correct size for height
                #   (width will be base_dim)
                h_prop = base_dim / im_width
                h_adjust = int(float(im_height) * float(h_prop))

                # scale image to appropriate size
                image = image.resize((base_dim, h_adjust), Image.ANTIALIAS)
                image.save(os.path.join(work_dir, f"res_{i}"))

            # same for height
            else:
                h_prop = base_dim / im_height
                h_adjust = int(float(im_width) * float(h_prop))
                image = image.resize((h_adjust, base_dim), Image.ANTIALIAS)
                image.save(os.path.join(work_dir, f"res_{i}"))


def main():

    # main_work_dir = "/Users/nmuncy/Desktop/stimuli"
    main_work_dir = sys.argv[1]
    main_image_list = [x for x in os.listdir(main_work_dir)]
    main_image_list.sort()
    main_base_dim = 600

    func_job(main_work_dir, main_image_list, main_base_dim)


if __name__ == "__main__":
    main()


# %%
