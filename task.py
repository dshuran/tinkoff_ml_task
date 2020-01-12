import time


def get_cell_changes(a, n, cell_i, cell_j):
    neigh_fish = 0
    neigh_shrimps = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            new_i = cell_i + di
            new_j = cell_j + dj
            if 0 <= new_i < n and 0 <= new_j < n:
                if a[new_i][new_j] == 's':
                    neigh_shrimps = neigh_shrimps + 1
                elif a[new_i][new_j] == 'f':
                    neigh_fish = neigh_fish + 1
    if a[cell_i][cell_j] == 'f':
        if neigh_fish == 2 or neigh_fish == 3:
            return 'f'
        else:
            return 'e'
    elif a[cell_i][cell_j] == 's':
        if neigh_shrimps == 2 or neigh_shrimps == 3:
            return 's'
        else:
            return 'e'
    elif a[cell_i][cell_j] == 'e':
        if neigh_fish == 3:
            return 'f'
        elif neigh_shrimps == 3:
            return 's'
        else:
            return 'e'
    else:
        return 'r'


def get_new_world(a, n):
    # Creating new array for the next world
    next_world = [0] * n
    for i in range(n):
        next_world[i] = [0] * n
    # Changing every cell
    for i in range(n):
        for j in range(n):
            next_world[i][j] = get_cell_changes(a, n, i, j)
    return next_world


# s - креветка (shrimp), f - рыба (fish), r - скала (rock), e - пустое место (empty)
def main():
    # Input
    n = int(input())
    a = []
    for i in range(n):
        row = input()
        row_list = list(row)
        a.append(row_list)
    # Scenario
    while True:
        a = get_new_world(a, n)
        # Output
        for i in range(n):
            for j in range(n):
                print(a[i][j], end='')
            print('\n', end='')
        time.sleep(1)
        print('------------------------\n', end='')


if __name__ == '__main__':
    main()
