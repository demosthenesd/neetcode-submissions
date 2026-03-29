class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let columns = Array.from({ length: 9 }, () => new Set());
        let rows = Array.from({ length: 9 }, () => new Set());
        let squares = new Map();

        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                let num = board[i][j];

                if (num === ".") continue;

                let squareKey = `${Math.floor(i / 3)}-${Math.floor(j / 3)}`;
                if (!squares.has(squareKey)) squares.set(squareKey, new Set());

                if (rows[i].has(num) || columns[j].has(num) || squares.get(squareKey).has(num)) {
                    return false; // Duplicate found
                }

                rows[i].add(num);
                columns[j].add(num);
                squares.get(squareKey).add(num);
            }
        }
        return true;
    }
}

