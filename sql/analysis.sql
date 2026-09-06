-- 1: Average salary by department
SELECT 
	department,
	AVG(salary) AS avgsal
FROM employees
GROUP BY department
ORDER BY avgsal DESC;

-- 2: Top 10 Highest-paid employees
SELECT 
	employee_id, 
	employee_name, 
	department, 
	salary
FROM employees
ORDER BY salary DESC
LIMIT 10;

-- 3: Salary ranking within departments
WITH ranks AS(
	SELECT 
		employee_id, 
		employee_name, 
		department, 
		salary, 
		RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS salary_rank
	FROM employees
)

SELECT * 
FROM ranks
WHERE salary_rank < 4

-- 4: Employees hired per year
SELECT
	EXTRACT(year FROM joining_date) AS Year,
	COUNT(*) AS employees_hired
FROM employees
GROUP BY Year
ORDER BY Year

-- 5: Department salary comparison
SELECT
	department, 
	MIN(salary) AS minimum_salary,
	AVG(salary) AS average_salary, 
	MAX(salary) AS maximum_salary
FROM employees
GROUP BY department

-- 6: 10 Employees just above overall average salary
SELECT
	employee_id, 
	employee_name, 
	department, 
	salary
FROM employees
WHERE salary > (
				SELECT 
					AVG(salary)
				FROM employees
				)
ORDER BY salary
LIMIT 10;

-- 7: Top 0.1% earners per department
WITH details AS (
	SELECT
		employee_id, 
		employee_name, 
		department, 
		salary, 
		NTILE(1000) OVER(PARTITION BY department ORDER BY salary DESC) AS salary_rank,
		COUNT(*) OVER(PARTITION BY department) AS department_size
	FROM employees
)

SELECT *
FROM details
WHERE salary_rank=1

-- 8: Duplicate employee IDs
SELECT 
	employee_id,
	COUNT(*) AS employee_count
FROM employees
GROUP BY employee_id
HAVING COUNT(*) > 1