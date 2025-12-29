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

def stack_maze(maze,x1,y1,x2,y2):
    """
    x1,y1和x2,y2代表入口和出口的坐标
    """
    # 创建x,y两个指针
    x=x1
    y=y1
    maze[x][y]=2 #标记起点为2（走过的点均标记为2）
    stack=[(x,y)] #创建栈保存当前路线

    while not (x == x2 and y == y2): #循环终止条件：走到终点

        #按照上右下左的顺序判断当前所在坐标的四个方向是否有路
        if maze[x-1][y]==0:
            x=x-1 #移动指针
            maze[x][y]=2 #标记已经走过的路线
            stack.append((x,y)) #持续进栈
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
        # 走到死胡同（四个方向均不为0)
        else: 
            stack.pop() #后退一步(出栈)
            #指针回到后退一步之后的当前栈顶
            try:
                x=stack[-1][0] 
                y=stack[-1][1]
            #若后退一步后栈顶为空，则代表退回起点，死局
            except IndexError:
                print('未找到正确路线，迷宫无解')
                return False

    for i in stack:#打印栈
        print(i)

stack_maze(maze3,1,1,6,6)