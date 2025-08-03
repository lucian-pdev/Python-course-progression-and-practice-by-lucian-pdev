# EXERCISE: GAME OF LIFE
#     Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#     Any live cell with two or three live neighbours lives on to the next generation.
#     Any live cell with more than three live neighbours dies, as if by overpopulation.
#     Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# imports
import time, os, random


# TODO:
# 1. create backend canvas
# 2. spawning mechanism
# 3. rules for living and dying
# 4. rules for reproducing
# 5. create frontend canvas
# 6. final score message
# 7. arrange into a loop
# 8. failsafe against infinity

# Backend canvas
def backend_canvas(canvas_height=50, canvas_width=100):
    """Create a 'canvas' for the loops to iterate over."""
    canvas_backend = [[False for x in range(canvas_width + 1)] for x in range(canvas_height + 1)]
    return canvas_backend


# Spawning mechanism
def spawning_creatures(canvas_backend, canvas_height, canvas_width):
    """This will find an empty 10x10 space in the canvas and spawn a 'creature' there."""
    # choose a random location to start looking into
    # TODO: REPLACE VVVVVVVVVVVVVVVVV with sample(canvas_backend, 5),
    #  and consider it to allow the verification of multiple locations with a smaller code
    coordinate_Y = random.randint(0, canvas_height)
    coordinate_X = random.randint(0, canvas_width)
    # setup search parameters
    # TODO: this is too LONG, it's ugly, find a way to shorten it or replace
    if coordinate_Y - 10 < 0:
        start_search_Y = 0
    else:
        start_search_Y = coordinate_Y - 10
    if coordinate_Y + 10 > canvas_height:
        end_search_Y = canvas_height
    else:
        end_search_Y = coordinate_Y + 10
    if coordinate_X - 10 < 0:
        start_search_X = 0
    else:
        start_search_X = coordinate_X - 10
    if coordinate_X + 10 > canvas_width:
        end_search_X = canvas_width
    else:
        end_search_X = coordinate_X + 10
    # search loop



# main block for safety
if __name__ == "__main__":
    print(f"Work in progress.")
    while True:
        try:
            canvas_height = int(input("How tall shall the canvas be?"))
            canvas_width = int(input("How wide shall the canvas be?"))
        except TypeError:
            print(f"Please input only whole, positive numbers.")
            continue
        # create canvas
        backend_canvas(canvas_height, canvas_width)