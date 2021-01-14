-- SELECT with conditions 

select *
from emp
where deptno = 10
     or comm is not null
     or sal <= 2000 and deptno=20

-- SELECT with conditions brackets
select *
from emp
where ( deptno = 10
        or comm is not null
        or sal <= 2000
      )
      and deptno=20
      
--SELECT with aliased new column names
select sal as salary, comm as commission
from emp

-- Alias filtering 
select *
from (
select sal as salary, comm as commission
from emp
        ) x
 where salary < 5000
 
-- Concatenating columns
select ename + ' WORKS AS A ' + job as msg
from emp
where deptno=10

--- conditional logic
select ename,sal,
        case when sal <= 2000 then 'UNDERPAID'
             when sal >= 4000 then 'OVERPAID'
             else 'OK'
        end as status
   from emp
   
-- serching for patterns
 select ename, job
   from emp
  where deptno in (10,20)
      and (ename like '%I%' or job like '%ER')
