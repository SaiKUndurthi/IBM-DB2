--Task 1
DROP TABLE  INSTRUCTOR;
Create table Instructor (
ins_id Integer not null Primary Key,
lastname varchar(25) not null,
firstname varchar(25) not null,
city varchar(25),
country char(2)
);
insert into Instructor values(1, 'Ahuja', 'Rav', 'Toronto', 'CA'); 
insert into Instructor values (2, 'Chong', 'Raul', 'Toronto', 'CA'),
(3, 'Vasudevan', 'Hima', 'Chicago', 'US');
select * from Instructor;
select firstname, lastname, country from Instructor where city = 'Toronto';
update Instructor set city = 'Markham' where ins_id = 1;
delete from Instructor where ins_id = 2;
select * from Instructor;
--End of Task 1
