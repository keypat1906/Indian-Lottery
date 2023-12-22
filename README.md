Solution for Hungarian lottery

Introduction:
I have created this program in python3 and it is using argument as a file which contains multiple lines of numbers. My program parses each line and calculate the total number of winners who won 2, 3, 4 and 5 numbers.


How to run:
You can run using python source file which I have attached in the src folder. You need python3 installed on your machine.

    pick_winner.py FILENAME


Input validation:
If you enter other than number, it throws error and return. 
It only accepts 5 numbers so there is validation to check if numbers are not more than 5, otherwise it returns the program. You can enter less than 5 numbers though. 


Test results:
This program is heavily CPU bound so result may vary based on the machine we run. I developed and tested this code on my 2015 Macbook Pro which has CPU configuration 2.8 GHz Quad-Core Intel Core i7 with 4 CPU Cores and it has 16 GB RAM.

This is sample screenshot of my tests. You can see it also lists how much time it takes to pull the results. Based on the sample file provided which has 10 million records, it takes average 5 to 6 seconds to calculate the results of 10 million records. 

 

Program will keep running until you press Cntrl C. You can enter as many as number you like to calculate the winners.

Time and Space complexity
Time complexity is easily O(N) where N is number of input lines we feed to the program. In addition I used dictionary to calculate and store the results which is O(1) best case and worst case is O(N). That means total time complexity is O(N) + O(1)  best case scenario.

For space, I am using dictionary to store 5 numbers it so it takes O(N) space complexity where N=5


Improvement 
This is most optimized code in the Python3 language. I developed this code in Python3 and python3 does not provide better performance if I use Threading due to GIL mechanism in python language. I have heard Golang is more efficient than Python so if you like I can create this in Golang as well. Let me know your thoughts on this. Any criticism or comment on the code welcome.
![image](https://github.com/keypat1906/Hungarian_lottery/assets/97865025/05a94f42-ba0e-43f9-b1b1-8e23d059b23c)
