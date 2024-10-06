from utils.readfile import read_adj, read_h
from utils.check import check_OPEN_CLOSE

def leodoi(graph, start, goal):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(graph) #Lop cha
    print(f"Parent: {Parent}")

    #khoi tao cac gia tri
    OPEN.append(start) #dua star vao OPEN

    while len(OPEN) > 0:        #OPEN <> 0
        curr = OPEN.pop(0)      #lay ra tu dau cua OPEN
        print(f"curr : {curr}")
        CLOSE.append(curr)       # đưa đỉnh đang xét vào CLOSE
        print(f"CLOSE : {CLOSE}")
        if curr == goal:
            print('Tim thay duong di')
            #in ra duong di tu goal - start
            path = []
            idx = goal
            while idx != -1:
                # path.append(idx)
                path.insert(0, idx) #chen o dau
                idx = Parent[idx]
            # dao danh sach path
            # path.reverse()
            print(f"lo trinh: {path}")
            return
    # neu chua la dinh ket thuc, thi xet cac dinh kề kế tiếp
    for neighbor in range(len(graph)):
        if graph[curr][neighbor] == 1 and check_OPEN_CLOSE(OPEN,neighbor)==False and check_OPEN_CLOSE(CLOSE,neighbor)==False:
            Tn.append(neighbor)
            Parent[neighbor]=curr
    #in danh sach

    #Sap xep TN tang dan theo h
    Tn_sorted = sorted(Tn,key = lambda x: h[x][1],reverse = False)
    Tn = Tn_sorted
    print(f"neighbor : {Tn}")

    # chèn Tn vào đầu OPEN
    OPEN = Tn + OPEN


    #reset Tn trước khi quay lại từ đỉnh từ OPEN
    Tn=[]

    # in mot so ket qua
    print(f"OPEN: {OPEN}")
    print(f"PARENT: {Parent}")


    print("Khong tim thay duong di")

    # ham doc va in file
if __name__ == '__main__':
    n, adj = read_adj('input/leodoi.adj')
    print(f"Number of nodes: {n}")
    h = read_h('input/leodoi.h')
    print(f"Heuristic values: {h}")
    for i in range(n):
        print(f"Node {i}: {adj[i]}")

    leodoi(adj, 0, 6)