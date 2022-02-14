Movie Theater Seating Challenge
Language used: Python

Program Description: 
This program takes an input file from command line argument, reads line by line and processes the user requests for reserving seats in the movie theater. And then returns the file path for the output file.
The algorithm follows following rules:
1. Customers that come first will be allocated seats in the middle rows.
2. Each group will be allocated seats in a single row.
3. Fullfill as many requests as possible.\
4. If the numbers of requested seats are not available in the theater then, inform the customer about insufficient seats.

Assumptions:

1. The theater cannot reserve seats for a group if the requested number of seats is greater than the available seats. In that case, the customers are informed about the insufficient number of available seats.
2. The reservation number(R###) will be in sequential order like (R001, R002, R003...) in the input file.
3. Reservations will be read one by one, if a reservation is skipped due to insufficient seats, later reservations will still be checked
4. Group size < 20

How are the goals of the problem statement achieved?

Customer Satisfaction:

1. Preference to seating groups together
2. Since the middle seats give a better viewing experience in the movie theater, customers who come first will be allocated seats in the middle rows.

Customer Safety:
1. Distance of 3 seats and/or 1 row is maintained between 2 groups at any point.

Theater Utilization:

If safety is priority, seats will not be allocated once there are no seats to ensure the minimum distance between groups.

Steps for running the program

1. Download the movie.py file and inputfile.txt
2. Modify the inputfile if required.
2. Run movie.py in the terminal, with the input file location as the command line argument.
3. A 'seats.txt' file will be generated in the same directory as the required output file with seat reservation details.
