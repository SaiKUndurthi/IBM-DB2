select * from Employees where address like '%Elgin,IL%';
select * from Employees where b_date like '197%';
select * from Employees where DEP_ID = 5 and salary between 60000 and 70000;
select * from Employees order by dep_id desc, l_name desc;
select DEP_ID,count(*)as NUM_EMPLOYEES, avg(salary) as AVG_SALARY from Employees group by DEP_ID having count(*) < 4 order by AVG_SALARY;
select * from Employees E, Departments D where E.DEP_ID = D.DEPT_ID_DEP order by DEP_NAME, l_name desc;