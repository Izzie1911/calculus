#y= 4.9* x**2
#the avg = deltaY/deltaX
# value of function y in interval [x1,x2]
def function(x1,x2):
    deltaY = 4.9 * x2 ** 2 - 4.9 * x1 ** 2
    deltaX = x2 - x1
    return deltaY / deltaX

if __name__ == '__main__':
    #Avg velocity in 2 first secont
    v = function (0,2)
    #Avg velocity in [1,2]
    v2 = function(1,2)
