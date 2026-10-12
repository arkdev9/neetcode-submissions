class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.compmatrix = []
        prev_row = None
        for i, row in enumerate(matrix):
            prefix_row = []
            cumsum = 0
            for j, item in enumerate(row):
                prev_row_item = self.compmatrix[i - 1][j] if i > 0 else 0
                prefix_row.append(cumsum + item + prev_row_item)
                cumsum += item
            
            self.compmatrix.append(prefix_row)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # (r2c2 - r0c2 - r2c0 + r0c0)
        upper_rect = self.compmatrix[row1 - 1][col2] if row1 - 1 >= 0 else 0
        left_rect = self.compmatrix[row2][col1-1] if col1 - 1 >= 0 else 0
        
        chopped_rect = self.compmatrix[row1-1][col1-1] if col1 - 1 >= 0 and row1 - 1 >= 0 else 0
        
        bigger_rect = self.compmatrix[row2][col2]
        return bigger_rect - upper_rect - left_rect + chopped_rect


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)