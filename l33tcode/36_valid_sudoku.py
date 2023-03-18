class Solution:
    def isValidSubSudoku(self, subBoard: List[List[str]]) -> bool:
        return False

    def isValidLine(self, line: List[str]) -> bool:
        count = {}
        for i, val in enumerate(line):
            if val == ".":
                continue
            count[val] = 1 + count.get(val, 0)
            if count[val] > 1:
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(list)
        subSudoku = collections.defaultdict(list)

        for i in range(0, 9):
            if not self.isValidLine(board[i]):
                return False
            for j, val in enumerate(board[i]):
                columns[j].append(val)
                # TODO optimize via (i//3, j//3)
                if i < 3 and j < 3:
                    subSudoku[0].append(val)
                elif i < 3 and 3 <= j < 6:
                    subSudoku[1].append(val)
                elif i < 3 and 6 <= j:
                    subSudoku[2].append(val)
                elif 3 <= i < 6 and j < 3:
                    subSudoku[3].append(val)
                elif 3 <= i < 6 and 3 <= j < 6:
                    subSudoku[4].append(val)
                elif 3 <= i < 6 and 6 <= j:
                    subSudoku[5].append(val)
                elif 6 <= i and j < 3:
                    subSudoku[6].append(val)
                elif 6 <= i and 3 <= j < 6:
                    subSudoku[7].append(val)
                elif 6 <= i and 6 <= j:
                    subSudoku[8].append(val)

        for column in list(columns.values()):
            if not self.isValidLine(column):
                return False

        for column in list(subSudoku.values()):
            if not self.isValidLine(column):
                return False

        # print(subSudoku.values())

        return True
