from PIL import Image
import argparse
import os


def resize_image(path_to_original, path_to_result, result_size):
    with Image.open(path_to_original) as original_im:
        results_im = original_im.resize(result_size)
        results_im.save(path_to_result)


def get_final_size(original_size, result_size):
    if result_size[0] != 0 and result_size[1] != 0:
        proportionally = original_size[0]/result_size[0] ==\
                         original_size[1]/result_size[1]
        return result_size, proportionally
    new_results_size = list(result_size)
    if result_size[0] == 0:
        new_results_size[0] = int(
            original_size[0]*result_size[1]/original_size[1]
        )
    else:
        new_results_size[1] = int(
            original_size[1]*result_size[0]/original_size[0]
        )
    return new_results_size, True


def get_parser_args():
    parser = argparse.ArgumentParser(
        description="Resize image"
    )
    parser.add_argument(
        "original",
        help="path to original"
    )
    parser.add_argument(
        "results",
        nargs="?",
        help="path to results"
    )
    parser.add_argument(
        "--height",
        type=int,
        default=0,
        help="Height to results"
    )
    parser.add_argument(
        "--width",
        type=int,
        default=0,
        help="Width to results"
    )
    args = parser.parse_args()
    return args


def get_path_to_changed(path_to_original, size):
    parts_original_path = os.path.splitext(path_to_original)
    path_to_results = "{}__{}x{}{}".format(
        parts_original_path[0],
        size[0],
        size[1],
        parts_original_path[1]
    )
    return path_to_results


if __name__ == '__main__':
    arguments = get_parser_args()
    path_to_results = arguments.results
    if arguments.height == 0 and arguments.width == 0:
        exit("You have not entered the final size")
    try:
        with Image.open(arguments.original) as original_im:
            result_size, uniformity = get_final_size(
                original_im.size,
                (arguments.height, arguments.width)
            )
        if path_to_results is None:
            path_to_results = get_path_to_changed(arguments.original,
                                                  result_size)
        resize_image(arguments.original, path_to_results, result_size)
    except IOError:
        exit("Error: file {}  not found or opened".format(arguments.original))
    if not uniformity:
        print("The image was not changed proportionally")
