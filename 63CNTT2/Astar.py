from utils.readfile import read_adj, read_h
from utils.check import check_OPEN_CLOSE


def Astar(adj,start,stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj) #Lop cha
    g= [float('inf')] * len(adj)
    f= [float('inf')] * len(adj)

    #Buoc 0:
    #khoi tao cac gia tri
    OPEN.append(start) #dua star vao OPEN
    g[start] = 0
    f[start] = h[start][1]

    while len(OPEN) > 0:        #OPEN <> 0
        curr = OPEN.pop(0)      #lay ra tu dau cua OPEN
        print(f"curr : {curr}")
        CLOSE.append(curr)       # đưa đỉnh đang xét vào CLOSE
        print(f"CLOSE : {CLOSE}")

        if curr == stop:
            print(f'Tim thay duong di {start} -> {stop}')
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

        #neu chua la dinh ket thuc, thi xet cac dinh kề kế tiếp
        for neighbor in range(len(adj)):
            if adj[curr][neighbor] !=0:
                 if check_OPEN_CLOSE(OPEN,neighbor)==False and check_OPEN_CLOSE(CLOSE,neighbor)==False:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + adj[curr][neighbor]
                    f[neighbor] = g[neighbor] + h[neighbor][1]
                    Parent[neighbor] = curr
                 else: #neighbor thuoc ve OPEN hoac CLOSE
                    g_new = g[curr] + adj[curr][neighbor]
                    f_new = g_new + h[neighbor][1]
                    print(f"g_new : ({neighbor}): {g_new}, f_new({neighbor}): {f_new}")

                    if f_new < f[neighbor]:
                        g[neighbor] = g_new
                        f[neighbor] = f_new
                        print(f"cap nhat gia tri f({neighbor}),  g({f[neighbor]}):")
                        Parent[neighbor] = curr #cap nhat lai Parent va khong dua vao Tn
        print(f"Tn : {Tn}")
        #chen Tn vao dau Open
        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        #Sap xep TN tang dan theo h
        OPEN_sorted = sorted(OPEN,key = lambda x: f[x],reverse = False)
        OPEN = OPEN_sorted

        print(f"OPEN sorted: {OPEN}")
        print(f"g : {g}")
        print(f"f : {f}")
        print(f"Parent : {Parent}")

        #Reset Tn trước khi quay lại từ đỉnh từ OPEN
        Tn=[]

    #Open = 0
    print(f"Khong tim thay duong di {start} -> {stop}")

if __name__ == '__main__':
    n, adj = read_adj('input/astar.adj')
    h = read_h('input/astar.h')
    print(f"Number of nodes: {n}")
    print(f"Heuristic values: {h}")
    for i in range(n):
        print(f"{adj[i]}")

    Astar(adj, 0, 9)