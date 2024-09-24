from bitarray import bitarray

class Life:
    """A python implementation of Game of Life
    
    part of BGP
    """
    def __init__(self, filename:str):
        """Create a game of life object
    
        Args:
            filename: Input file name.
    
        Raises:
            Exceptions: If input data is invalid.
        """
        self.filename = filename  
        self.grid = []
        with open(filename) as f:
            
            self.w,self.h = map(int, f.readline().split(' ', 1))
            
            for y in range(self.h + 2):
                self.grid.append(bitarray(self.w + 2)) # save memory, bitarray is also avaliable
                
            for no, line in enumerate(f):
                try:
                    y , x = map(int, line.split(' ', 1))
                    
                    if y < 0 or x < 0:
                        raise ValueError
    
                except ValueError:
                    raise Exception(f"Invaild cell on line {no+2}.")
     
                self.grid[y + 1][x + 1] = 1

    
    def tick_grid(self,n:int=1):
        """Applies the rules of Game of Life for specified number of generations.
    
        Args:
        n: Number of generations      
        """
        for i in range(n):
            for y,row in enumerate(self.grid[1:-1]):
                y1,y2 = y+1,y+2   
                curr = bitarray (self.w+2)
                for x,cell in enumerate(row[1:-1]):
                    count = self.grid[y][x] + self.grid[y][x+1] + self.grid[y][x+2] + self.grid[y1][x] + self.grid[y1][x+2]  + self.grid[y2][x] + self.grid[y2][x+1] + self.grid[y2][x+2]
                    curr[x+1] = 1 if count == 3 or (cell and count ==2) else 0
        
                if y > 0:
                    self.grid [y] = prev
                prev = curr
            self.grid [y+1] = curr
