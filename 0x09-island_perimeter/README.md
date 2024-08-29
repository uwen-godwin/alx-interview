# Island Perimeter

## Description
This project involves calculating the perimeter of an island in a grid. The grid is represented as a 2D list, where `0` represents water and `1` represents land.

## Solution
The `island_perimeter` function iterates through each cell in the grid and calculates the perimeter by assuming each land cell contributes 4 to the perimeter. It then checks for adjacent land cells and reduces the perimeter accordingly.

## Running the Project
1. Ensure the files are executable:
   ```bash
   chmod +x 0-island_perimeter.py 0-main.py

## Run the main test file to see the output:
      
        ./0-main.py

