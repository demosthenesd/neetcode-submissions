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

// Example test
const board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
];

const solution = new Solution();
console.log(solution.isValidSudoku(board)); // Output: true
