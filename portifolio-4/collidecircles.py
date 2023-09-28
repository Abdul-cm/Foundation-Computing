def collidecircles(x1, y1, x2, y2):
    R = 4
    if (x1-x2)^2 + (y1-y2)^2 < (2 * R):
        return True
    else:
        return False

answer = collidecircles(1,2,3,4)
print(answer)
