-- 1. Create and select the database
CREATE DATABASE college;
USE college;

-- 2. Create the student table
CREATE TABLE student (
    rollno INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT NOT NULL,
    grade VARCHAR(1),
    city VARCHAR(20)
);

-- 3. Insert the sample data
INSERT INTO student
(rollno, name, marks, grade, city)
VALUES
(101, 'anil', 78, 'C', 'Pune'),
(102, 'bhumika', 93, 'A', 'Mumbai'),
(103, 'chetan', 85, 'B', 'Mumbai'),
(104, 'dhruv', 96, 'A', 'Delhi'),
(105, 'emanuel', 12, 'F', 'Delhi'),
(106, 'farah', 82, 'B', 'Delhi');

-- This is for fk & cascading foreign key example the dept & teacher tables 
CREATE TABLE dept (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
insert into dept 
values 
(101 , "english"),
(102 , "IT");
update dept
set id = 103
where id = 102;

select * from dept;
update dept
set id = 103
where id = 102;

CREATE TABLE teacher (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    foreign key (dept_id) references dept(id)
    on update cascade
    on delete cascade
    
);

insert into teacher 
values 
(101 , "ADAM" ,101 ),
(102 , "BOB" , 102);
select * from teacher;

-- HERE on update cascade , the id updated in parent table(student) auto. changes the dept id in child table(teacher)


-- To select unique cities from the table , SELECT Query in detail

SELECT DISTINCT city FROM student;
SELECT name , marks from student;

-- Select with WHERE Clause
select * from student where marks > 80;
select * from student where city = "Mumbai" and marks > 80;

-- Operators 
select * from student where marks % 2 = 0;
select * from student where marks + 10 > 100;
select * from student where marks - 10 < 80;

-- between operator (inclusive range):-
select * from student where marks between 80 and 90;

-- IN operator with list (not case sensitive):-
select * from student where city in ("Delhi"  , 'mumbai');

-- NOT - Negates the given condition
select * from student where city not in ("Delhi"  , 'mumbai');

-- LIMIT Clause :- sets an upper limit on number of rows to be returned
select * from student limit 3;

-- Order by clause (default it is ASC):
select * from student order by city ;
select * from student order by marks desc
limit 3;

-- Aggregate Functions
SELECT AVG(marks) from student;
SELECT max(marks) from student;
SELECT min(marks) from student;


-- GROUP BY CLAUSE:- USED AFTER "WHERE" & BEFORE "HAVING" to check what is the average marks of students ine ach city
select city , avg(marks)
from student 
GROUP BY city;

-- Columns selected at SELECT Clause must be included in Group by clause as well.
-- to find the no of students in each city
select city ,count(rollno)
from student 
GROUP BY city;

-- Q Write a query to find the average marks in each city in desc order
select city , avg(marks)
from student 
group by city 
order by city desc;

-- Q to check how many students scored what grade A B C...etc
select grade , count(name)
from student
group by grade
order by grade;

-- HAVING CLAUSE
select city , count(rollno)
from student
group by city
having max(marks) > 90;

 -- General order 
 select city
from student
where grade = 'A'
group by city
having max(marks) >=93
order by city;

-- UPDATE QUERY
-- In MySQL, sql_safe_updates = 0 disables safe update mode, allowing you to execute UPDATE or DELETE queries without a WHERE clause or a LIMIT constraint.
set sql_safe_updates = 0;
update student
set grade = "O"
where grade = "A";

update student
set grade = "B"
where marks between 80 and 90;

update student
set marks = marks + 1 ;

select * from student;

-- DELETE cmd
delete from student
where marks < 50;

-- ALTER CMDs to change the schema in database design)
-- 1] ADD a column (adds a column to the database)
alter table student
add column age INT;

 -- 2] DROP a column (drops a columns from the database)
 alter table student drop column age;
 
 -- 3] rename a table (dont run this) cuz i changed it from student to STUDENT1 & viceversa (current name is student)
 -- alo using caps doesnt make any diff for table name it keeps it lowercase even if u use caps
 alter table STUDENT1 
 rename to student ;
 
 alter table student
 add column yrs_old int not null default 18;

-- 4] modify cmd
alter table student
modify column yrs_old varchar(2) ; -- modifies the int dtype to varchar 

-- 5] change cmd
alter table student
change age student_age int; -- change previous col name to new col name w dtype

-- 6] Truncate cmd - to delete entire data of the table doesnt delete the table 
truncate student; -- ( again if u run this agian u will ve to insert the data & run queries again)

-- Q1] change the name of the column name to 'full_name"
alter table student
change name full_name varchar(50);

-- Q2] Delete all the students who scored marks < 80
delete from student 
where marks < 80;

-- Q3] Delete the column for grades
alter table student 
drop column grade;

 select * from student;  -- Execute this for each above queries to see the diff
 
 -- JOINS
 -- ===================================================
-- SETUP: Create Sample Database and Tables
-- ===================================================
CREATE DATABASE IF NOT EXISTS joins_demo;
USE joins_demo;

-- Clean up any prior tables
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- Parent Table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- Child Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT
);

-- Insert Department Data
-- Notice: Dept 40 (HR) has NO employees
INSERT INTO departments (dept_id, dept_name) VALUES
(10, 'Engineering'),
(20, 'Marketing'),
(30, 'Sales'),
(40, 'HR');

-- Insert Employee Data
-- Notice: Charlie (dept_id 50) belongs to a non-existent department
-- Notice: David (dept_id NULL) has no assigned department
INSERT INTO employees (emp_id, emp_name, dept_id) VALUES
(1, 'Alice', 10),
(2, 'Bob', 20),
(3, 'Charlie', 50),
(4, 'David', NULL);


-- ===================================================
-- 1. INNER JOIN
-- ===================================================
/*
DEFINITION:
Returns only the rows that have matching values in BOTH tables.
Any record from either table without a match is discarded.
*/

SELECT 
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employees e
INNER JOIN departments d 
    ON e.dept_id = d.dept_id;

-- Result: Shows Alice (10) and Bob (20). 
-- Charlie, David, and HR are omitted.


-- ===================================================
-- 2. LEFT JOIN (or LEFT OUTER JOIN)
-- ===================================================
/*
DEFINITION:
Returns ALL rows from the left table (employees), along with matched 
rows from the right table (departments). If there is no match on the right, 
NULL values are filled in for the right table's columns.
*/

SELECT 
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employees e
LEFT JOIN departments d 
    ON e.dept_id = d.dept_id;

-- Result: Shows all 4 employees.
-- Charlie and David show NULL for dept_name.


-- ===================================================
-- 3. RIGHT JOIN (or RIGHT OUTER JOIN)
-- ===================================================
/*
DEFINITION:
Returns ALL rows from the right table (departments), along with matched 
rows from the left table (employees). If there is no match on the left, 
NULL values are filled in for the left table's columns.
*/

SELECT 
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employees e
RIGHT JOIN departments d 
    ON e.dept_id = d.dept_id;

-- Result: Shows all 4 departments.
-- Sales and HR have NULL for emp_id and emp_name because no employees are assigned to them.


-- ===================================================
-- 4. FULL OUTER JOIN (Emulated via UNION)
-- ===================================================
/*
DEFINITION:
Returns all records when there is a match in either the left or right table.
Unmatched rows from either side are padded with NULLs.

NOTE FOR MYSQL:
MySQL does NOT support the native syntax "FULL OUTER JOIN".
Instead, you produce a FULL JOIN by taking a LEFT JOIN and combining 
it with a RIGHT JOIN using the UNION operator (which removes duplicates).
*/

SELECT 
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employees e
LEFT JOIN departments d 
    ON e.dept_id = d.dept_id

UNION

SELECT 
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employees e
RIGHT JOIN departments d 
    ON e.dept_id = d.dept_id;

-- Result: Shows everything from both tables, with NULLs wherever a match is missing.


-- ===================================================
-- 5. CROSS JOIN (Cartesian Product)
-- ===================================================
/*
DEFINITION:
Returns the Cartesian product of the two tables. Every single row from 
the first table is multiplied by every single row from the second table. 
No ON condition is used.
Total rows produced = (Left table count) * (Right table count).
Here: 4 employees * 4 departments = 16 rows.
*/

SELECT 
    e.emp_name,
    d.dept_name
FROM employees e
CROSS JOIN departments d;


-- ===================================================
-- 6. SELF JOIN
-- ===================================================
/*
DEFINITION:
A regular join in which a table is joined with itself.
Commonly used for hierarchical data (e.g., finding an employee's manager 
when both are stored in the same table).
*/

-- Temporary setup to show Self Join:
DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
    staff_id INT PRIMARY KEY,
    staff_name VARCHAR(50),
    manager_id INT
);

INSERT INTO staff (staff_id, staff_name, manager_id) VALUES
(1, 'Boss Khan', NULL),
(2, 'Sara', 1),
(3, 'Kabir', 1),
(4, 'Ravi', 2);

-- Query: Finding each staff member's manager name
SELECT 
    emp.staff_name AS Employee,
    mgr.staff_name AS Manager
FROM staff emp
LEFT JOIN staff mgr 
    ON emp.manager_id = mgr.staff_id;

-- Result:
-- Boss Khan -> NULL (Top of hierarchy)
-- Sara      -> Boss Khan
-- Kabir     -> Boss Khan
-- Ravi      -> Sara
 
 
