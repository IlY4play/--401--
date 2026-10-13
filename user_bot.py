from collections import deque

def script(check, x, y):
    # 1 Уровень
    if check("level") == 1:
        if check("gold", x, y): return "take" 
        if check("wall", x-23, y) and check("wall", x, y-2): return "right"
        if check("wall", x, y - 6): return "down"
     # 2 Уровень
    if check("level") == 2:
        if check("gold", x, y): return "take"
        if check("wall", x - 1, y) and not check("gold", x, y + 1) : return "right"
        if check("gold", x + 2, y) or check("gold", x + 1, y): return "right"
        if check("gold", x, y + 1): return "down"
        if check("gold", x, y - 1): return "up"
        if not check("wall", x, y - 1) and check("wall", x - 2, y): return "up"
    # 3 Уровень
    if check("level") == 3:
        if check("gold", x, y): return "take"

        if check("gold", 8, 23): return "right"
        if check("gold", 1, 16):
            if y > 16:
                if x < 4: return "right"
                return "up"
            return "left"

        if (check("gold", 13, 12) or check("gold", 14, 12) or
            check("gold", 13, 13) or check("gold", 14, 13)):
            if y > 14:
                if x < 7: return "right"
                return "up"
            if y == 14:
                if x < 13: return "right"
                return "up"
            if check("gold", x, y - 1): return "up"
            if check("gold", x + 1, y): return "right"
            if check("gold", x, y + 1): return "down"
            if check("gold", x - 1, y): return "left"

        if (check("gold", 1, 1) or check("gold", 1, 1) or
            check("gold", 8, 1)):
            if 12 <= y <= 13 and 13 <= x <= 14: return "down"
            if y > 10:
                if x < 18: return "right"
                return "up"
            if y > 8:
                if x > 4: return "left"
                return "up"
            if y == 8 and (check("gold", 1, 8) or check("gold", 1, 1)):
                if x > 1: return "left"
                return "up"
            if y > 1: return "up"
            if check("gold", 1, 1) and x > 1: return "left"
            if check("gold", 8, 1) and x < 8: return "right"

        if (check("gold", 19, 1) or check("gold", 26, 1) or
            check("gold", 26, 8)):
            if x < 19:
                if y < 7: return "down"
                return "right"
            if check("gold", 19, 1): return "up"
            if check("gold", 26, 1):
                if y > 1: return "up"
                return "right"
            if x < 26: return "right"
            return "down"

        if (check("gold", 26, 16) or check("gold", 26, 23) or
            check("gold", 19, 23)):
            if y < 16:
                if x > 20: return "left"
                return "down"
            if check("gold", 26, 16):
                if x < 26: return "right"
                return "up"
            if check("gold", 26, 23):
                if x < 26: return "right"
                return "down"
            if y < 23: return "down"
            if x > 19: return "left"
    # 4 и 5 Уровень
    if check("level") in (4, 5):
        if check("gold", x, y): return "take"
        
        width, height = (28, 25) if check("level") == 4 else (17, 17)
        moves = (("right", 1, 0), ("down", 0, 1),
                 ("left", -1, 0), ("up", 0, -1))
        queue = deque([(x, y, None)])
        visited = {(x, y)}
        while queue:
            cx, cy, first_move = queue.popleft()
            if check("gold", cx, cy): return first_move

            for move, dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < width and 0 <= ny < height): continue
                if (nx, ny) in visited or check("wall", nx, ny): continue
                if check("player", nx, ny): continue
                visited.add((nx, ny))
                queue.append((nx, ny, first_move or move))

    return "pass"
