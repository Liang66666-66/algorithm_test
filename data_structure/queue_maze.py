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

    q=deque([(x1,y1)]) #创建一个队列，用来保存当前所有路径的末端，起始时只有一个末端即起点
    maze[x1][y1]=2 #标记已经走过的坐标

    path={(x1,y1):None} #创建一个字典，用来保存每个所走过坐标的上一个坐标，起始坐标没有上一个坐标，即为None

    while q: #循环终止条件：队列为空，即所有末端都为死路，此时此题无解

        #队列中出现终点即结束循环
        if (x2,y2) in q:
            print('找到了出口')
            break

        #每次出队列一个末端坐标
        currNode=q.popleft()

        #判断该出列的末端坐标的四个方向是否有路
        if maze[currNode[0]-1][currNode[1]]==0:
            q.append((currNode[0]-1,currNode[1]))#添加新的末端到队列中
            maze[currNode[0]-1][currNode[1]]=2#标记新增末端的坐标
            path[(currNode[0]-1,currNode[1])]=currNode#添加键值对到字典(新增末端坐标：他的上一个坐标)

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
    
    else: #循环结束前未执行break会跳到此处
        print('无解，全部死路')
        return 
    

    best_path=[(x2,y2)] #创建一个列表，用来存储最短路径

    node=(x2,y2) #从终点坐标开始寻找
    while path[node] is not None: #循环终止条件：找到起点
        node=path[node] #每次搜寻上一个坐标
        best_path.append(node) 
    
    best_path.reverse() #倒转列表
    print(best_path)

queze_maze(maze4,1,1,6,6)
