# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

    def judgeCircle(self, moves: str) -> bool:
        directions = { 'U':0, 'L':0, 'R': 0, 'D':0}

        for i in range(0, len(moves)):
            directions[moves[i]] += 1
        
        if directions['U'] == directions['D'] and directions['L'] == directions['R']:
            return True
        else:
            return False
        