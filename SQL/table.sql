CREATE TABLE users (
    id INT  PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    role ENUM('STUDENT', 'TEACHER') NOT NULL
    

);



create table students (
    institution varchar(255) not null,
    address varchar(255) not null,
    user_id int primary key,
    foreign key (user_id) references users(id)
);



create table teachers (
    institution varchar(255) not null,
    user_id int primary key,
    expertize varchar(255) not null,
    foreign key (user_id) references users(id)
);




create table payments(
    amount int not null,
    user_id int  primary key,
    foreign key (user_id) references users(id)
);



create table requests(
    id int  primary key,
    teacher_id int not null,
    student_id int not null,
    send_at datetime default current_timestamp,
    foreign key (student_id) references users(id),
    foreign key (teacher_id) references users(id)
);




create table tuitions(
    id int primary key,
    
    teacher_id int,
    student_id int,
    created_at datetime default current_timestamp,
    foreign key (student_id) references users(id),
    foreign key (teacher_id) references users(id)
);



create table tuitionDates(
    id int primary key,
    tuition_id int,
    date datetime default current_timestamp,
    foreign key (tuition_id) references tuitions(id)
);



create table pendingPayements(
    id int primary key,

    tuition_id int,
    amount int default 0,
    foreign key (tuition_id) references tuitions(id)
);



create table messages(
    id int primary key,
    tuition_id int,
    message varchar(255),
    send_at datetime default current_timestamp,
    sender ENUM('STUDENT', 'TEACHER') NOT NULL,
    foreign key (tuition_id) references tuitions(id)
);



create table notifications(
    id int primary key,
    teacher_id int,
    student_id int,
    message varchar(255),
    send_at datetime default current_timestamp,
    toShow ENUM('STUDENT', 'TEACHER') NOT NULL,
    foreign key (student_id) references users(id),
    foreign key (teacher_id) references users(id)
);



create table makePayements(
    id int primary key,
    tuition_id int,
    amount int default 0,
    transaction_id varchar(255),
    send_at datetime default current_timestamp,
    foreign key (tuition_id) references tuitions(id)
);

create table account(
    user_id int primary key,
    balance int default 0,
    foreign key (user_id) references users(id)
); 


create table reviews(
    id int primary key,
    teacher_id int,
    student_id int,
    review varchar(255),
    rating float default 5,
    send_at datetime default current_timestamp,
    foreign key (student_id) references users(id),
    foreign key (teacher_id) references users(id)
);