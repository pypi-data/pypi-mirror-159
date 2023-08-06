#!/usr/bin/env python3

import argparse

from pathlib import Path

import imageio
import numpy

from scipy import ndimage
from skimage import exposure, filters, color, io
from cv2 import normalize, NORM_MINMAX

DEBUG = True  # Save each step in an image.


def save_image(output_file: Path, image: numpy.ndarray) -> None:
    if len(image.shape) == 3 and image.shape[-1] == 3:
        normalized_image = normalize(image,
                                     None,
                                     0,
                                     numpy.iinfo(numpy.uint8).max,
                                     NORM_MINMAX).astype(numpy.uint8)
        io.imsave(str(output_file.with_suffix('.png')),
                  normalized_image)
        return

    if image.dtype == numpy.dtype(bool):
        image = image.astype(numpy.float32)

    if len(image.shape) == 2:
        normalized_image = normalize(image,
                                     None,
                                     0,
                                     numpy.iinfo(numpy.uint16).max,
                                     NORM_MINMAX).astype(numpy.uint16)

        io.imsave(str(output_file.with_suffix('.png')),
                  normalized_image)
        return

    if image.shape[-1] == 3:
        normalized_image = normalize(image,
                                     None,
                                     0,
                                     numpy.iinfo(numpy.uint8).max,
                                     NORM_MINMAX).astype(numpy.uint8)
        imageio.volwrite(str(output_file.with_suffix('.tiff')),
                         normalized_image)
        return

    imageio.volwrite(str(output_file.with_suffix('.tiff')), image)


def segment(input_file: Path,
            output_file: Path,
            slice_number: int) -> None:
    image_3d = imageio.volread(input_file)
    assert image_3d.dtype == numpy.float32

    planar = slice_number is not None
    if planar:  # 2d
        image = numpy.take(image_3d, slice_number, axis=0)
    else:
        image = image_3d

    normalized_image = normalize(image,
                                 None,
                                 0.0,
                                 1.0,
                                 NORM_MINMAX)
    if DEBUG:
        save_image(Path("010_normalized"), normalized_image)

    threshold_image = numpy.where(normalized_image < 0.5,
                                  normalized_image, 0)

    if DEBUG:
        save_image(Path("020_threshold"), threshold_image)

    normalized_image = normalize(threshold_image,
                                 None,
                                 0.0,
                                 1.0,
                                 NORM_MINMAX)

    if DEBUG:
        save_image(Path("030_normalized"), normalized_image)

    equalized_image = exposure.equalize_hist(normalized_image)
    if DEBUG:
        save_image(Path("040_equalized"), equalized_image)

    otsu_threshold = filters.threshold_otsu(equalized_image)
    otsu_threshold_image = (equalized_image >= otsu_threshold)
    if DEBUG:
        save_image(Path("050_otsu_threshold"), otsu_threshold_image)

    # Opening is just another name of erosion followed by dilation. It
    # is useful in removing noise.
    if planar:  # 2d
        kernel = numpy.ones((5, 5), numpy.uint8)
    else:
        kernel = numpy.ones((5, 5, 5), numpy.uint8)

    opening = ndimage.binary_opening(otsu_threshold_image,
                                     kernel,
                                     iterations=2)
    if DEBUG:
        save_image(Path("060_opening"), opening)

    # Certain background area
    certain_bg = ndimage.binary_dilation(opening,
                                         kernel,
                                         iterations=3)
    if DEBUG:
        save_image(Path("070_certain_bg"), opening)

    distance_transform = ndimage.distance_transform_edt(opening)
    if DEBUG:
        save_image(Path("080_distance_transform"),
                   distance_transform)

    distance_transform = normalize(distance_transform,
                                   None,
                                   0.0,
                                   1.0,
                                   NORM_MINMAX).astype(numpy.float32)
    if DEBUG:
        save_image(Path("090_normalized"), distance_transform)

    certain_fg = distance_transform > 0.3
    if DEBUG:
        save_image(Path("100_certain_fg"), certain_fg)

    unknown = numpy.logical_and((certain_fg != 1), (certain_bg != 0))
    if DEBUG:
        save_image(Path("110_unknown"), unknown)

    markers, nr_objects = ndimage.label(certain_fg)

    print(f'{nr_objects} objects found')

    normalized_equalized_image = normalize(equalized_image,
                                           None,
                                           0,
                                           numpy.iinfo(numpy.uint16).max,
                                           NORM_MINMAX).astype(numpy.uint16)

    markers = ndimage.watershed_ift(normalized_equalized_image, markers)

    markers += 1
    markers[certain_bg == 0] = 0
    markers[unknown == 1] = 0

    labeled_image = color.label2rgb(markers,
                                    equalized_image,
                                    image_alpha=0.5,
                                    bg_label=0)

    save_image(output_file, labeled_image)


def main() -> None:
    """Automatically segment a volumetric image using watershedding."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('input_file',
                        type=Path,
                        metavar='FILE',
                        help='input image')
    parser.add_argument('output_file',
                        type=Path,
                        metavar='FILE',
                        help='output image')
    parser.add_argument('-s',
                        '--slice-number',
                        metavar='N',
                        type=int,
                        nargs='?',
                        help='segment a single slice only')

    args = parser.parse_args()

    segment(args.input_file, args.output_file, args.slice_number)


if __name__ == '__main__':
    main()
