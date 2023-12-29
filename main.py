import sys

def create_table(width: int, height: int):
    table = []
    for _ in range(height):  # loop to create lists A.K.A rows
        row = ["X" for _ in range(width)]  # nested loop to add columns for each row
        table.append(row)

    return table


def place_ball(table: list, x: int, y: int):
    start = x, y  # starting position, used in another function

    if x >= 0 and y >= 0 and x < len(table[0]) and y < len(table):  # check if coordinates are within the table
        table[y][x] = "8"
        return table, start
    else:
        print("Choose numbers within the table.")
        quit()


def move_ball(placed_ball: list, start: tuple, direction: str, steps: int):
    directions = {
        "UP": (0, -1),
        "DOWN": (0, 1),
        "RIGHT": (1, 0),
        "LEFT": (-1, 0),
        "UP-RIGHT": (1, -1),
        "UP-LEFT": (-1, -1),
        "DOWN-RIGHT": (1, 1),
        "DOWN-LEFT": (-1, 1)
    }

    x, y = start
    dx, dy = directions[direction]
    height = len(placed_ball)  # number of rows
    width = len(placed_ball[0])  # number of columns

    for step in range(steps):
        next_x = x + dx
        next_y = y + dy

        if next_x < 0 or next_x >= width:
            dx = -dx
            next_x = x + dx

        if next_y < 0 or next_y >= height:
            dy = -dy
            next_y = y + dy

        x, y = next_x, next_y

    return print(f"\nFinal spot = Column: {x}, Row: {y}")

if __name__ == '__main__':

    width = int(sys.argv[1])
    height = int(sys.argv[2])
    x = int(sys.argv[3])
    y = int(sys.argv[4])
    direction = sys.argv[5]
    steps = int(sys.argv[6])


    table = create_table(width, height)
    placed_ball, start = place_ball(table, x, y)
    print(placed_ball)
    move_ball(placed_ball, start, direction, steps)

