-- Write query to get number of graded assignments for each student:
select student_id, count(*) as graded_assignments from assignments where state='GRADED' group by student_id;
