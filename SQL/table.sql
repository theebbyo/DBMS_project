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