/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
  const queue = [];
  const freshOranges = 0;
  const minutes = -1;
	const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 2) queue.push([r, c]);
      else if (grid[i][j] === 1) freshOranges++;
    }
  }

	queue.push[(-1, -1)];
	
	while (queue.length > 0) {
		const row = 
	}
};
