def knight_walk_distance(src, dest, board_size = 8):
    """
    The first challenge was to:
    Compute the number of chess' knight's jumps from src to dest.
    The squares of a chess board are enumerated sequentially from 
    left to right and top to bottom, starting from 0.
        src  = value for the position of the initial position
        dest = value for the position of the destination
    What it does is Breadth-first-search 
        (https://en.wikipedia.org/wiki/Breadth-first_search)
    The challenge only required 8x8 boards, if I remember correctly.
    """
    from collections import deque
    def inside(row, col):
        return (0 <= row and row <= board_size-1 and 0 <= col and col <= board_size-1)
    # To store if the position has been visited.
    board = [[False]*board_size for i in range(board_size)]
    # Deltas that move you like a knight
    delta_row = [-2, -1, 1, 2, -2, -1, 1, 2]
    delta_col = [-1, -2, -2, -1, 1, 2, 2, 1]
    # row and column of the initial position
    row, col = src//board_size, src%board_size
    board[row][col] = True
    # row and column of the destination
    dest_row, dest_col = dest//board_size, dest%board_size
    # End-points of the trajectories that still need to be explored
    q = deque([[row,col,0]])
    while (len(q) != 0):
        t = q.popleft()
        # Go o the destination
        if t[0] == dest_row and t[1] == dest_col:
            return t[2]
        # Try each knight's jump from where we are now
        for i in range(8):
            newpos_row = t[0] + drow[i]
            newpos_col = t[1] + dcol[i] 
            inSideIs = inside(newpos_row, newpos_col)
            if inSideIs:
                # the new position is inside the board.
                # Let's see if we have been here before.
                boardVisited = (board[newpos_row][newpos_col] == True)
            if inSideIs and not boardVisited:
                # The new position is inside the board and was not 
                # visited before. Add it to the queue of routs to try.
                board[newpos_row][newpos_col] = True
                q.append([newpos_row, newpos_col, t[2] + 1])
    return 0

def knight_walk_distance_catched(src,dest):
    """
    Returns the number of chess knight's jumps from src to dest.
    The squares of a chess board are enumerated sequentially from 
    left to right and top to bottom.
        src  = value for the position of the initial position
        dest = value for the position of the destination
    This one just has the solutions computed by the previous function.

        SOLUTIONS = [[0] * 64  for i in range(64)]
        for i in range(64):
            for j in range(64):
                SOLUTIONS[i][j] = knight_walk_distance(i,j)
        with open('SOLUTIONS.txt','w') as outfile:
            outfile.write(str(SOLUTIONS))
    """
    # For an 8 x 8 board we can just compute all solutions
    # using knight_walk_distance(src, dest, board_size = 8)
    # and just return the saved values each time. 
    SOLUTIONS = [[0, 3, 2, 3, 2, 3, 4, 5, 3, 4, 1, 2, 3, 4, 3, 4, 
                  2, 1, 4, 3, 2, 3, 4, 5, 3, 2, 3, 2, 3, 4, 3, 4, 
                  2, 3, 2, 3, 4, 3, 4, 5, 3, 4, 3, 4, 3, 4, 5, 4, 
                  4, 3, 4, 3, 4, 5, 4, 5, 5, 4, 5, 4, 5, 4, 5, 6], 
                 [3, 0, 3, 2, 3, 2, 3, 4, 2, 3, 2, 1, 2, 3, 4, 3, 
                  1, 2, 1, 4, 3, 2, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3, 
                  3, 2, 3, 2, 3, 4, 3, 4, 4, 3, 4, 3, 4, 3, 4, 5, 
                  3, 4, 3, 4, 3, 4, 5, 4, 4, 5, 4, 5, 4, 5, 4, 5], 
                 [2, 3, 0, 3, 2, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3, 4, 
                  4, 1, 2, 1, 4, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 4, 
                  2, 3, 2, 3, 2, 3, 4, 3, 3, 4, 3, 4, 3, 4, 3, 4, 
                  4, 3, 4, 3, 4, 3, 4, 5, 5, 4, 5, 4, 5, 4, 5, 4], 
                 [3, 2, 3, 0, 3, 2, 3, 2, 2, 1, 2, 3, 2, 1, 2, 3,
                  3, 4, 1, 2, 1, 4, 3, 2, 2, 3, 2, 3, 2, 3, 2, 3, 
                  3, 2, 3, 2, 3, 2, 3, 4, 4, 3, 4, 3, 4, 3, 4, 3, 
                  3, 4, 3, 4, 3, 4, 3, 4, 4, 5, 4, 5, 4, 5, 4, 5], 
                 [2, 3, 2, 3, 0, 3, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 
                   2, 3, 4, 1, 2, 1, 4, 3, 3, 2, 3, 2, 3, 2, 3, 2, 
                   4, 3, 2, 3, 2, 3, 2, 3, 3, 4, 3, 4, 3, 4, 3, 4, 
                   4, 3, 4, 3, 4, 3, 4, 3, 5, 4, 5, 4, 5, 4, 5, 4], 
                 [3, 2, 3, 2, 3, 0, 3, 2, 4, 3, 2, 1, 2, 3, 2, 1,
                  3, 2, 3, 4, 1, 2, 1, 4, 4, 3, 2, 3, 2, 3, 2, 3, 
                  3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 4, 3, 4, 3, 4, 3, 
                  5, 4, 3, 4, 3, 4, 3, 4, 4, 5, 4, 5, 4, 5, 4, 5], 
                 [4, 3, 2, 3, 2, 3, 0, 3, 3, 4, 3, 2, 1, 2, 3, 2, 
                  4, 3, 2, 3, 4, 1, 2, 1, 3, 4, 3, 2, 3, 2, 3, 2, 
                  4, 3, 4, 3, 2, 3, 2, 3, 5, 4, 3, 4, 3, 4, 3, 4, 
                  4, 5, 4, 3, 4, 3, 4, 3, 5, 4, 5, 4, 5, 4, 5, 4], 
                 [5, 4, 3, 2, 3, 2, 3, 0, 4, 3, 4, 3, 2, 1, 4, 3, 
                  5, 4, 3, 2, 3, 4, 1, 2, 4, 3, 4, 3, 2, 3, 2, 3, 
                  5, 4, 3, 4, 3, 2, 3, 2, 4, 5, 4, 3, 4, 3, 4, 3, 
                  5, 4, 5, 4, 3, 4, 3, 4, 6, 5, 4, 5, 4, 5, 4, 5], 
                 [3, 2, 1, 2, 3, 4, 3, 4, 0, 3, 2, 3, 2, 3, 4, 5, 
                  3, 2, 1, 2, 3, 4, 3, 4, 2, 1, 4, 3, 2, 3, 4, 5, 
                  3, 2, 3, 2, 3, 4, 3, 4, 2, 3, 2, 3, 4, 3, 4, 5, 
                  3, 4, 3, 4, 3, 4, 5, 4, 4, 3, 4, 3, 4, 5, 4, 5], 
                 [4, 3, 2, 1, 2, 3, 4, 3, 3, 0, 3, 2, 3, 2, 3, 4, 
                  2, 3, 2, 1, 2, 3, 4, 3, 1, 2, 1, 4, 3, 2, 3, 4, 
                  2, 3, 2, 3, 2, 3, 4, 3, 3, 2, 3, 2, 3, 4, 3, 4, 
                  4, 3, 4, 3, 4, 3, 4, 5, 3, 4, 3, 4, 3, 4, 5, 4], 
                 [1, 2, 3, 2, 1, 2, 3, 4, 2, 3, 0, 3, 2, 3, 2, 3, 
                  1, 2, 3, 2, 1, 2, 3, 4, 4, 1, 2, 1, 4, 3, 2, 3, 
                  3, 2, 3, 2, 3, 2, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3, 
                  3, 4, 3, 4, 3, 4, 3, 4, 4, 3, 4, 3, 4, 3, 4, 5], 
                 [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 3, 0, 3, 2, 3, 2, 
                  2, 1, 2, 3, 2, 1, 2, 3, 3, 4, 1, 2, 1, 4, 3, 2, 
                  2, 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 4, 
                  4, 3, 4, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3, 4, 3, 4], 
                 [3, 2, 1, 2, 3, 2, 1, 2, 2, 3, 2, 3, 0, 3, 2, 3, 
                  3, 2, 1, 2, 3, 2, 1, 2, 2, 3, 4, 1, 2, 1, 4, 3, 
                  3, 2, 3, 2, 3, 2, 3, 2, 4, 3, 2, 3, 2, 3, 2, 3, 
                  3, 4, 3, 4, 3, 4, 3, 4, 4, 3, 4, 3, 4, 3, 4, 3], 
                 [4, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 2, 3, 0, 3, 2, 
                  4, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 4, 1, 2, 1, 4, 
                  4, 3, 2, 3, 2, 3, 2, 3, 3, 4, 3, 2, 3, 2, 3, 2, 
                  4, 3, 4, 3, 4, 3, 4, 3, 5, 4, 3, 4, 3, 4, 3, 4], 
                 [3, 4, 3, 2, 1, 2, 3, 4, 4, 3, 2, 3, 2, 3, 0, 3, 
                  3, 4, 3, 2, 1, 2, 3, 2, 4, 3, 2, 3, 4, 1, 2, 1, 
                  3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 4, 3, 2, 3, 2, 3, 
                  5, 4, 3, 4, 3, 4, 3, 4, 4, 5, 4, 3, 4, 3, 4, 3], 
                 [4, 3, 4, 3, 2, 1, 2, 3, 5, 4, 3, 2, 3, 2, 3, 0, 
                  4, 3, 4, 3, 2, 1, 2, 3, 5, 4, 3, 2, 3, 4, 1, 2, 
                  4, 3, 4, 3, 2, 3, 2, 3, 5, 4, 3, 4, 3, 2, 3, 2, 
                  4, 5, 4, 3, 4, 3, 4, 3, 5, 4, 5, 4, 3, 4, 3, 4], 
                 [2, 1, 4, 3, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 3, 4, 
                  0, 3, 2, 3, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 3, 4, 
                  2, 1, 4, 3, 2, 3, 4, 5, 3, 2, 3, 2, 3, 4, 3, 4, 
                  2, 3, 2, 3, 4, 3, 4, 5, 3, 4, 3, 4, 3, 4, 5, 4], 
                 [1, 2, 1, 4, 3, 2, 3, 4, 2, 3, 2, 1, 2, 3, 4, 3, 
                  3, 0, 3, 2, 3, 2, 3, 4, 2, 3, 2, 1, 2, 3, 4, 3, 
                  1, 2, 1, 4, 3, 2, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3, 
                  3, 2, 3, 2, 3, 4, 3, 4, 4, 3, 4, 3, 4, 3, 4, 5], 
                 [4, 1, 2, 1, 4, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3, 4, 
                  2, 3, 0, 3, 2, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3, 4, 
                  4, 1, 2, 1, 4, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 4, 
                  2, 3, 2, 3, 2, 3, 4, 3, 3, 4, 3, 4, 3, 4, 3, 4], 
                 [3, 4, 1, 2, 1, 4, 3, 2, 2, 1, 2, 3, 2, 1, 2, 3, 
                  3, 2, 3, 0, 3, 2, 3, 2, 2, 1, 2, 3, 2, 1, 2, 3, 
                  3, 4, 1, 2, 1, 4, 3, 2, 2, 3, 2, 3, 2, 3, 2, 3, 
                  3, 2, 3, 2, 3, 2, 3, 4, 4, 3, 4, 3, 4, 3, 4, 3], 
                 [2, 3, 4, 1, 2, 1, 4, 3, 3, 2, 1, 2, 3, 2, 1, 2, 
                  2, 3, 2, 3, 0, 3, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 
                  2, 3, 4, 1, 2, 1, 4, 3, 3, 2, 3, 2, 3, 2, 3, 2, 
                  4, 3, 2, 3, 2, 3, 2, 3, 3, 4, 3, 4, 3, 4, 3, 4], 
                 [3, 2, 3, 4, 1, 2, 1, 4, 4, 3, 2, 1, 2, 3, 2, 1, 
                  3, 2, 3, 2, 3, 0, 3, 2, 4, 3, 2, 1, 2, 3, 2, 1, 
                  3, 2, 3, 4, 1, 2, 1, 4, 4, 3, 2, 3, 2, 3, 2, 3, 
                  3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 4, 3, 4, 3, 4, 3], 
                 [4, 3, 2, 3, 4, 1, 2, 1, 3, 4, 3, 2, 1, 2, 3, 2, 
                  4, 3, 2, 3, 2, 3, 0, 3, 3, 4, 3, 2, 1, 2, 3, 2, 
                  4, 3, 2, 3, 4, 1, 2, 1, 3, 4, 3, 2, 3, 2, 3, 2, 
                  4, 3, 4, 3, 2, 3, 2, 3, 5, 4, 3, 4, 3, 4, 3, 4], 
                 [5, 4, 3, 2, 3, 4, 1, 2, 4, 3, 4, 3, 2, 1, 2, 3, 
                  5, 4, 3, 2, 3, 2, 3, 0, 4, 3, 4, 3, 2, 1, 2, 3, 
                  5, 4, 3, 2, 3, 4, 1, 2, 4, 3, 4, 3, 2, 3, 2, 3, 
                  5, 4, 3, 4, 3, 2, 3, 2, 4, 5, 4, 3, 4, 3, 4, 3],
                 [3, 2, 3, 2, 3, 4, 3, 4, 2, 1, 4, 3, 2, 3, 4, 5, 
                  3, 2, 1, 2, 3, 4, 3, 4, 0, 3, 2, 3, 2, 3, 4, 5, 
                  3, 2, 1, 2, 3, 4, 3, 4, 2, 1, 4, 3, 2, 3, 4, 5, 
                  3, 2, 3, 2, 3, 4, 3, 4, 2, 3, 2, 3, 4, 3, 4, 5], 
                 [2, 3, 2, 3, 2, 3, 4, 3, 1, 2, 1, 4, 3, 2, 3, 4, 
                  2, 3, 2, 1, 2, 3, 4, 3, 3, 0, 3, 2, 3, 2, 3, 4, 
                  2, 3, 2, 1, 2, 3, 4, 3, 1, 2, 1, 4, 3, 2, 3, 4, 
                  2, 3, 2, 3, 2, 3, 4, 3, 3, 2, 3, 2, 3, 4, 3, 4], 
                 [3, 2, 3, 2, 3, 2, 3, 4, 4, 1, 2, 1, 4, 3, 2, 3, 
                  1, 2, 3, 2, 1, 2, 3, 4, 2, 3, 0, 3, 2, 3, 2, 3, 
                  1, 2, 3, 2, 1, 2, 3, 4, 4, 1, 2, 1, 4, 3, 2, 3, 
                  3, 2, 3, 2, 3, 2, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3], 
                 [2, 3, 2, 3, 2, 3, 2, 3, 3, 4, 1, 2, 1, 4, 3, 2, 
                  2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 3, 0, 3, 2, 3, 2, 
                  2, 1, 2, 3, 2, 1, 2, 3, 3, 4, 1, 2, 1, 4, 3, 2, 
                  2, 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 4], 
                 [3, 2, 3, 2, 3, 2, 3, 2, 2, 3, 4, 1, 2, 1, 4, 3, 
                  3, 2, 1, 2, 3, 2, 1, 2, 2, 3, 2, 3, 0, 3, 2, 3, 
                  3, 2, 1, 2, 3, 2, 1, 2, 2, 3, 4, 1, 2, 1, 4, 3, 
                  3, 2, 3, 2, 3, 2, 3, 2, 4, 3, 2, 3, 2, 3, 2, 3], 
                 [4, 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 4, 1, 2, 1, 4, 
                  4, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 2, 3, 0, 3, 2, 
                  4, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 4, 1, 2, 1, 4, 
                  4, 3, 2, 3, 2, 3, 2, 3, 3, 4, 3, 2, 3, 2, 3, 2], 
                 [3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 2, 3, 4, 1, 2, 1, 
                  3, 4, 3, 2, 1, 2, 3, 2, 4, 3, 2, 3, 2, 3, 0, 3, 
                  3, 4, 3, 2, 1, 2, 3, 2, 4, 3, 2, 3, 4, 1, 2, 1, 
                  3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 4, 3, 2, 3, 2, 3], 
                 [4, 3, 4, 3, 2, 3, 2, 3, 5, 4, 3, 2, 3, 4, 1, 2, 
                  4, 3, 4, 3, 2, 1, 2, 3, 5, 4, 3, 2, 3, 2, 3, 0, 
                  4, 3, 4, 3, 2, 1, 2, 3, 5, 4, 3, 2, 3, 4, 1, 2, 
                  4, 3, 4, 3, 2, 3, 2, 3, 5, 4, 3, 4, 3, 2, 3, 2], 
                 [2, 3, 2, 3, 4, 3, 4, 5, 3, 2, 3, 2, 3, 4, 3, 4, 
                  2, 1, 4, 3, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 3, 4, 
                  0, 3, 2, 3, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 3, 4, 
                  2, 1, 4, 3, 2, 3, 4, 5, 3, 2, 3, 2, 3, 4, 3, 4], 
                 [3, 2, 3, 2, 3, 4, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3, 
                  1, 2, 1, 4, 3, 2, 3, 4, 2, 3, 2, 1, 2, 3, 4, 3, 
                  3, 0, 3, 2, 3, 2, 3, 4, 2, 3, 2, 1, 2, 3, 4, 3, 
                  1, 2, 1, 4, 3, 2, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3], 
                 [2, 3, 2, 3, 2, 3, 4, 3, 3, 2, 3, 2, 3, 2, 3, 4, 
                  4, 1, 2, 1, 4, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3, 4, 
                  2, 3, 0, 3, 2, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3, 4, 
                  4, 1, 2, 1, 4, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 4], 
                 [3, 2, 3, 2, 3, 2, 3, 4, 2, 3, 2, 3, 2, 3, 2, 3, 
                  3, 4, 1, 2, 1, 4, 3, 2, 2, 1, 2, 3, 2, 1, 2, 3, 
                  3, 2, 3, 0, 3, 2, 3, 2, 2, 1, 2, 3, 2, 1, 2, 3, 
                  3, 4, 1, 2, 1, 4, 3, 2, 2, 3, 2, 3, 2, 3, 2, 3], 
                 [4, 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 
                  2, 3, 4, 1, 2, 1, 4, 3, 3, 2, 1, 2, 3, 2, 1, 2, 
                  2, 3, 2, 3, 0, 3, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 
                  2, 3, 4, 1, 2, 1, 4, 3, 3, 2, 3, 2, 3, 2, 3, 2], 
                 [3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 2, 3, 2, 3, 2, 3, 
                  3, 2, 3, 4, 1, 2, 1, 4, 4, 3, 2, 1, 2, 3, 2, 1, 
                  3, 2, 3, 2, 3, 0, 3, 2, 4, 3, 2, 1, 2, 3, 2, 1, 
                  3, 2, 3, 4, 1, 2, 1, 4, 4, 3, 2, 3, 2, 3, 2, 3], 
                 [4, 3, 4, 3, 2, 3, 2, 3, 3, 4, 3, 2, 3, 2, 3, 2, 
                  4, 3, 2, 3, 4, 1, 2, 1, 3, 4, 3, 2, 1, 2, 3, 2, 
                  4, 3, 2, 3, 2, 3, 0, 3, 3, 4, 3, 2, 1, 2, 3, 2, 
                  4, 3, 2, 3, 4, 1, 2, 1, 3, 4, 3, 2, 3, 2, 3, 2], 
                 [5, 4, 3, 4, 3, 2, 3, 2, 4, 3, 4, 3, 2, 3, 2, 3, 
                  5, 4, 3, 2, 3, 4, 1, 2, 4, 3, 4, 3, 2, 1, 2, 3, 
                  5, 4, 3, 2, 3, 2, 3, 0, 4, 3, 4, 3, 2, 1, 2, 3, 
                  5, 4, 3, 2, 3, 4, 1, 2, 4, 3, 4, 3, 2, 3, 2, 3], 
                 [3, 4, 3, 4, 3, 4, 5, 4, 2, 3, 2, 3, 4, 3, 4, 5, 
                  3, 2, 3, 2, 3, 4, 3, 4, 2, 1, 4, 3, 2, 3, 4, 5, 
                  3, 2, 1, 2, 3, 4, 3, 4, 0, 3, 2, 3, 2, 3, 4, 5, 
                  3, 2, 1, 2, 3, 4, 3, 4, 2, 1, 4, 3, 2, 3, 4, 5], 
                 [4, 3, 4, 3, 4, 3, 4, 5, 3, 2, 3, 2, 3, 4, 3, 4, 
                  2, 3, 2, 3, 2, 3, 4, 3, 1, 2, 1, 4, 3, 2, 3, 4, 
                  2, 3, 2, 1, 2, 3, 4, 3, 3, 0, 3, 2, 3, 2, 3, 4, 
                  2, 3, 2, 1, 2, 3, 4, 3, 1, 2, 1, 4, 3, 2, 3, 4], 
                 [3, 4, 3, 4, 3, 4, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3, 
                  3, 2, 3, 2, 3, 2, 3, 4, 4, 1, 2, 1, 4, 3, 2, 3, 
                  1, 2, 3, 2, 1, 2, 3, 4, 2, 3, 0, 3, 2, 3, 2, 3, 
                  1, 2, 3, 2, 1, 2, 3, 4, 4, 1, 2, 1, 4, 3, 2, 3], 
                 [4, 3, 4, 3, 4, 3, 4, 3, 3, 2, 3, 2, 3, 2, 3, 4, 
                  2, 3, 2, 3, 2, 3, 2, 3, 3, 4, 1, 2, 1, 4, 3, 2, 
                  2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 3, 0, 3, 2, 3, 2, 
                  2, 1, 2, 3, 2, 1, 2, 3, 3, 4, 1, 2, 1, 4, 3, 2], 
                 [3, 4, 3, 4, 3, 4, 3, 4, 4, 3, 2, 3, 2, 3, 2, 3, 
                  3, 2, 3, 2, 3, 2, 3, 2, 2, 3, 4, 1, 2, 1, 4, 3, 
                  3, 2, 1, 2, 3, 2, 1, 2, 2, 3, 2, 3, 0, 3, 2, 3, 
                  3, 2, 1, 2, 3, 2, 1, 2, 2, 3, 4, 1, 2, 1, 4, 3], 
                 [4, 3, 4, 3, 4, 3, 4, 3, 3, 4, 3, 2, 3, 2, 3, 2, 
                  4, 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 4, 1, 2, 1, 4, 
                  4, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 2, 3, 0, 3, 2, 
                  4, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 4, 1, 2, 1, 4], 
                 [5, 4, 3, 4, 3, 4, 3, 4, 4, 3, 4, 3, 2, 3, 2, 3, 
                  3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 2, 3, 4, 1, 2, 1, 
                  3, 4, 3, 2, 1, 2, 3, 2, 4, 3, 2, 3, 2, 3, 0, 3, 
                  3, 4, 3, 2, 1, 2, 3, 2, 4, 3, 2, 3, 4, 1, 2, 1], 
                 [4, 5, 4, 3, 4, 3, 4, 3, 5, 4, 3, 4, 3, 2, 3, 2, 
                  4, 3, 4, 3, 2, 3, 2, 3, 5, 4, 3, 2, 3, 4, 1, 2, 
                  4, 3, 4, 3, 2, 1, 2, 3, 5, 4, 3, 2, 3, 2, 3, 0, 
                  4, 3, 4, 3, 2, 1, 2, 3, 5, 4, 3, 2, 3, 4, 1, 2], 
                 [4, 3, 4, 3, 4, 5, 4, 5, 3, 4, 3, 4, 3, 4, 5, 4, 
                  2, 3, 2, 3, 4, 3, 4, 5, 3, 2, 3, 2, 3, 4, 3, 4, 
                  2, 1, 4, 3, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 3, 4, 
                  0, 3, 2, 3, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 3, 4], 
                 [3, 4, 3, 4, 3, 4, 5, 4, 4, 3, 4, 3, 4, 3, 4, 5, 
                  3, 2, 3, 2, 3, 4, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3, 
                  1, 2, 1, 4, 3, 2, 3, 4, 2, 3, 2, 1, 2, 3, 4, 3, 
                  3, 0, 3, 2, 3, 2, 3, 4, 4, 3, 2, 1, 2, 3, 4, 3], 
                 [4, 3, 4, 3, 4, 3, 4, 5, 3, 4, 3, 4, 3, 4, 3, 4, 
                  2, 3, 2, 3, 2, 3, 4, 3, 3, 2, 3, 2, 3, 2, 3, 4, 
                  4, 1, 2, 1, 4, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3, 4, 
                  2, 3, 0, 3, 2, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3, 4], 
                 [3, 4, 3, 4, 3, 4, 3, 4, 4, 3, 4, 3, 4, 3, 4, 3, 
                  3, 2, 3, 2, 3, 2, 3, 4, 2, 3, 2, 3, 2, 3, 2, 3, 
                  3, 4, 1, 2, 1, 4, 3, 2, 2, 1, 2, 3, 2, 1, 2, 3, 
                  3, 2, 3, 0, 3, 2, 3, 2, 2, 1, 2, 3, 2, 1, 2, 3], 
                 [4, 3, 4, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3, 4, 3, 4, 
                  4, 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 
                  2, 3, 4, 1, 2, 1, 4, 3, 3, 2, 1, 2, 3, 2, 1, 2, 
                  2, 3, 2, 3, 0, 3, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2], 
                 [5, 4, 3, 4, 3, 4, 3, 4, 4, 3, 4, 3, 4, 3, 4, 3, 
                  3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 2, 3, 2, 3, 2, 3, 
                  3, 2, 3, 4, 1, 2, 1, 4, 4, 3, 2, 1, 2, 3, 2, 1, 
                  3, 2, 3, 2, 3, 0, 3, 2, 4, 3, 2, 1, 2, 3, 2, 1], 
                 [4, 5, 4, 3, 4, 3, 4, 3, 5, 4, 3, 4, 3, 4, 3, 4, 
                  4, 3, 4, 3, 2, 3, 2, 3, 3, 4, 3, 2, 3, 2, 3, 2, 
                  4, 3, 2, 3, 4, 1, 2, 1, 3, 4, 3, 2, 1, 2, 3, 2, 
                  4, 3, 2, 3, 2, 3, 0, 3, 3, 4, 3, 2, 1, 2, 3, 4], 
                 [5, 4, 5, 4, 3, 4, 3, 4, 4, 5, 4, 3, 4, 3, 4, 3, 
                  5, 4, 3, 4, 3, 2, 3, 2, 4, 3, 4, 3, 2, 3, 2, 3, 
                  5, 4, 3, 2, 3, 4, 1, 2, 4, 3, 4, 3, 2, 1, 2, 3, 
                  5, 4, 3, 2, 3, 2, 3, 0, 4, 3, 4, 3, 2, 1, 2, 3], 
                 [5, 4, 5, 4, 5, 4, 5, 6, 4, 3, 4, 3, 4, 5, 4, 5, 
                  3, 4, 3, 4, 3, 4, 5, 4, 2, 3, 2, 3, 4, 3, 4, 5, 
                  3, 2, 3, 2, 3, 4, 3, 4, 2, 1, 4, 3, 2, 3, 4, 5, 
                  3, 4, 1, 2, 3, 4, 3, 4, 0, 3, 2, 3, 2, 3, 4, 5], 
                 [4, 5, 4, 5, 4, 5, 4, 5, 3, 4, 3, 4, 3, 4, 5, 4, 
                  4, 3, 4, 3, 4, 3, 4, 5, 3, 2, 3, 2, 3, 4, 3, 4, 
                  2, 3, 2, 3, 2, 3, 4, 3, 1, 2, 1, 4, 3, 2, 3, 4, 
                  2, 3, 2, 1, 2, 3, 4, 3, 3, 0, 3, 2, 3, 2, 3, 4], 
                 [5, 4, 5, 4, 5, 4, 5, 4, 4, 3, 4, 3, 4, 3, 4, 5, 
                  3, 4, 3, 4, 3, 4, 3, 4, 2, 3, 2, 3, 2, 3, 4, 3, 
                  3, 2, 3, 2, 3, 2, 3, 4, 4, 1, 2, 1, 4, 3, 2, 3, 
                  1, 2, 3, 2, 1, 2, 3, 4, 2, 3, 0, 3, 2, 3, 2, 3], 
                 [4, 5, 4, 5, 4, 5, 4, 5, 3, 4, 3, 4, 3, 4, 3, 4, 
                  4, 3, 4, 3, 4, 3, 4, 3, 3, 2, 3, 2, 3, 2, 3, 4, 
                  2, 3, 2, 3, 2, 3, 2, 3, 3, 4, 1, 2, 1, 4, 3, 2, 
                  2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 3, 0, 3, 2, 3, 2], 
                 [5, 4, 5, 4, 5, 4, 5, 4, 4, 3, 4, 3, 4, 3, 4, 3, 
                  3, 4, 3, 4, 3, 4, 3, 4, 4, 3, 2, 3, 2, 3, 2, 3, 
                  3, 2, 3, 2, 3, 2, 3, 2, 2, 3, 4, 1, 2, 1, 4, 3, 
                  3, 2, 1, 2, 3, 2, 1, 2, 2, 3, 2, 3, 0, 3, 2, 3], 
                 [4, 5, 4, 5, 4, 5, 4, 5, 5, 4, 3, 4, 3, 4, 3, 4, 
                  4, 3, 4, 3, 4, 3, 4, 3, 3, 4, 3, 2, 3, 2, 3, 2, 
                  4, 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 4, 1, 2, 1, 4, 
                  4, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 2, 3, 0, 3, 2], 
                 [5, 4, 5, 4, 5, 4, 5, 4, 4, 5, 4, 3, 4, 3, 4, 3, 
                  5, 4, 3, 4, 3, 4, 3, 4, 4, 3, 4, 3, 2, 3, 2, 3, 
                  3, 4, 3, 2, 3, 2, 3, 2, 4, 3, 2, 3, 4, 1, 2, 1, 
                  3, 4, 3, 2, 1, 2, 3, 2, 4, 3, 2, 3, 2, 3, 0, 3], 
                 [6, 5, 4, 5, 4, 5, 4, 5, 5, 4, 5, 4, 3, 4, 3, 4, 
                  4, 5, 4, 3, 4, 3, 4, 3, 5, 4, 3, 4, 3, 2, 3, 2, 
                  4, 3, 4, 3, 2, 3, 2, 3, 5, 4, 3, 2, 3, 4, 1, 2, 
                  4, 3, 4, 3, 2, 1, 4, 3, 5, 4, 3, 2, 3, 2, 3, 0]]
    return SOLUTIONS[src,dest]
