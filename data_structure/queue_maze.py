from collections import deque

maze4 = [
    [1, 1, 1, 1, 1, 1, 1, 1], # 行0
    [1, 0, 0, 0, 0, 0, 1, 1], # 行1 - (1,1)入口，往右(1,2)-(1,5)全是死胡同
    [1, 0, 1, 1, 1, 0, 1, 1], # 行2
    [1, 0, 0, 0, 0, 0, 0, 1], # 行3 - (3,1)处有分岔，往右也是死胡同
    [1, 0, 1, 0, 1, 0, 1, 1], # 行4
    [1, 0, 1, 0, 1, 0, 1, 1], # 行5 - (5,3)是关键转折点
    [1, 0, 0, 0, 1, 0, 0, 1], # 行6 - (6,6)出口
    [1, 1, 1, 1, 1, 1, 1, 1]  # 行7
]

def queze_maze(maze,x1,y1,x2,y2):
    """
    x1,y1和x2,y2代表入口和出口的坐标
    """
    q=deque([(x1,y1)])
    maze[x1][y1]=2

    path={(x1,y1):None}
    

    while q:
        if (x2,y2) in q:
            print('找到了出口')
            break
        currNode=q.popleft()

        if maze[currNode[0]-1][currNode[1]]==0:
            q.append((currNode[0]-1,currNode[1]))
            maze[currNode[0]-1][currNode[1]]=2
            path[(currNode[0]-1,currNode[1])]=currNode

        if maze[currNode[0]][currNode[1]+1]==0:
            q.append((currNode[0],currNode[1]+1))
            maze[currNode[0]][currNode[1]+1]=2
            path[(currNode[0],currNode[1]+1)]=currNode

        if maze[currNode[0]+1][currNode[1]]==0:
            q.append((currNode[0]+1,currNode[1]))
            maze[currNode[0]+1][currNode[1]]=2
            path[(currNode[0]+1,currNode[1])]=currNode

        if maze[currNode[0]][currNode[1]-1]==0:
            q.append((currNode[0],currNode[1]-1))
            maze[currNode[0]][currNode[1]-1]=2
            path[(currNode[0],currNode[1]-1)]=currNode
    
    else:
        print('无解，全部死路')
    
    print(path)
    best_path=[(x2,y2)]
    node=(x2,y2)

    while path[node] is not None:
        node=path[node]
        best_path.append(node)
    
    best_path.reverse()
    print(best_path)



queze_maze(maze4,1,1,6,6)
