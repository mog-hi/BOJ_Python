from copy import deepcopy
cube = [[3,5,2,4],[2,5,3,4],[0,5,1,4],[0,4,1,5],[0,2,1,3],[0,3,1,2]]
cube_color = [[['w']*3 for _ in range(3)], [['y']*3 for _ in range(3)], [['r']*3 for _ in range(3)],
              [['o']*3 for _ in range(3)], [['g']*3 for _ in range(3)], [['b']*3 for _ in range(3)]]
change = [[0, -1], [-1,2], [2, -1],[-1,0]]
def turn(where, dir):
    global cube_color
    temp = deepcopy(cube_color)
    for i in range(4):
        x = cube[where][i]
        if dir == '+':
            to = cube[where][(i-1+4)%4]
        else:
            to = cube[where][(i+1+4)%4]
        where_x = cube[x].index(where)
        a, b = change[where_x]
        where_to = cube[to].index(where)
        c, d = change[where_to]
        print(x, to)
        print(where_x, a, b, where_to, c, d)
        if a == -1:
            for j in range(3):
                if c == -1:
                    temp[x][j][b] = cube_color[to][j][d]
                else:
                    temp[x][j][b] = cube_color[to][c][j]
        else:
            for j in range(3):
                if c == -1:
                    temp[x][a][j] = cube_color[to][j][d]
                else:
                    temp[x][a][j] = cube_color[to][c][j]
    cube_color = temp

# 1
# turn(4, '-')
# 2
# turn(2, '+')
# turn(3, '+')

#3
turn(0, '-')
turn(1, '-')
for i in range(6):
    print(cube_color[i])
turn(4, '+')
# turn(5, '+')
for i in range(6):
    print(cube_color[i])