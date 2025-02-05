from include import Model
import moderngl as mgl

class Scene:
    def __init__(self,app):
        self.app=app
        self.objects=[]
        self.obj_names=['shaft','body','jaw_right','jaw_left']
        self.load()

    def add_object(self,obj):
        self.objects.append(obj)

    def load(self):
        app=self.app
        add=self.add_object

        #add(Model.BackgroundModel(app))
        add(Model.Shaft(app,pos=(0,0,-20)))
        add(Model.Body(app,pos=(0,0,-20)))
        add(Model.LeftJaw(app,pos=(0,0,-20)))
        add(Model.RightJaw(app,pos=(0,0,-20)))

        #add(Model.Cube(app))
        #add(Model.Cube(app,tex_id=0,pos=(-2.5,0,0),rot=(45,0,0),scale=(1,2,1)))
        #add(Model.Cube(app,tex_id=0,pos=(2.5,0,0),rot=(0,0,45),scale=(1,1,2)))
    def render(self,ctx):
        #i=0
        for obj in self.objects:
            #if self.obj_names[i]=='background':
             #   ctx.disable(mgl.DEPTH_TEST)
              #  obj.render(ctx)
               # ctx.enable(mgl.DEPTH_TEST)
            #else:
            obj.render(ctx)
            #i+=1
    def move_obj(self,obj_name,new_mat):
        for obj in self.objects:
            if obj.tex_id==obj_name:
                obj.move(new_mat)