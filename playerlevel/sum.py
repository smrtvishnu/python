// JAVA Code for Find difference between sums
// of two diagonals
class GFG {
     
    public static int difference(int arr[][], int n)
    {
        // Initialize sums of diagonals
        int d1 = 0, d2 = 0;
      
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                // finding sum of primary diagonal
                if (i == j)
                    d1 += arr[i][j];
      
                // finding sum of secondary diagonal
                if (i == n - j - 1)
                    d2 += arr[i][j];
            }
        }
      
        // Absolute difference of the sums
        // across the diagonals
        return Math.abs(d1 - d2);
