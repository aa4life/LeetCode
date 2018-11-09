class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        (row, col) = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        elif board[row][col] == 'E':
            minenum = 0
            for i in (row-1, row, row+1):
                for j in (col-1, col, col+1):
                    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                        continue
                    if board[i][j] == 'M':
                        minenum += 1
            if minenum > 0:
                board[row][col] = str(minenum)
            else:
                board[row][col] = 'B'
                for i in (row-1, row, row+1):
                    for j in (col-1, col, col+1):
                        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                            continue
                        self.updateBoard(board, [i,j])
        return board