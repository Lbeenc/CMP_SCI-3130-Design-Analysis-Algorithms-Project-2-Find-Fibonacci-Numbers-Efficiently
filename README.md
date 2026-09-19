# CMP_SCI-3130-Design-Analysis-Algorithms-Project-2-Find-Fibonacci-Numbers-Efficiently

Project 2. Find Fibonacci Numbers Efficiently
(Due 12/15/2024 Sunday)
Description:
In this project, we will compare different algorithms for the Fibonacci Numbers to get
an idea on the power of an efficient algorithm. The first algorithm is the straightforward
recursive algorithm (see PPT notes - Module 3 Part C page 1 - Fibo(int n)). This
algorithm contains too much redundant computation, and as a result, extremely ineffi-
cient. The second algorithm removes all the redundant computation and calculates the
Fibonacci numbers using the dynamic programming approach (see PPT notes - Module
3 Part C page 4 Method 2). (The third algorithm is optional for those students who
would like to earn extra credit. See the last item of the requirements for the description.)
Requirements:
1. (Determine an appropriate problem size for the first method)
Since the first algorithm is extremely slow, it takes too long to calculate a Fibonacci
number of relatively large size. In our first program, we will pass the problem size
(the number n for the Fibonacci number Fn) either as a command-line argument,
or written in the program. (If you like to get the number n from the user’s input
at the prompt, you can do it.) When you calculate the number, also record the
execution time (in seconds or milliseconds based on the situation) and display it in
the console.
When you do experiments, find the size number n0, such that your execution time
for Fn0 is between 20 and 30 seconds on your machine. After you find this number
n0, you can use it in your program directly, just display a message on the screen
to show the value of n0. (Use the long integer data type instead of the int data
type.)
2. (See the huge difference of an efficient algorithm)
Write our second program or method to implement the efficient algorithm. To see
how large the problem size this algorithm can handle, we need to go to a much
larger data type in this situation. In Java, we can use BigInteger class to do the
calculation. When you print the execution time, use the number of milliseconds.
See how much time you need to calculate F10000. When you do experiments using
this method, do twice: The first time, find Fn0 and compare the response time with
1
that of the first method to see the improvement; the second time, calculate a large
Fibonacci number, for example, F5000 or F10000, to see how powerful this method is.
3. (Show experiment results)
Make a screenshot/screenshots to include all the experiment results and put it in
the submission folder. This step will help the grading that allows me to see the
problems faster.
4. (Optional for 2% extra credit: An algorithm with logarithmic efficiency)
Now we want to get better efficiency for the Fibonacci numbers. A new property
is needed to achieve this goal. From our textbook, we have the following matrix
formula, "
F (n − 1) F (n)
F (n) F (n + 1)
#
=
"
0 1
1 1
#n
for n ≥ 1.
In order to apply this formula, you need to know how to calculate the matrix
multiplication. To calculate the powers of a matrix as fast as possible, we can
use the repeated squaring technique. We still use the Java BigInteger class to do
calculation for this part. If you use Python, it can handle big integers automatically
without any special treatment.
You still pass the problem size n as before. If n is not provided, use the default
value n = 1000. Then you compare Method 2 and Method 3 in two aspects: 1)
Make sure that both Method 2 and Method 3 return the same result for the same
input number n; 2) For sufficiently large input n, see if you can get better efficiency
for Methods 3.
For each of your program/method, print out appropriate messages on the screen for
the users to understand what you are doing.
