# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:15:42 2019

@author: kasprark

title: example on objects inheritance
"""

#%%

class Agent():
    
    #def __init__(self, discount=.9, learning_rate=.1, exploration_rate=.1):
    def __init__(self, discount, learning_rate=.1, exploration_rate=.1):
        
        self.discount = discount                   # gamma
        self.learning_rate = learning_rate         # alpha 
        self.exploration_rate = exploration_rate   # epsilon 
        
        self._dic = {'a': 1, 'b': 3}
        
        self._lst = ['a', 'b']
        
    @property
    def lst(self):
        return self._lst

    @property
    def dic(self):
        return self._dic
    
    def reset(self):
        pass
    
    def action(self):
        pass
    
    def learn(self):
        pass
    
    def statistics(self):
        print()
    
#%%

class DiscreteAgent(Agent):
    
        
    def __init__(self, envir, *args):
        
        # discrete
        self.nA = envir.nA
        self.nS = envir.nS
        
        super(DiscreteAgent, self).__init__(*args)
        
        self._dic = {**super().dic,
                    'd': 6
                    }
        
        self._lst = super().lst + ['c']
        

        
#%%        
        
class Envir():
    def __init__(self, nA, nS):    
        self.nA = nA
        self.nS = nS
             
#%%
        
env = Envir(2, 3)
env
dir(env)        

da = DiscreteAgent(env, .9)        
da        
dir(da)        
da.dic
da.lst

da.discount        
da.learning_rate        
da.exploration_rate

da = DiscreteAgent(env, .9, .4)        
da        
dir(da)        
da.discount        
da.learning_rate        
da.exploration_rate

#%%