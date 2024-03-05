

class Expanding_Galaxy:
   
    path = "gx/bg"
    filenames = [f for f in os.listdir(path) if f.endswith('.png')]
    imagelist = []
    for name in filenames:
        imagename = os.path.splitext(name)[0] 
        imagelist.append(pg.image.load(os.path.join(path, name)).convert_alpha())
       
 

    def __init__(self, player):
        self.player = player
        self.cam = self.player.camera
        self.camx, self.camy = self.cam
        self.img = []
        self.bgdata = []
        self.player = player
        self.x = 1000
        self.y = 1000
        self.w = W
        self.H = H
        


    def coordinates(self, camx, camy, objw, objh):
      
        self.camxx = 2*self.camx
        self.camyy = 2*self.camy
       
        if self.camx = camxx // 2:
            self.camxx= 3 * self.camx



         if self.camy = camyy // 2:
            self.camyy = 3 * self.camy    
        self.camrect = pg.Rect(self.camxx, self.camyy, W, H)
        if not self.objrect.colliderect(self.camrect):
               
                return self.rx, self.ry
    
    
    def add_bg(self, camx, camy):
        self.bg = {}
     
    
        self.bg['img'] = random.randint(0, len(self.imagelist) - 1)
       
        self.bg['width'] = self.imagelist[0].get_width()
        self.bg['height'] = self.imagelist[0].get_height()

      
        self.bg['x'], self.bg['y'] = self.coordinates(camx, camy, self.bg['width'], self.bg['height'])
        self.bg['rect'] = pg.Rect( (self.bg['x'], self.bg['y'], self.bg['width'], self.bg['height']) )
        
        return self.bg
    def boundaries(self, camx, camy, bg):
        # Return False if camx and camy are more than
        # a half-window length beyond the edge of the window.
        self.bounds_left = self.camx - W
        self.bounds_top = self.camy - H
        self.boundsrect = pg.Rect(self.bounds_left, self.bounds_top, W2*2, H2*2)
        self.objrect = pg.Rect(self.bg['x'], self.bg['y'], self.bg['width'], self.bg['height'])
        return not self.boundsrect.colliderect(self.objrect)        



    def bgupdate(self, camx, camy):
       
         self.camx = camx
         self.camy  = camy
         if len(self.bgdata) < self.stars:
             self.bgdata.append(self.add_bg(self.camx, self.camy))
         for self.bg in self.bgdata:
            self.mrect = pg.Rect( (self.bg['x'] - self.camx, self.bg['y'] - self.camy, self.bg['width'], self.bg['height']) )
            
            screen.blit(self.imagelist[self.bg['img']], self.mrect)    
       
         for i in range(len(self.bgdata) - 1, -1, -1):
            if self.boundaries(self.camx, self.camy, self.bgdata[i]):
                del self.bgdata[i]
         return self.imagelist, self.mrect 
     
        

                



