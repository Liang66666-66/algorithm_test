maze3 = [
    [1, 1, 1, 1, 1, 1, 1, 1], # 行0
    [1, 0, 0, 0, 0, 0, 1, 1], # 行1 - (1,1)入口，往右(1,2)-(1,5)全是死胡同
    [1, 0, 1, 1, 1, 0, 1, 1], # 行2
    [1, 0, 0, 0, 0, 0, 0, 1], # 行3 - (3,1)处有分岔，往右也是死胡同
    [1, 0, 1, 0, 1, 0, 1, 1], # 行4
    [1, 0, 1, 0, 1, 0, 0, 1], # 行5 - (5,3)是关键转折点
    [1, 0, 0, 0, 1, 0, 0, 1], # 行6 - (6,6)出口
    [1, 1, 1, 1, 1, 1, 1, 1]  # 行7
]

# 调用你的函数测试
# stack_maze(maze3, 1, 1, 6, 6)
# 调用你的函数
# stack_maze(maze2, 1, 1, 8, 8)

def stack_maze(maze,x1,y1,x2,y2):
    """
    x1,y1和x2,y2代表入口和出口的坐标
    """
    x=x1
    y=y1
    maze[x][y]=2
    stack=[(x,y)]

    while not (x == x2 and y == y2):

        if maze[x-1][y]==0:
            x=x-1
            maze[x][y]=2
            stack.append((x,y))
        elif maze[x][y+1]==0:
            y=y+1
            maze[x][y]=2
            stack.append((x,y))
        elif maze[x+1][y]==0:
            x=x+1
            maze[x][y]=2
            stack.append((x,y))
        elif maze[x][y-1]==0:
            y=y-1
            maze[x][y]=2
            stack.append((x,y))
        else:
            stack.pop()
            try:
                x=stack[-1][0]
                y=stack[-1][1]
            except IndexError:
                print('未找到正确路线，迷宫无解')
                return False

    for i in stack:
        print(i)

stack_maze(maze3,1,1,6,6)