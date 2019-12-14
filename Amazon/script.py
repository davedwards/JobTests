
count = 0
def removeObstacle(numRows, numColoumns, lot):

    def search(x, y):
        if lot[x][y] == 9:
            print('found at %d,%d' % (x, y))
            return True
        elif lot[x][y] == 0:
            print('wall at %d,%d' % (x, y))
            return False
        elif lot[x][y] == 3:
            print('visited at %d,%d' % (x, y))
            return False
        
        print('visiting %d,%d' % (x, y))

        # mark as visited
        lot[x][y] = 3
        
        # explore neighbors clockwise starting by the one on the right
        if ((x < len(lot)-1 and search(x+1, y))
            or (y > 0 and search(x, y-1))
            or (x > 0 and search(x-1, y))
            or (y < len(lot)-1 and search(x, y+1))):
            global count
            count += 1
            return True

        return False

    search(0,0)

if __name__ == '__main__':
    # lot = [ [1,0,0], [1,0,0], [1,9,1] ]
    lot = [[1,1,1,1],[0,1,1,1],[0,1,0,1],[1,1,9,1],[0,0,1,1]]
    
    removeObstacle(len(lot), len(lot[0]), lot)
    print(count)
