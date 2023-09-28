def collidesquares (x1, y1, x2, y2):
    R = 4
    if abs(x1-x2) < R and abs(y1-y2) < R:
        return True
    else:
        return False
    
answer = collidesquares(1, 2, 3, 4)
print(answer)
