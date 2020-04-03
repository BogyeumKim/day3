import math


def abc(point1,point2):
    result = math.sqrt ( math.pow(point1[1]-point1[1],2) +
                         math.pow(point2[2]-point2[2],2) )

    return result



movie=[('A',27,12),('A',50,10),('A',32,4),('M',8,34),('M',14,50),('M',2,40)]


scankiss = int(input('키스 몇번했나요'))
scanaction = int(input('액션 몇번있나요'))



compairson = (scankiss, scanaction)

movie.sort(key= lambda x: abc(x,compairson))


print(movie)


movie[]