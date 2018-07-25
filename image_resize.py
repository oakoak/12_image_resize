from PIL import Image
import argparse
import os


def resize_image(initial_image, result_size):
    return initial_image.resize(result_size)


def get_final_size(original_height, original_width, height, width, scale):
    if height != 0 and width != 0:
        proportionally = (original_height/height ==
                          original_width/width)
        return (height, width), proportionally
    if scale != 0:
        height = int(original_height * scale)
        width = int(original_width * scale)
    elif height == 0:
        height = int(original_height*width/original_width)
    else:
        width = int(original_width*height/original_height)
    return (height, width), True


def get_parser_args():
    parser = argparse.ArgumentParser(
        description="Resize image"
    )
    parser.add_argument(
        "original",
        help="path to original"
    )
    parser.add_argument(
        "output",
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
    parser.add_argument(
        "--scale",
        type=float,
        default=0,
        help="Compression ratio"
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


def arguments_validation(height, width, scale):
    if height == 0 and width == 0 and scale == 0:
        return"You have not entered the final size"
    if height < 0 or width < 0 or scale < 0:
        return "You input incorrect values"
    if scale != 0 and (height != 0 or width != 0):
        return "You input incompatible arguments"
    return ""


def main():
    arguments = get_parser_args()
    path_to_results = arguments.output
    error_validation = arguments_validation(
            arguments.height,
            arguments.width,
            arguments.scale
    )
    if error_validation is not None:
        exit(error_validation)
    try:
        with Image.open(arguments.original) as original_im:
            height, width = original_im.size
            result_size, uniformity = get_final_size(
                height,
                width,
                arguments.height,
                arguments.width,
                arguments.scale
            )
            new_image = resize_image(original_im, result_size)
        if path_to_results is None:
            path_to_results = get_path_to_changed(
                arguments.original,
                result_size
            )
        new_image.save(path_to_results)
    except IOError:
        exit("Error: file {}  not found or opened".format(arguments.original))
    if not uniformity:
        print("The image was not changed proportionally")


if __name__ == "__main__":
    main()
