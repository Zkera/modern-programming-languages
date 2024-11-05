class Tree:
    
    height = 0
    radius = 0
    def __init__(self, h, r):
        self.height = h
        self.radius = r
    def calculate_volume(self):
        return ((self.radius**2)*self.height*0.7854)
    