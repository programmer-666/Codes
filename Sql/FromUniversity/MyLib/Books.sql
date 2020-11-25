use mylib;
CREATE TABLE books(
id_book int AUTO_INCREMENT PRIMARY KEY,
name_book VARCHAR(32),
nop_book smallint,
id_category int,
id_publisher int,
id_writer int,
FOREIGN KEY (id_category) REFERENCES categories(id_category),
FOREIGN KEY (id_publisher) REFERENCES publishers(id_publisher),
FOREIGN KEY (id_writer) REFERENCES writers(id_writer),
printno_book int,
printdate_book year,
explanation_book text,
price int
);