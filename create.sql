drop table if exists "restaurants";
create table restaurants(
	res_id int primary key not null,
	name varchar(255) not null,
	address varchar(255) default null,
	city varchar(255) default null,
	zip_code varchar(255) default null,
	phone_number varchar(255) default null,
	website varchar(255) default null
);

drop table if exists "restaurant_info";
create table restaurant_info(
	res_id INT primary key not null,
	tax_code varchar(255) default null,
	certificate varchar(255) default null,
	foreign key (res_id) references restaurants
);

drop table if exists "owner";
create table owner(
	res_id int not null,
	owner_name varchar(255) not null,
	owner_address varchar(255) default null,
	owner_city varchar(255) default null,
	owner_zip_code varchar(255) default null,
	owner_phone_number varchar(255) default null,
	foreign key (res_id) references restaurants,
	primary key (res_id, owner_name)
);

drop table if exists "cuisines";
create table cuisines(
	cuisine_id int primary key not null,
    cuisine_name varchar(255) default null,
	calories int default null,
	ingredients varchar(255) default null
);

drop table if exists "menu_items";
create table menu_items(
	res_id int not null,
	cuisine_id int not null,
    dish_name varchar(255) not null,
	description varchar(255) default null,
	price varchar(255) not null,
	foreign key (res_id) references restaurants,
	foreign key (cuisine_id) references cuisines,
	primary key(res_id, cuisine_id, dish_name)
);

drop table if exists "reviews";
create table reviews(
	res_id int not null,
	rating int not null,
	reviewer_email varchar(255) not null,
	comments varchar(255) default null,
	foreign key (res_id) references restaurants,
	primary key(res_id, reviewer_email)
);