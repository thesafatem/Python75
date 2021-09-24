create database decode;

create table course (
	id int auto_increment primary key,
    name varchar(255),
    duration int
);

insert into course(name, duration) values
	('C++', 2),
    ('PHP', 4),
	('Olymp', 6); 
    
-- insert into course(-- id, name) values
-- 	(1, 'Python');
    
-- drop table course;

-- delete from course where name = 'Python';


create table student(
	id int auto_increment primary key,
    first_name varchar(255),
    last_name varchar(255),
    email varchar(255),
    phone_number char(12)
);

insert into student(first_name, last_name, email, phone_number) values
	('Ildar', 'Gilmanov', 'abc@gmail.com', '+77777777777'),
    ('Bekaidar', 'Myrzabekov', 'def@mail.ru', '+77012211184');

select * from student;

select * from student where id = 1;


create table teacher(
	id int auto_increment primary key,
    first_name varchar(255),
    last_name varchar(255)
);

insert into teacher(first_name, last_name) values
('Temirlan', 'Safargaliyev'),
('Derbes', 'Utebaliyev');

select * from teacher;


create table _group(
	id int auto_increment primary key,
    number int not null,
    course_id int not null,
    teacher_id int not null,
    foreign key (course_id) references course(id),
    foreign key (teacher_id) references teacher(id)
);

insert into _group(number, course_id, teacher_id) values
(75, 1, 1),
(30, 2, 2);

select * from _group;

create table group_student(
	id int auto_increment primary key,
    student_id int not null,
    group_id int not null,
    foreign key (student_id) references student(id),
    foreign key (group_id) references _group(id)
);

insert into group_student(student_id, group_id) values
	(1, 1),
	(2, 1),
	(1, 2),
	(2, 2);

select * from group_student;


select * from student where email like '_%@gmail.com';

insert into student(first_name, last_name, email, phone_number) values
	('Zhandos', 'Zhandosov', '@gmail.com', '+77777777777');
    
-- % - строка любой длины (0, +бесконечность)
-- _ - строго один символ

select * from course where duration < 4 and name like "___n%";

select * from course order by duration desc;

select * from course order by name;

insert into course(name, duration) values
	('Pascal', 5);
    
select * from course where duration between 3 and 5;

select name from course where name between 'a' and 'o';

select count(id) as count from course;

select distinct duration from course;

select duration, count(*) as count from course group by duration;

select * from course where duration = 2 or duration = 4 or duration = 6;

select * from course where duration in (2, 4, 6);

select name, sum(duration) from course group by name;

select sum(duration) from course;

-- interaction between tables

select first_name, last_name from student where id in 
(select student_id from group_student where group_id = 1);

