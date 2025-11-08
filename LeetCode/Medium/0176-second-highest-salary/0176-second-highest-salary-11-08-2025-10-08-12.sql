# Write your MySQL query statement below
SELECT MAX(salary) as SecondHighestSalary from Employee WHERE salary NOT IN (SELECT MAX(salary) from Employee)
