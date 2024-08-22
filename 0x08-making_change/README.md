# Making Change Project

## Project Overview

The **Making Change** project is a classic problem in the realm of dynamic programming and greedy algorithms. The objective is to determine the fewest number of coins needed to achieve a given amount using a list of available coin denominations. This project demonstrates the application of dynamic programming concepts to solve optimization problems efficiently.

## Concepts Applied

### Greedy Algorithms
- **Description**: Greedy algorithms make the locally optimal choice at each stage with the hope of finding a global optimum. They are often used for problems like coin change but may not always yield the optimal solution.
  
### Dynamic Programming
- **Description**: Dynamic programming is a method for solving problems by breaking them down into simpler subproblems and storing the results of subproblems to avoid redundant calculations. It's particularly useful in optimization problems like the coin change problem.

### Algorithmic Complexity
- **Time Complexity**: The implemented algorithm strives to minimize the time complexity to ensure it runs efficiently, even for large inputs.
- **Space Complexity**: Memory usage is also optimized, storing only necessary intermediate results.

## Files

- **`0-making_change.py`**: This file contains the main function `makeChange`, which implements the dynamic programming solution to the coin change problem.
  
- **`0-main.py`**: This file includes test cases that demonstrate the functionality of the `makeChange` function. It tests various scenarios, including cases where the total can and cannot be made up with the available coins.

## Usage

### How to Run the Files

1. **Ensure the files are executable**:
   ```bash
   chmod +x 0-making_change.py 0-main.py
