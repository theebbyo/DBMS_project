CREATE TABLE users (
    id INT  PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    role ENUM('STUDENT', 'TEACHER') NOT NULL
    

);

create table students (
    id int  primary key,
    institution varchar(255) not null,
    address varchar(255) not null,
    user_id int not null,
    foreign key (user_id) references users(id)
);

create table teachers (
    id int  primary key,
    institution varchar(255) not null,
    user_id int not null,
    expertize varchar(255) not null,
    foreign key (user_id) references users(id)
);




create table payments(
    id int  primary key,
    amount int not null,
    user_id int not null,
    foreign key (user_id) references users(id)
);

create table requests(
    id int  primary key,
    teacher_id int not null,
    student_id int not null,
    foreign key (student_id) references users(id),
    foreign key (teacher_id) references users(id)
);
-- # below two table not inserted yet
create table tuition(
    id int primary key,
    student_id int,
    teacher_id int,
    foreign key (student_id) references users(id),
    foreign key (teacher_id) references users(id)
)