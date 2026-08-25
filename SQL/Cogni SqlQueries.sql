create database Employee;

use Employee;

create table EmployeeDetails (
	Empid int primary key,
    Fullname varchar(20),
    ManagerId int, 
    DateOfJoining date, 
    City varchar(20)
);

create table EmployeeSalary(
	Empid int,
    Project varchar(10),
    Salary int,
    Variable int,
    foreign key (Empid) references EmployeeDetails(Empid)
);

INSERT INTO EmployeeDetails (EmpId, FullName, ManagerId, DateOfJoining, City)
VALUES
(121, 'John Snow', 321, '2019-01-31', 'Toronto'),
(321, 'Walter White', 986, '2020-01-30', 'California'),
(421, 'Kuldeep Rana', 876, '2021-11-27', 'Delhi');


INSERT INTO EmployeeSalary (EmpId, Project, Salary, Variable)
VALUES
(121, 'P1', 8000, 500),
(321, 'P2', 10000, 1000),
(421, 'P1', 12000, 0);

-- 1. Write an SQL query to fetch the EmpId and FullName of all the employees working
-- under the Manager with id – ‘986’.
select Empid,FullName
from EmployeeDetails
where ManagerId=986;

-- 2. Write an SQL query to fetch the different projects available from the EmployeeSalary table.
select Project
from EmployeeSalary;

-- 3. Write an SQL query to fetch the count of employees working in project ‘P1’
select Project,count(EmpId)
from EmployeeSalary
where Project='P1';

-- 4. Write an SQL query to find the maximum, minimum, and average salary of the employees. 
select max(Salary),min(Salary),avg(Salary)
from EmployeeSalary;

-- 5. Write an SQL query to find the employee id whose salary lies in the range of 9000 and 15000
select Empid,Salary
from EmployeeSalary
where Salary  between 9000 and 15000;

-- 6. Write an SQL query to fetch those employees who live in Toronto and work under the
-- manager with ManagerId – 321.
SELECT EmpId, City, ManagerId
FROM EmployeeDetails
WHERE City='Toronto' AND ManagerId='321'; 

-- 7. Write an SQL query to fetch all the employees who either live in California or work
-- under a manager with ManagerId – 321.
SELECT EmpId, City, ManagerId
FROM EmployeeDetails
WHERE City='California' OR ManagerId='321';

-- 8. Write an SQL query to fetch all those employees who work on Projects other than P1.
SELECT EmpId
FROM EmployeeSalary
WHERE  Project!='P1';

-- 9. Write an SQL query to display the total salary of each employee adding the Salary with
-- Variable value.
SELECT EmpId,
Salary+Variable as TotalSalary
FROM EmployeeSalary; 

-- 10. Write an SQL query to fetch the employees whose name begins with any two
-- characters, followed by a text “hn” and ends with any sequence of characters.
select Fullname
from EmployeeDetails
where Fullname like '__hn%';

-- 11. Write an SQL query to fetch all the EmpIds which are present in either of the tables –
-- ‘EmployeeDetails’ and ‘EmployeeSalary’.
SELECT EmpId FROM EmployeeDetails
UNION
SELECT EmpId FROM EmployeeSalary;

-- 12. Write an SQL query to fetch common records between two tables.
SELECT DISTINCT EmpId
FROM EmployeeDetails
WHERE EmpId IN (SELECT EmpId FROM EmployeeSalary);

-- 13. Write an SQL query to fetch records that are present in one table but not in another table.
SELECT e.*
FROM EmployeeDetails e
LEFT JOIN EmployeeSalary s
ON e.EmpId = s.EmpId
WHERE s.EmpId IS NULL;

-- 14. Write an SQL query to fetch the EmpIds that are present in both the tables -‘EmployeeDetails’ and ‘EmployeeSalary.
SELECT EmpId FROM
EmployeeDetails
where EmpId IN (SELECT EmpId 
				FROM EmployeeSalary);

-- 15. Write an SQL query to fetch the EmpIds that are present in EmployeeDetails but not in EmployeeSalary.
SELECT EmpId FROM
EmployeeDetails
where EmpId Not IN
(SELECT EmpId FROM EmployeeSalary);

-- 16. Write an SQL query to fetch the employee’s full names and replace the space with ‘-’.
SELECT REPLACE(FullName, ' ', '-') as newName
FROM EmployeeDetails; 

-- 17. Write an SQL query to fetch the position of a given character(s) in a field.
SELECT INSTR(FullName, 'Snow')
FROM EmployeeDetails; 

-- 18. Write an SQL query to display both the EmpId and ManagerId together.
SELECT CONCAT(EmpId, ManagerId) as NewId
FROM EmployeeDetails; 

-- 19. Write a query to fetch only the first name(string before space) from the FullName
-- column of the EmployeeDetails table.
select substring_index(FullName,' ',1) As FirstName
from EmployeeDetails;

-- 20. Write an SQL query to uppercase the name of the employee and lowercase the city values.
select ucase(FullName),lcase(City)
from EmployeeDetails;

-- 21. Write an SQL query to find the count of the total occurrences of a particular character – ‘n’ in the FullName field.
select FullName,length(FullName)-length(replace(FullName,'n','')) as Char_Count
from EmployeeDetails;

SET SQL_SAFE_UPDATES = 0;


-- 22. Write an SQL query to update the employee names by removing leading and trailing spaces
UPDATE EmployeeDetails
SET FullName = LTRIM(RTRIM(FullName))
WHERE EmpId IS NOT NULL;

-- 23. Write an SQL query to update the Salary field by value 10% in case of ‘Employee’ and 5% in case of ‘Manager’
update EmployeeSalary e
set Salary=case
		when e.EmpId in(
			select distinct ManagerId
            from EmployeeDetails
            where ManagerId is not null
        )
        then Salary*1.05
        else Salary*1.10
	end;

-- 24. Fetch all the employees who are not working on any project.
select EmpId 
from EmployeeSalary
where Project is null;

-- 25. Write an SQL query to fetch employee names having a salary greater than or equal to
-- 5000 and less than or equal to 10000.
SELECT FullName
FROM EmployeeDetails
WHERE EmpId IN
(SELECT EmpId FROM EmployeeSalary
WHERE Salary BETWEEN 5000 AND 10000);

-- 26. Write an SQL query to find the current date-time
select now();

-- 27. Write an SQL query to fetch all the Employee details from the EmployeeDetails table
-- who joined in the Year 2020.
select FullName
from EmployeeDetails
where year(DateOfJoining)=2020;

-- 28. Write an SQL query to fetch all employee records from the EmployeeDetails table who
-- have a salary record in the EmployeeSalary table.
SELECT *
FROM EmployeeDetails e
WHERE EXISTS (
    SELECT 1
    FROM EmployeeSalary s
    WHERE s.EmpId = e.EmpId
);

-- 29. Write an SQL query to fetch the project-wise count of employees sorted by project’s
-- count in descending order.
select count(EmpId),Project
from EmployeeSalary
group by project
order by Count(EmpId) desc;

-- 30. Write a query to fetch employee names and salary records. Display the employee
-- details even if the salary record is not present for the employee.
SELECT E.FullName, S.Salary
FROM EmployeeDetails E
LEFT JOIN
EmployeeSalary S
ON E.EmpId = S.EmpId; 

-- 31. Write an SQL query to join 3 tables.
SELECT
    e.EmpId,
    e.FullName AS EmployeeName,
    m.FullName AS ManagerName
from EmployeeDetails e
LEFT JOIN EmployeeSalary s
    ON e.EmpId = s.EmpId
LEFT JOIN EmployeeDetails m
    ON e.ManagerId = m.EmpId;
    
    
-- 32. Write an SQL query to fetch all the Employees who are also managers from the
-- EmployeeDetails table.
SELECT DISTINCT m.FullName
FROM EmployeeDetails e
JOIN EmployeeDetails m
ON e.ManagerId = m.EmpId;

-- 33. Write an SQL query to fetch duplicate records from EmployeeDetails (without
-- considering the primary key – EmpId).
select FullName,ManagerId,DateOfJoining,City,count(*)
from EmployeeDetails
group by FullName,ManagerId,DateOfJoining,City
having count(*)>1;

-- 34. Write an SQL query to remove duplicates from a table without using a temporary table.
delete e1
from EmployeeDetails e1
join EmployeeDetails e2
on e1.FullName=e2.FullName
and e1.EmpId>e2.EmpId;

-- 35. Write an SQL query to fetch only odd rows from the table.
-- 36. Write an SQL query to fetch only even rows from the table.

-- 37. Write an SQL query to create a new table with data and structure copied from another table. 
create table newTable
select * from EmployeeDetails;

-- 38. Write an SQL query to create an empty table with the same structure as some other table.
create table newTabblo
select * from EmployeeDetails
where 1=0;

-- 39. Write an SQL query to fetch top n records
select *
from EmployeeSalary
order by Salary desc limit 2;

-- 40. Write an SQL query to find the nth highest salary from a table.
select Salary
from EmployeeSalary
order by Salary desc limit 2,1;

SELECT Salary
FROM EmployeeSalary e1
WHERE 1 = (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM EmployeeSalary e2
    WHERE e2.Salary > e1.Salary
);

-- 41. Write SQL query to find the 3rd highest salary from a table without using the TOP/limit keyword. 
SELECT Salary
FROM EmployeeSalary e1
WHERE 2 = (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM EmployeeSalary e2
    WHERE e2.Salary > e1.Salary
);

-- 42. Consider a SalesData with columns SaleID, ProductID, RegionID, SaleAmount. Write a
-- query to find the total sales amount for each product in each region.
SELECT ProductID, RegionID, SUM(SaleAmount) AS TotalSales
FROM SalesData
GROUP BY ProductID, RegionID; 

-- 43. Write a query to find employees who earn more than their managers. 
select e.FullName as EmployeeName,
e.EmpId as EmployeeId,
s1.Salary as EmployeeSalary,
m.FullName as ManagerName,
s2.Salary as ManagerSalary
from EmployeeDetails e
join EmployeeDetails m on e.ManagerId=m.EmpId
join EmployeeSalary s1 on e.EmpId=s1.EmpId
join EmployeeSalary s2 on m.EmpId=s2.EmpId
where s1.Salary > s2.Salary;

-- 44. Consider a BookCheckout table with columns
-- CheckoutID, MemberID, BookID, CheckoutDate, ReturnDate. Write an SQL query to find
-- the number of books checked out by each member.
SELECT MemberID, COUNT(*) AS NumberOfBooksCheckedOut
FROM BookCheckout
GROUP BY MemberID; 

-- 45. Consider a StudentGrades table with columns – StudentID, CourseID, Grade. Write a
-- query to find students who have scored an ‘A’ in more than three courses. 
SELECT StudentID
FROM StudentGrades
WHERE Grade = 'A'
GROUP BY StudentID
HAVING COUNT(*) > 3;

-- 46. Consider a table OrderDetails with columns
-- OrderID, CustomerID, ProductID, OrderDate, QuanƟty, Price. Write a query to find the
-- average order value for each customer. 
SELECT CustomerID, AVG(QuanƟty * Price) AS AvgOrderValue
FROM OrderDetails
GROUP BY CustomerID; 

-- 47. Consider a table PaƟentVisits with
-- Columns VisitID, PaƟentID, DoctorID, VisitDate, Diagnosis. Write a query to find the latest
-- visit date for each paƟent.
SELECT PatientID, MAX(VisitDate) AS LatestVisitDate
FROM PatientVisits
GROUP BY PatientID;

-- 48. For a table FlightBookings with columns
-- BookingID, FlightID, PassengerID, BookingDate, TravelDate, Class, write a query to count
-- the number of bookings for each flight class
SELECT Class, COUNT(*) AS NumberOfBookings
FROM FlightBookings
GROUP BY Class; 

-- 49. Consider a table FoodOrders with columns
-- OrderID, TableID, MenuItemID, OrderTime, QuanƟty. Write a query to find the most
-- ordered menu item. 
SELECT MenuItemID
FROM FoodOrders
GROUP BY MenuItemID
ORDER BY COUNT(*) DESC
LIMIT 1; 

-- 50. Consider a table TransacƟons with columns
-- TransacƟonID, CustomerID, ProductID, TransacƟonDate, Amount. Write a query to find
-- the total transacƟon amount for each month.
SELECT MONTH(TransacƟonDate) AS Month,
SUM(Amount) AS TotalAmount
FROM TransacƟons
GROUP BY MONTH(TransacƟonDate);

-- 51. Consider a table EmployeeAttendance with columns
-- AttendanceID, EmployeeID, Date, Status. Write a query to find employees with more
-- than 5 absences in a month. 
SELECT EmployeeID,
MONTH(Date) AS Month,
COUNT(*) AS Absences
FROM EmployeeAƩendance
WHERE Status = 'Absent'
GROUP BY EmployeeID, MONTH(Date)
HAVING COUNT(*) > 5; 










