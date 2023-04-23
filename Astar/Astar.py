import math
class State:
    def __init__(self,value,level,fval):
        self.value = value
        self.level = level
        self.fval = fval
    def generate_children(self):
 
        x,y = self.search_space(self.value,'0')
        coor_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in coor_list:
            child = self.valid_position(self.value,x,y,i[0],i[1])
            if child is not None:
                child_node = State(child,self.level+1,0)
                children.append(child_node)
               
        return children
     
    def search_space(self,puz,x):
        for i in range(0,len(self.value)):
            for j in range(0,len(self.value)):
                if puz[i][j] == x:
                    return i,j
    def valid_position(self,puz,x1,y1,x2,y2):
       
        if x2 >= 0 and x2 < len(self.value) and y2 >= 0 and y2 < len(self.value):
            temp_puz = []
            temp_puz = self.copy_matrix(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
    def copy_matrix(self,root):
 
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
           
   
 
class Eight_Puzzle:

    def __init__(self,size):
        self.n = size
        self.fringe = []
        self.explored = []
       
    def get_values(self):
            create_matrix = []
            for i in range(0,self.n):
                store_value = input().split(",")
                create_matrix.append(store_value)
            return create_matrix
       
    def h_misplaced_tiles(self,initial_state,goal_state):
            mis_tiles = 0
            for i in range(0,self.n):
                for j in range(0,self.n):
                    if initial_state[i][j] != goal_state[i][j] and initial_state[i][j] != '0':
                        mis_tiles += 1
 
            return mis_tiles
   
    def h_manhattan_dist(self,initial_state,goal_state):
        manh_dist = []
        manhattan_dist = 0
        for i in range (0,3):
            for j in range (0,3):
                manh_dist.append(goal_state[i][j])
 
        for i in range (0,3):
            for j in range (0,3):
                current_coor = initial_state[i][j]
                x_coor = i
                y_coor = j
                index = manh_dist.index(current_coor)
                x_goal, y_goal = index//3,index%3
                if current_coor != '0':
                    manhattan_dist += (math.fabs(x_goal - x_coor) + math.fabs(y_goal - y_coor))
       
        return manhattan_dist
    def f_manhattan_dist(self,initial_state,goal_state):
        g_x = initial_state.level
        h_x = self.h_manhattan_dist(initial_state.value,goal_state)
        f_x = g_x + h_x
        print("\ng(x): ",g_x)
        print("h(x): ",h_x)
        print("f(x): ",f_x)
        return f_x
   
    def f_misplace_tiles(self,initial_state,goal_state):
        g_x = initial_state.level
        h_x = self.h_misplaced_tiles(initial_state.value,goal_state)
        f_x = g_x + h_x
        print("\ng(x): ",g_x)
        print("h(x): ",h_x)
        print("f(x): ",f_x)
        return f_x
   
    def f1(self,initial_state,goal_state):
        g_x = initial_state.level
        h_x = self.h_manhattan_dist(initial_state.value,goal_state)
        f_x = g_x + h_x
        return f_x,g_x,h_x
   
    
    def stage_process(self):
            counter = 0
            print("\nInitial State \nEnter values comma separated 3 in each row(e.g: 1,2,3): ")
            initial_state = self.get_values()
            print("\nGoal State \nEnter values comma separated 3 in each row(e.g: 4,5,6): ")        
            goal_state = self.get_values()
            print("\n Select the heuristic function h(x): \n1. Manhattan Distance \n2. Misplaced Tiles ")
            choice = int(input())
           
            initial_state = State(initial_state,0,0)
            if choice==1:
                initial_state.fval = self.f_manhattan_dist(initial_state,goal_state)
            else:
                initial_state.fval = self.f_misplace_tiles(initial_state,goal_state)
           
            self.fringe.append(initial_state)
            print("\n\n")
            while True:
               
                cur = self.fringe[0]
                if counter == 0:
                    counter =1
                else:
                    print("")
                    print("  |  ")
                    print("  |  ")
                    print("  |  ")
                    print(" \\/ \n")
                   
                for i in cur.value:
                    for j in i:
                        print(j,end=" ")
                    print("")
               
                if choice==1:
                    if(self.h_manhattan_dist(cur.value,goal_state) == 0):
                        break
                else:
                    if(self.h_misplaced_tiles(cur.value,goal_state) == 0):
                        break
                       
                print("\nBelow are the values of all the child nodes that are added to the fringe but will expand the node with minimum value of f(x): ")
                for i in cur.generate_children():
                    if choice == 1:
                        i.fval = self.f_manhattan_dist(i,goal_state)
                    else:
                        i.fval = self.f_misplace_tiles(i,goal_state)
                       
                    self.fringe.append(i)
                   
                self.explored.append(cur)
                del self.fringe[0]
               
                self.fringe.sort(key = lambda x:x.fval,reverse=False)
 
            f,g,h = obj.f1(cur,goal_state)
            print("\ng(x): ",g)
            print("h(x): ",h)
            print("f(x):",f)
            print("Path Cost: ",f)
            print("Generated Nodes: ",len(self.fringe))
            print("Expanded Nodes: ",len(self.explored))
               
 
obj = Eight_Puzzle(3)
obj.stage_process()
