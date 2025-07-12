from pynput.keyboard import Key, Listener, KeyCode

background = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]


def on_press(key):
    pos = find_2d_position(background, 1)[0]
    i, j = map(int, pos)
    print(f"key pressed: {key}, current position: {pos}")
    match key:
        case _ if key == KeyCode.from_char('w'):
            if i > 0:
                background[i - 1][j] = 1
                background[i][j] = 0

        case _ if key == KeyCode.from_char('s'):
            if i < len(background[0]) - 1:
                background[i + 1][j] = 1
                background[i][j] = 0
        case _ if key == KeyCode.from_char('a'):
            if j > 0:
                background[i][j - 1] = 1
                background[i][j] = 0
        case _ if key == KeyCode.from_char('d'):
            if j < len(background[0]) - 1:
                background[i][j + 1] = 1
                background[i][j] = 0
    print(background[0])
    print(background[1])
    print(background[2])


def find_2d_position(matrix, target):
    positions = []
    for i in range(len(matrix)):
        if len(positions) > 0:
            break
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                positions.append((i, j))
                break
    return positions


with Listener(on_press=on_press) as listener:
    listener.join()
