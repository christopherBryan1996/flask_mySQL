use heroku_5ac5dbad874fd18;

create table curso(
	codigo char (6) not null,
    nombre varchar(30) not null,
    creditos tinyint(1) not null,
    primary key(codigo)
);

describe curso;

insert into curso
values ('325817','matematicas basicas','5');