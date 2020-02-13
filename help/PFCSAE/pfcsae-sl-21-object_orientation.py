# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Mon Dec 18 16:08:46 2017

21. Object Orientation And All That
===================================
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/PFCSAE
ls


#%%
'''
Earlier, we did an exercise for a first-in-first-out queue.
At the time, we used a global variable to keep the state of the queue.
To compare different approaches, the following slides show:

1. the original FIFO-queue solution (using a global variable, generally not good)
2. a modified version where the queue variable is passed to every function
   (! this is object oriented programming without objects)
3. an object oriented version (where the queue data is part of the queue object).
   Probably the best solution, see OO programming for details.
4. a version based on closures (where the state is part of the closures)

'''

#%%
## Original FIFO solution (fifoqueue.py)

import fifoqueue as fq

fq.queue
fq.length()
fq.show()
fq.next()   ## takes and removes (pops) the first in the queue = last in the queue list
fq.show()

fq.add('Conan')  ## adds to the queue i.e. prepends to the queue list (its posiiton is 0)
fq.show()

fq.next()
fq.show()

#%%
## improved FIFO solution (fifoqueue2.py)

import fifoqueue2 as fq2

fq2.q1
fq2.q2

fq2.lenght()    ## Err, lack of argument
fq2.length(fq2.q1)
fq2.length(fq2.q2)

fq2.show(fq2.q1)
fq2.add(fq2.q1,"Conan")
fq2.q1
fq2.next(fq2.q1)
fq2.q1

#%%
## Object Oriented FIFO solution (fifoqueueoo.py)

import fifoqueueoo as fo

fo.q1   ## object of class "fifoqueue"
fo.q1.queue
fo.q1.length()

fo.q1.add('Conan')
fo.q1.show()
fo.q1.queue

fo.q1.next()
fo.q1.show()
fo.q1.queue

#%%
## Functional (closure) FIFO solution (fifoqueuecl.py)

import fifoqueuecl as cl

cl.q1_show()
## there's no acces to the queue itself !!! (at least no simple access...)

cl.q1_add('Conan')
cl.q1_show()

cl.q1_length()
cl.q1_next()
cl.q1_length()
cl.q1_show()

#%%
'''
Object orientation (OO):

* one important idea is to combine data and functions operating on data (in objects),
* objects contain data but
* access to data through interface (implementation details irrelevant to user)

Can program in OO style without OO-programming language:

* as in FIFO2 solution
* as in closure based approach
* OO mainstream programming paradigm (Java, C++, C#, ...)
* Python supports OO programming, and all things in Python are objects (see also slides 32 pp)
'''

