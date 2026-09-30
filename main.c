#include <stdio.h>

int main() {
    // 1. Defining your subject mark variables
    int physics = 85;    // Change these numbers to your actual 12th marks!
    int chemistry = 80;
    int maths = 90;
    
    // 2. Calculating the total value
    int totalMarks = physics + chemistry + maths;
    
    // 3. Printing the results cleanly
    printf("--- My 12th Grade PCM Score ---\n");
    printf("Physics: %d\n", physics);
    printf("Chemistry: %d\n", chemistry);
    printf("Maths: %d\n", maths);
    printf("-------------------------------\n");
    printf("Total PCM Marks: %d / 300\n", totalMarks);
    
    return 0;
}

