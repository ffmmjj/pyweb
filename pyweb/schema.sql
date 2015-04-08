drop table if exists users;
create table users (
  id integer primary key autoincrement,
	username text not null,
	password text not null
);

insert into users (id, username, password) values (1, 'john', 'johnpass');
insert into users (id, username, password) values (2, 'susan', 'susanpass');
