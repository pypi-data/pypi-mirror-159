#!/usr/bin/env python
from shutil import get_terminal_size
from PIL import Image, ImageStat  # type:ignore
import click

# from truecolor import color_print, color_text
# from rich import print
import random
from typing import Optional


RGBPixel = tuple[int, int, int]


def brightness_rms(im):
    grey = im.convert("L")
    stat = ImageStat.Stat(grey)

    return stat.rms[0]


def get_color_escape(r: int, g: int, b: int, background: bool = False) -> str:
    return "\033[{};2;{};{};{}m".format(48 if background else 38, r, g, b)


def truecolor_print(fg: RGBPixel, text: str) -> str:
    return get_color_escape(*fg) + text + "\033[0m"


def get_2by4(im, x: int, y: int):
    """finds the 2-by-4 chunk starting at (2*x,4*y) in an image"""
    return [
        (im[2 * x, 4 * y], im[2 * x + 1, 4 * y]),
        (im[2 * x, 4 * y + 1], im[2 * x + 1, 4 * y + 1]),
        (im[2 * x, 4 * y + 2], im[2 * x + 1, 4 * y + 2]),
        (im[2 * x, 4 * y + 3], im[2 * x + 1, 4 * y + 3]),
    ]


def quad_to_braille(bits: list[tuple[bool, bool]]) -> int:
    """turns a 2 by 4 2d array into a unicode offset"""
    ret = 0
    for i in range(3):
        ret += (2 ** (i)) * bits[i][0] + (2 ** (i + 3)) * bits[i][1]
    ret += (2**6) * bits[3][0] + (2**7) * bits[3][1]
    return ret


def braille_char(bits: list[tuple[bool, bool]]) -> str:
    """converts 2d iterable of truthy/falsy values to braille character"""
    return chr(ord("⠀") + quad_to_braille(bits))  # ord('⠀') == 10240


def rgb_to_bool(pixel: RGBPixel, threshold: float, add_noise: bool = False) -> bool:
    average = (pixel[0] + pixel[1] + pixel[2]) / 3
    ret = average
    if add_noise:
        ret += random.random() * 64 - 32
    return ret > threshold


def chunk_to_braille(
    image_pixels: list[tuple[RGBPixel, RGBPixel]],
    threshold: float,
    add_noise: bool = False,
) -> tuple[list[tuple[bool, bool]], RGBPixel]:
    lit_pixels: list[tuple[bool, bool]] = [
        (rgb_to_bool(a, threshold, add_noise), rgb_to_bool(b, threshold, add_noise))
        for a, b in image_pixels
    ]
    fg: RGBPixel = get_fg_bg(lit_pixels, image_pixels)
    return lit_pixels, fg


def get_fg_bg(
    lit_pixels: list[tuple[bool, bool]], image_pixels: list[tuple[RGBPixel, RGBPixel]]
) -> RGBPixel:
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
@click.option("--dithering", "-d", help="enables dithering", is_flag=True)
@click.option(
    "--size",
    "-s",
    metavar="<WIDTH>x<HEIGHT>",
    help="scales the output to the largest size fitting into the given width and height (in characters), while preserving aspect ratio. Defaults to terminal size.",
    default=None,
)
@click.option(
    "--threshold",
    "-t",
    help="manually set threshold to a brightness between 0 and 1. defaults to the brightness root-mean-square of FILE",
    default=None,
    type=float,
)
def cli(file: str, dithering: bool, size: Optional[str], threshold: str):
    print(render(file, dithering, size, threshold))


def render(file: str, dithering: bool, size: Optional[str], threshold: str) -> str:
    """Prints out the image FILE to the terminal, using 2x4 braille characters."""
    image = Image.open(file).convert("RGB")

    sizeX, sizeY = image.size

    if threshold:
        thres = float(threshold) * 255
    else:
        rms_brightness = brightness_rms(image)
        thres = rms_brightness
    if size:
        sizes = size.split("x")
        try:
            assert len(sizes) == 2
            assert sizes[0].isdigit()
            assert sizes[1].isdigit()
        except AssertionError:
            print("Size must be on the form 'XxY'.")
            quit(1)
        max_x, max_y = 2 * int(sizes[0]), 4 * int(sizes[1])
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
    out_string = ""
    for y in range(sizeY // 4):
        for x in range(sizeX // 2):
            image_pixels = get_2by4(im, x, y)
            braille, fg = chunk_to_braille(image_pixels, thres, dithering)
            out_string += truecolor_print(fg, braille_char(braille))
        out_string += "\n"

    return out_string


if __name__ == "__main__":
    cli()
