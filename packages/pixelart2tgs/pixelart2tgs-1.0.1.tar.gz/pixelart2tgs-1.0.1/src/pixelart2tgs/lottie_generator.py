from .converter_types import *
from . import templates

from .shape_generator import generate_shapes
from .contour_generator import generate_contours
from .chain_generator import generate_chains


def get_image_sizes(source: SourceAnimationType) -> tuple[int, int]:
    return source[1][0].shape[:2]


def shift_and_scale(source: SourceAnimationType):
    """
    Generates shift of the whole animation to center it
    and scale to fill most of the avaliable sticker's space.
    """
    x, y = get_image_sizes(source)

    scale = 512 / max(x, y)
    if x > y:
        shift = ((1 - y / x) * 256, 0.0)
    else:
        shift = (0.0, (1 - x / y) * 256)
    return shift, scale


def generate_lottie(source: SourceAnimationType, label: str):
    """
    Generates final lottie json by applying functions from all modules.
    """
    durations, shape_dict = generate_shapes(source)

    shift, scale = shift_and_scale(source)
    length = round(sum(durations), 1)

    groups = []

    for shape, frames in shape_dict.items():
        contours = generate_contours(shape)
        chains = generate_chains(frames)

        groups += [
            chain.generate_group(contours, durations, scale)
            for chain in chains
        ]

    return templates.lottie(length, label, shift, scale, groups)