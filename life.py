def read_grid(filename):
    grid = []
    with open(filename) as f:
        
        w,h = map(int, f.readline().split(' ', 1))
        
        for y in range(h):
            grid.append([0] * w)
            # grid.append(bytearray(10)) # save memory, bitarray is also avaliable
            
        for no, line in enumerate(f):
            try:
                y , x = map(int, line.split(' ', 1))
                
                if y < 0 or x < 0:
                    raise ValueError

            except ValueError:
                raise Exception(f"Invaild cell on line {no+2}.")


            grid[y][x] = 1
    return grid

@profile
def tick_grid(grid):
    h,w = len(grid), len(grid[0])

    nextgrid = []
    for y in range(h):
        nextgrid.append([0] *w)
        # nextgrid.append(bytearray(10))
        
    for y,row in enumerate(grid):
        for x,cell in enumerate(row):
            count = 0
            if y > 0:
                count += grid[y-1][x-1] if x > 0 else 0
                count += grid[y-1][x]
                count += grid[y-1][x+1] if x<w-1 else 0

            count += grid[y][x-1] if x > 0 else 0
            count += grid[y][x+1] if x < w-1 else 0

            if y < h-1:
                count += grid[y+1][x-1] if x > 0 else 0
                count += grid[y+1][x]
                count += grid[y+1][x+1] if x < w-1 else 0

            # if cell:           
            #     nextgen = 1 if count == 2 or count == 3 else 0
            # else:    
            #     nextgen = 1 if count == 3 else 0

            nextgrid[y][x] = 1 if count == 3 or (cell and count == 2) else 0

            # print(y, x, cell, count, nextgen)
    return nextgrid


filename = 'life.txt'
grid = read_grid(filename)
print(grid)

next_grid = tick_grid(grid)
print(grid)