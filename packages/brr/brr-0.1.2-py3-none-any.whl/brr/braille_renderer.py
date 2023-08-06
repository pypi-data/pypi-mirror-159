#!/usr/bin/env python
from shutil import get_terminal_size
from PIL import Image, ImageStat  # type:ignore
from math import floor, ceil
import click

# from truecolor import color_print, color_text
# from rich import print
import random
import sys


def brightness(im):
    stat = ImageStat.Stat(im)
    return stat.mean[0]


def get_color_escape(r, g, b, background=False):
    return "\033[{};2;{};{};{}m".format(48 if background else 38, r, g, b)


def truecolor_print(fg, text, end="\n"):
    print(get_color_escape(*fg) + text + "\033[0m", end=end, flush=True)


def get_2by4(im, x, y):
    """finds the 2-by-4 chunk starting at (2*x,4*y) in an image"""
    return [
        (im[2 * x, 4 * y], im[2 * x + 1, 4 * y]),
        (im[2 * x, 4 * y + 1], im[2 * x + 1, 4 * y + 1]),
        (im[2 * x, 4 * y + 2], im[2 * x + 1, 4 * y + 2]),
        (im[2 * x, 4 * y + 3], im[2 * x + 1, 4 * y + 3]),
    ]


def quad_to_braille(bits):
    """turns a 2 by 4 2d array into a unicode offset"""
    ret = 0
    for i in range(3):
        ret += (2 ** (i)) * bits[i][0] + (2 ** (i + 3)) * bits[i][1]
    ret += (2**6) * bits[3][0] + (2**7) * bits[3][1]
    return ret


def braille_char(bits):
    """converts 2d iterable of truthy/falsy values to braille character"""
    return chr(ord("⠀") + quad_to_braille(bits))  # ord('⠀') == 10240


def rgb_to_bool(pixel, threshold, add_noise=False):
    average = (pixel[0] + pixel[1] + pixel[2]) / 3
    ret = average
    if add_noise:
        ret += random.random() * 64 - 32
    return ret > threshold


def chunk_to_braille(image_pixels, threshold, add_noise=False):
    lit_pixels = [
        (rgb_to_bool(a, threshold, add_noise), rgb_to_bool(b, threshold, add_noise))
        for a, b in image_pixels
    ]
    fg = get_fg_bg(lit_pixels, image_pixels)
    return lit_pixels, fg


def median_range(ls):
    ordered = sorted(ls)
    lowermid = floor((len(ls) - 1) / 2)
    uppermid = ceil((len(ls) / 2) - 0.5)
    return ordered[lowermid], ordered[uppermid]


def get_fg_bg(lit_pixels, image_pixels):
    fg_color_list = [
        image_pixels[i][j] for i in range(4) for j in range(2) if lit_pixels[i][j]
    ]
    if fg_color_list:
        fg_r = sum(a[0] for a in fg_color_list) // len(fg_color_list)
        fg_g = sum(a[1] for a in fg_color_list) // len(fg_color_list)
        fg_b = sum(a[2] for a in fg_color_list) // len(fg_color_list)
        return (fg_r, fg_g, fg_b)
    else:
        return (0, 0, 0)


@click.command()
@click.argument("file")
@click.option("--dithering", "-d", is_flag=True)
@click.option("--size", "-s", default=None)
@click.pass_context
def render(ctx, file, dithering, size):
    image = Image.open(file)
    sizeX, sizeY = image.size

    average_brightness = brightness(image)

    if size:
        sizes = size.split("x")
        try:
            assert len(sizes) == 2
            assert sizes[0].isdigit()
            assert sizes[1].isdigit()
        except AssertionError as e:
            print("Size must be on the form 'XxY'.")
            quit(1)
        max_x, max_y = int(sizes[0]), int(sizes[1])
        scalar_x = max_x / sizeX
        scalar_y = max_y / sizeY
    else:
        terminal_width, terminal_height = get_terminal_size()
        # get scalars needed to reduce to terminal size (if necessary)
        scalar_x = min(terminal_width * 2, sizeX) / sizeX
        scalar_y = min((terminal_height - 1) * 4, sizeY) / sizeY

    # scalar needed to reduce to terminal size, with original aspect ratio
    scalar = min(scalar_x, scalar_y)

    sizeX, sizeY = int(scalar * sizeX), int(scalar * sizeY)
    image = image.resize((sizeX, sizeY))

    im = image.load()

    for y in range(sizeY // 4):
        for x in range(sizeX // 2):
            image_pixels = get_2by4(im, x, y)
            braille, fg = chunk_to_braille(image_pixels, average_brightness, dithering)
            truecolor_print(fg, braille_char(braille), end="")
        print("")


if __name__ == "__main__":
    render()
