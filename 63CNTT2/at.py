from utils.readfile import read_adj, read_h
from utils.check import check_OPEN_CLOSE


def at(adj,start,stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj) #Lop cha
    g= [float('inf')] * len(adj)

    #Buoc 0:
    #khoi tao cac gia tri
    OPEN.append(start) #dua star vao OPEN
    g[start] = 0

    while len(OPEN) > 0:        #OPEN <> 0
        curr = OPEN.pop(0)      #lay ra tu dau cua OPEN
        print(f"curr : {curr}")
        CLOSE.append(curr)       # đưa đỉnh đang xét vào CLOSE
        print(f"CLOSE : {CLOSE}")
        if curr == stop:
            print('Tim thay duong di')
            #in ra duong di tu goal - start
            path = []
            idx = stop
            while idx != -1:
                # path.append(idx)
                path.insert(0, idx) #chen o dau
                idx = Parent[idx]
            # dao danh sach path
            # path.reverse()
            print(f"lo trinh: {path}")
            return

            # neu chua la dinh ket thuc, thi xet cac dinh kề kế tiếp
        for neighbor in range(len(adj)):
            if adj[curr][neighbor] == 1 and check_OPEN_CLOSE(OPEN,neighbor)==False and check_OPEN_CLOSE(CLOSE,neighbor)==False:
                Tn.append(neighbor)
                g[neighbor] = g[curr] + h[neighbor][1]
                Parent[neighbor] = curr

    print(f"Tn : {Tn}")

    #chen Tn vao dau Open
    OPEN = Tn + OPEN
    print(f"OPEN: {OPEN}")

    #Sap xep TN tang dan theo h
    OPEN_sorted = sorted(OPEN,key = lambda x: g[x],reverse = False)
    OPEN = OPEN_sorted

    print(f"OPEN sorted: {OPEN}")
    print(f"g : {g}")

    #Reset Tn trước khi quay lại từ đỉnh từ OPEN
    Tn=[]

    #Open = 0
    print(f"Khong tim thay duong di {start} -> {stop}")

if __name__ == '__main__':
    n, adj = read_adj('input/at.adj')
    print(f"Number of nodes: {n}")
    h = read_h('input/at.h')
    print(f"Heuristic values: {h}")
    for i in range(n):
        print(f"Node {i}: {adj[i]}")

    at(adj, 0, 7)