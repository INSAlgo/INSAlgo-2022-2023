#This is the demonstration of my KD tree "library"

#When plotting each search, you might see that sometimes the search using the KD tree doesn't find the same result as the regular search.
#I don't know why. I hope it's a case of distance equality.

from KDTree import *

import time as t
import random as rd


test = 0    #Type of test : test multiple times on one scatter with plotting if =0, plots time complexity if =1
N = 20      #Number of tests on the scatter (the biggest, the best kdt is, but it's also the number of plots if test == 0 so don't go nuts)

cmin, cmax = -2000, 2000                    #Limits of the coordinates
NbP = 1000                                  #Number of points in the scatter for test == 0
NbPmin, NbPmax, NbPstep = 200, 10000, 100   #Parameters for test == 1


#Tests in 2D (I don't want to deal with 3D plots) :

if test == 0 :
    timeBuild = 0
    timeNaive = 0
    timeKDT = 0

    #The test are all done on the same scatter plot, but the point it computes is different each loop.

    #Building the scatter with random points :
    s = Scatter("Test scatter")
    plt.figure(s.name)
    for i in range(NbP) :
        s.addPoint(Point((rd.randrange(cmin, cmax), rd.randrange(cmin, cmax))))
    #Building the KDTree :
    t0 = t.time()
    s.buildKDT()
    timeBuild = t.time()-t0

    #Using the KDTree method on a bunch of points :
    for k in range(N) :

        coords = (rd.randrange(cmin, cmax), rd.randrange(cmin, cmax))

        t0 = t.time()
        closeNaive = s.closest(coords)
        timeNaive += t.time()-t0
        
        t0 = t.time()
        closeKDT, minDist = s.closest_kdt(coords)
        timeKDT += t.time()-t0

        if N <= 20 :
            s.draw()
            plt.scatter(coords[0], coords[1], c='r', marker='+', label="Test point")

            closeKDT = closeKDT.info
            closeNaive.draw('g', 'o', label="Naive solution")
            closeKDT.draw('y', '.', label="Solution with KDTree")

            plt.legend()
            plt.title("Click for next plot")
            plt.show(block=False)
            plt.waitforbuttonpress()
            plt.clf()

    #Showing computation time :
    print(f"For a scatter of {NbP} points, for {N} searches :")
    print("Time taken to build trees :", timeBuild)
    print("Time taken to search the normal way :", timeNaive)
    print("Time taken to search with the tree :", timeKDT)



if test == 1 :
    TBuild = []
    TNaive = []
    TKDT = []
    Naxis = []
    import sys

    for Nbp in range(NbPmin, NbPmax, NbPstep) :
        Naxis.append(Nbp)
        print(f'Computing for {Nbp} points')
        sys.setrecursionlimit(Nbp)
        cmin, cmax = round(-10*Nbp**0.5, 0), round(10*Nbp**0.5, 0)
        timeNaive = 0
        timeKDT = 0

        s = Scatter("Test scatter", 2)
        for i in range(Nbp) :
            s.addPoint(Point((rd.randrange(cmin, cmax), rd.randrange(cmin, cmax))))
        t0 = t.time()
        s.buildKDT()
        timeBuild = t.time()-t0

        for _ in range(N) :

            point = (rd.randrange(cmin, cmax), rd.randrange(cmin, cmax))

            t0 = t.time()
            closeNaive = s.closest(point)
            timeNaive += t.time()-t0
            
            t0 = t.time()
            closeKDT, minDist = s.closest_kdt(point)
            timeKDT += t.time()-t0
        
        TBuild.append(timeBuild)
        TNaive.append(timeNaive)
        TKDT.append(timeKDT)

    plt.figure('time complexity')
    plt.plot(Naxis, TBuild, label='building time')
    plt.plot(Naxis, TNaive, label='time for naive search')
    plt.plot(Naxis, TKDT, label='time with KDTree')
    plt.legend()
    plt.show()