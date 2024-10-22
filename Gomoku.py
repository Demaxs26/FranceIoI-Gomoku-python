nb = int(input())
plateau = [list(map(lambda x :int(x) ,input().split())) for k in range(nb)]

global tabtested1,tabtested2
tabtested1 =[]
tabtested2 =[]

def testAjout(coo:tuple,ajout:tuple,tab:list,team:int)->bool:
    '''renvoie true si la case visée après l'ajout est de la meme team, 
    False si la case est vide, n'existe pas ou appartient a l'autre team '''
    try:
        if plateau[coo(0) + ajout(0)][coo(1) + ajout(1)] == team:
            return True
        else:
            return False
    except:
        return False

def ligne(coo:tuple,team:int,plateau:list)->bool:
    tabcoo = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
    for ajout in tabcoo:
        if testAjout(coo,ajout,plateau,team):
            
        

ok = False
y = 0
while not(ok) and y < nb:
    x = 0
    while not(ok) and x < nb: 

        x += 1
    y += 1

