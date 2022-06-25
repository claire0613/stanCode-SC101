"""
File: babygraphics.py
Name: Claire
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1300
CANVAS_HEIGHT = 900
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 5
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_space=width/len(YEARS)
    coordinate=GRAPH_MARGIN_SIZE+x_space*year_index
    return coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for index in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH,index),0,get_x_coordinate(CANVAS_WIDTH,index),CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH,index)+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,text=YEARS[index],anchor=tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for name_count in range(len(lookup_names)):
        lookup_name=lookup_names[name_count]
        year0=str(YEARS[0])
        if year0 in name_data[lookup_name]:
            first_year_rank= int(name_data[lookup_name][year0])+GRAPH_MARGIN_SIZE
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 0) + TEXT_DX,first_year_rank,
                               text=lookup_name+" "+str(first_year_rank-GRAPH_MARGIN_SIZE), fill=COLORS[name_count%len(COLORS)], anchor=tkinter.SW)

        else:
            first_year_rank='*'
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 0) + TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                               text=lookup_name + first_year_rank, fill=COLORS[name_count%len(COLORS)], anchor=tkinter.SW)


        for index in range(len(YEARS)-1):
            year=str(YEARS[index+1])
            if year in name_data[lookup_name]:
                second_year_rank = int(name_data[lookup_name][year])+GRAPH_MARGIN_SIZE
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index), first_year_rank,
                                   get_x_coordinate(CANVAS_WIDTH, index + 1), second_year_rank, fill=COLORS[name_count%len(COLORS)])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH,index+1)+TEXT_DX,second_year_rank,
                               text=lookup_name+" "+str(second_year_rank-GRAPH_MARGIN_SIZE),fill=COLORS[name_count%len(COLORS)],anchor=tkinter.SW)


                first_year_rank = second_year_rank


            else:
                second_year_rank = '*'

                if (first_year_rank == '*'):
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index),  CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, index + 1), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       fill=COLORS[name_count%len(COLORS)])
                else:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index), first_year_rank,
                                       get_x_coordinate(CANVAS_WIDTH, index + 1), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       fill=COLORS[name_count%len(COLORS)])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH,index+1)+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                               text=lookup_name+" "+str(second_year_rank),fill=COLORS[name_count%len(COLORS)],anchor=tkinter.SW)
                first_year_rank = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE










# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
