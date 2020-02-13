from direct.showbase.ShowBase import *
 
class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.10, 0.10, 0.10)
        self.scene.setPos(-8, 42, 0)
 
 
app = MyApp()
app.run()
