-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
with most_graded_teacher as (
select teacher_id, count(*) as graded_assignments from assignments where state='GRADED' group by teacher_id order by graded_assignments desc limit 1
)
select count(*) a_grades from assignments where teacher_id = (select teacher_id from most_graded_teacher) and grade = 'A';
