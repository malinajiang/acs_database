drop table if exists acs_data;

create table acs_data(id INTEGER PRIMARY KEY AUTOINCREMENT, var_name TEXT, value INTEGER, units TEXT, update_time INTEGER, original_table TEXT);