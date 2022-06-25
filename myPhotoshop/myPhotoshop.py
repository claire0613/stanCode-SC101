"""
File: stanCodoshop.py
Name: claire
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """


    red_avg=red
    green_avg=green
    blue_avg=blue
    color_distance=((red_avg-pixel.red)**2+(green_avg-pixel.green)**2+(blue_avg-pixel.blue)**2)**0.5

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    sum_red = 0
    sum_green =0
    sum_blue =0
    for i in range(len(pixels)):
        sum_red += pixels[i].red
        sum_green += pixels[i].green
        sum_blue += pixels[i].blue
    avg_red=sum_red//len(pixels)
    avg_green = sum_green // len(pixels)
    avg_blue= sum_blue // len(pixels)

    return [avg_red,avg_green,avg_blue]



def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    rgb_list=get_average(pixels)
    avg_red=rgb_list[0]
    avg_green=rgb_list[1]
    avg_blue=rgb_list[2]
    pixel_list=[]
    for i in range(len(pixels)):
        pixel_and_dist=[]
        pixel_and_dist.append(get_pixel_dist(pixels[i],avg_red,avg_green,avg_blue))
        pixel_and_dist.append(pixels[i])
        pixel_list.append(pixel_and_dist)

    min_pixel_list=min(pixel_list, key=lambda lst:lst[0])[1]
    min_dis_pixel=min_pixel_list



    return  min_dis_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixel = result.get_pixel(x,y)
            image_get_best = []
            for k in range(len(images)):
                new_pixel = images[k].get_pixel(x,y)
                image_get_best.append(new_pixel)
            best=get_best_pixel(image_get_best)
            pixel.red=best.red
            pixel.green=best.green
            pixel.blue=best.blue

    # green_pixel=SimpleImage.blank(20,20,'green').get_pixel(0,0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1=get_best_pixel([green_pixel,blue_pixel,blue_pixel])
    # print(best1.red,best1.green,best1.blue)

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
