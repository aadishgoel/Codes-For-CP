'''input
1
3 3
1 2 1
1 3 2
1 2
1 3
2 3
'''

for t in range(int(input())):
    n,q= map(int, input().split())
    graph={i:[] for i in range(1,n+1)}
    vs = set()
    for _ in range(n-1):
        u,v,w= map(int, input().split())
        graph[u].append((v,w))
        vs.add(v)

    roots = [i for i in range(1,n+1) if i not in vs] 

    for _ in range(q):
        u,v= map(int, input().split())    
        visited = {}
        ud=vd=-1
        def dfs(node,w,x):
            global ud,vd
            if not ud == -1 and not vd == -1:
                return
            if node not in visited:
                visited[node]=1
                w^=x
                if node==u:
                    ud = w
                if node==v:
                    vd = w
                for newNode,nW in graph[node]:
                    dfs(newNode,w,nW)
        
        for root in roots:
            dfs(root,0,0)
        print(ud^vd)


