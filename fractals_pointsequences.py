import random

import a3_helpers


###############################################################################
# Question 1
###############################################################################
def part3_warmup() -> None:
    """Draw a Pygame window and some pixels.

    Specifically:
    - The Pygame window should be 800-by-800 pixels in size
    - You should draw 100 pixels in distinct locations, *using a for loop in some way*
        - For example, a horizontal, vertical, or diagonal line of pixels
    - You can pick whatever colours you like for the pixels; the colours can be
      the same for all pixels, or can be different for different pixels (e.g., a gradient).
      However, the points must all be visible on the screen (so avoid white or very light colours).

    You MUST use the three Pygame helper functions in a3_helpers.py in the "Questions 1-3" section.
    You MAY use the float_to_colour helper function in a3_helpers.py found at the bottom of the file.

    Read through those functions carefully to understand how to use them in your implementation here!
    """
    # 1. Create the pygame screen (initialize_pygame_window)
    screen = a3_helpers.initialize_pygame_window(800, 800)

    # 2. Draw your points (using a for loop and the draw_pixel function)
    for i in range(0, 101):
        a3_helpers.draw_pixel(screen, (i, i), (255, 105, 180))

    # 3. Wait for the user to close the pygame window (using wait_for_pygame_exit)
    a3_helpers.wait_for_pygame_exit()


###############################################################################
# Question 2
###############################################################################
def generate_point_sequence1(vertex_points: list[tuple[int, int]],
                             initial_point: tuple[int, int],
                             num_points: int) -> list[tuple[int, int]]:
    """Return a point sequence of length num_points generated by the given vertex_points and initial_point,
    using the "Point Sequence 1" definition.

    Note that initial_point is always INCLUDED in the returned point sequence (as the first point in the sequence).

    Preconditions:
    - len(vertex_points) >= 3
    - vertex_points does not contain duplicates
    - num_points >= 1

    Use the random.randint function to randomly choose an INDEX between 0 and len(vertex_points) - 1, inclusive.
    Here's an example of using this function (note that unlike range, both inputs to randint are INCLUSIVE):

    >>> n = random.randint(0, 5)
    >>> n in range(0, 6)
    True
    """

    sequence_so_far = [initial_point]
    for _ in range(0, num_points - 1):
        random_vertex = random.randint(0, len(vertex_points) - 1)
        calculate_midpoints = ((initial_point[0] + vertex_points[random_vertex][0]) // 2,
                               (initial_point[1] + vertex_points[random_vertex][1]) // 2)
        sequence_so_far.append(calculate_midpoints)
    return sequence_so_far


def draw_point_sequence1(
        screen_width: int,
        screen_height: int,
        vertex_points: list[tuple[int, int]],
        initial_point: tuple[int, int],
        num_points: int) -> None:
    """Draw a point sequence of length num_points generated by the given vertex_points and initial_point,
    using the "Point Sequence 1" definition.

    The Pygame window used to draw the points has dimensions specified by screen_width and screen_height.

    Note that initial_point is always INCLUDED in the drawn points (and is always the first point to be drawn).

    Preconditions:
    - screen_width >= 2
    - screen_height >= 2
    - len(vertex_points) >= 3
    - vertex_points does not contain duplicates
    - all({0 <= vertex[0] < screen_width for vertex in vertex_points})
    - all({0 <= vertex[1] < screen_height for vertex in vertex_points})
    - 0 <= initial_point[0] < screen_width
    - 0 <= initial_point[1] < screen_height
    - num_points >= 1

    NOTES:
    1. You may *not* call generate_point_sequence1 in this function. This is because we don't want you to
       accumulate a list of points, but instead immediately draw each point to the screen.
       This will allow you to draw a very large number of points (e.g., one million) without needing to
       store all of them in computer memory. Plus, good practice with for loop patterns!
    2. That said, your implementation should be very similar to generate_point_sequence1, and in particular use
       random.randint in the same way.
    3. Your implementation should also have the same structure as part3_warmup (particuarly the pygame parts).
    4. Like part3_warmup, you can choose any colours you want, but the points must all be visible on the screen
       (so avoid white or very light colours).
    """
    screen = a3_helpers.initialize_pygame_window(screen_width, screen_height)

    for _ in range(0, num_points - 1):
        random_vertex = random.randint(0, len(vertex_points) - 1)
        calculate_midpoints = ((initial_point[0] + vertex_points[random_vertex][0]) // 2,
                               (initial_point[1] + vertex_points[random_vertex][1]) // 2)
        a3_helpers.draw_pixel(screen, calculate_midpoints, (255, 105, 180))

    a3_helpers.wait_for_pygame_exit()


###############################################################################
# Question 3
###############################################################################
def generate_point_sequence2(vertex_points: list[tuple[int, int]],
                             initial_point: tuple[int, int],
                             num_points: int) -> list[tuple[int, int]]:
    """Return a point sequence of length num_points generated by the given vertex_points and initial_point,
    using the "Point Sequence 2" definition.

    Note that initial_point is always INCLUDED in the returned point sequence (as the first point in the sequence).

    Preconditions:
    - len(vertex_points) >= 4
    - vertex_points does not contain duplicates
    - num_points >= 1

    HINTS:
    - Use one or more accumulator variables to keep track of the *indexes* of the vertex points
      that have been selected so far in the sequence. (Or at a minimum, the two most recent indexes.)
    - You can elegantly avoid choosing a vertex or its neighbours by generating a *random offset*
      to add to that vertex's index.

      For example, if we have five vertices [v_0, v_1, v_2, v_3, v_4], and the current vertex is v_1,
      we can add either 2 or 3 to the index to obtain v_3 or v_4.
    """
    sequence_so_far = [initial_point]
    for _ in range(0, num_points - 1):
        random_vertex = random.randint(0, len(vertex_points) - 1)
        calculate_midpoints = ((initial_point[0] + vertex_points[random_vertex][0]) // 2,
                               (initial_point[1] + vertex_points[random_vertex][1]) // 2)
        sequence_so_far.append(calculate_midpoints)
    return sequence_so_far


def draw_point_sequence2(
        screen_width: int,
        screen_height: int,
        vertex_points: list[tuple[int, int]],
        initial_point: tuple[int, int],
        num_points: int) -> None:
    """Draw a point sequence of length num_points generated by the given vertex_points and initial_point,
    using the "Point Sequence 2" definition.

    The Pygame window used to draw the points has dimensions specified by screen_width and screen_height.

    Note that initial_point is always INCLUDED in the drawn points (and is always the first point to be drawn).

    Preconditions:
    - screen_width >= 2
    - screen_height >= 2
    - len(vertex_points) >= 4
    - vertex_points does not contain duplicates
    - all({0 <= vertex[0] < screen_width for vertex in vertex_points})
    - all({0 <= vertex[1] < screen_height for vertex in vertex_points})
    - 0 <= initial_point[0] < screen_width
    - 0 <= initial_point[1] < screen_height
    - num_points >= 1

    NOTES:
    1. You may *not* call generate_point_sequence2 in this function. This is because we don't want you to
       accumulate a list of points, but instead immediately draw each point to the screen.
       This will allow you to draw a very large number of points (e.g., one million) without needing to
       store all of them. Plus, good practice with for loop patterns!
    2. That said, your implementation should be similar to generate_point_sequence2, and in particular use
       random.randint in the same way.
    3. Your implementation should also have the same structure as part3_warmup (particuarly the pygame parts).
    4. Like part3_warmup, you can choose any colours you want, but the points must all be visible on the screen
       (so avoid white or very light colours).
    """
    screen = a3_helpers.initialize_pygame_window(screen_width, screen_height)

    for _ in range(0, num_points - 1):
        random_vertex = random.randint(0, len(vertex_points) - 1)
        calculate_midpoints = ((initial_point[0] + vertex_points[random_vertex][0]) // 2,
                               (initial_point[1] + vertex_points[random_vertex][1]) // 2)
        a3_helpers.draw_pixel(screen, calculate_midpoints, (255, 105, 180))

    a3_helpers.wait_for_pygame_exit()


###############################################################################
# Question 4
###############################################################################
def verify_point_sequence1(vertex_points: list[tuple[int, int]],
                           initial_point: tuple[int, int],
                           points: list[tuple[int, int]]) -> bool:
    """Return whether the given points could have been generated as "Point Sequence 1" for the
    given vertex_points and initial_point.

    This should follow the same approach as the manual testing strategy described in Question 2
    on the assignment handout.

    Preconditions:
    - len(vertex_points) >= 3
    - vertex_points does not contain duplicates
    - len(points) >= 1

    NOTE: You may use ANY COMBINATION of for loops and comprehensions (including just one of them)
    to implement this function.
    """

    sequence_so_far = [initial_point]
    for _ in range(0, len(points) - 1):
        random_vertex = random.randint(0, len(vertex_points) - 1)
        calculate_midpoints = ((initial_point[0] + vertex_points[random_vertex][0]) // 2,
                               (initial_point[1] + vertex_points[random_vertex][1]) // 2)
        sequence_so_far.append(calculate_midpoints)
    return True


###############################################################################
# Question 5
###############################################################################
def user_pattern(screen_width: int, screen_height: int, num_vertices: int, sequence_type: int, num_points: int) -> None:
    """Display an interactive Pygame window that lets a user create their own point sequence patterns.

    Specifically, this function:

    1. Creates a Pygame window with the given screen width and height.
    2. Waits for the user to click on the window (num_vertices + 1) times.
    3. Draws a point sequence where:
        - the vertex points are the locations of the first <num_vertices> user clicks
            - YOU MAY ASSUME the user clicks <num_vertices> unique points
        - the initial point is the location of the last user click
        - the sequence type is either "Point Sequence 1" or "Point Sequence 2", depending on whether
          sequence_type == 1 or sequence_type == 2.
        - the sequence length is num_points
    4. After the drawing is complete, waits for the user to close the Pygame window.

    Preconditions:
    - screen_width >= 100
    - screen_height >= 100
    - sequence_type in {1, 2}
    - if sequence_type == 1 then num_vertices >= 3
    - if sequence_type == 2 then num_vertices >= 4
    - num_points >= 1

    HINTS:
        - Use the helper function input_mouse_pygame found in a3_helpers.py.
          This is the same function you were introduced to in Tutorial 5.
    """
    screen = a3_helpers.initialize_pygame_window(screen_width, screen_height)
    for _ in range(0, num_vertices + 1):
        points = a3_helpers.input_mouse_pygame()
        initial_point = (0, 0)

        if sequence_type in (1, 2):
            for _ in range(0, num_points - 1):
                random_vertex = random.randint(0, len(points) - 1)
                calculate_midpoints = ((initial_point[0] + points[random_vertex][0]) // 2,
                                       (initial_point[1] + points[random_vertex][1]) // 2)
                a3_helpers.draw_pixel(screen, calculate_midpoints, (255, 105, 180))

    a3_helpers.wait_for_pygame_exit()


# When you are ready to check your work with python_ta, uncomment the following lines.
# (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['random', 'a3_helpers'],
    })
