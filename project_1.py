"""Write a program that takes input from the user for the marks obtained 
(out of 100) in at least five subjects by a student. The program should 
calculate and display the following. (grand total, average marks, total percentage)"""

sub1 = int(input("Enter marks of first subject :"))
sub2 = int(input("Enter marks of second subject :"))
sub3 = int(input("Enter marks of third subject :"))
sub4 = int(input("Enter marks of fourth subject :"))
sub5 = int(input("Enter marks of fifth subject :"))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
print("Grand total :", total_marks)
print("Average marks :", total_marks/5)
print("Total percentage :", (total_marks/500)*100)
