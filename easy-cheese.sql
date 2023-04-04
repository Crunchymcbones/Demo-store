DROP DATABASE IF EXISTS easy_cheese;
CREATE DATABASE easy_cheese;
use easy_cheese;

-- create the customers table --
CREATE TABLE customers (
    customer_id     INT             AUTO_INCREMENT      PRIMARY KEY,
    first_name      VARCHAR(20)     NOT NULL,
    last_name		VARCHAR(20)     NOT NULL,
    address         VARCHAR(100),
    email_address   VARCHAR(50)     NOT NULL,
    phone_number    VARCHAR(15)     NOT NULL
);

-- create the customers table
CREATE TABLE products (
    product_id      INT             AUTO_INCREMENT      PRIMARY KEY,
    name            VARCHAR(20)     NOT NULL,
    product_desc    VARCHAR(100),
    vendor_id       INT             NOT NULL,
    in_store_qty             INT             NOT NULL,
    price           DECIMAL(9,2)    NOT NULL
);

-- create the invoices table
CREATE TABLE invoices (
    invoice_id      INT             AUTO_INCREMENT      PRIMARY KEY,
    customer_id     INT             NOT NULL,
    date            DATETIME        NOT NULL,
CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


-- intermediary table for invoices & products --
CREATE TABLE invoice_line_items (
    invoice_id      INT             NOT NULL,
    product_id      INT             NOT NULL,
    qty             INT             NOT NULL,
    CONSTRAINT invoice_product_pk PRIMARY KEY (invoice_id, product_id)
);

-- create views -- 
create view complete_invoice as
select i.invoice_id, concat(c.first_name, " ", c.last_name) as name, c.email_address, c.phone_number, sum(li.qty * p.price) as 'item total', 
round(sum(li.qty * p.price)*0.15, 2) as 'invoice tax',round(sum(li.qty * p.price)*1.15, 2) as "invoice total", sum(li.qty) as 'items purchased'
from invoices i join customers c on i.customer_id = c.customer_id
join invoice_line_items li on i.invoice_id = li.invoice_id
join products p on li.product_id = p.product_id
group by i.invoice_id;

-- *****************
-- *  sample data  *
-- *****************

-- sample data for customers --

INSERT INTO customers (first_name, last_name, address, email_address, phone_number)
VALUES  ("parker","wallace",  "45 address way",   "parwal@yahoo.com",     "XXX-XXX-1234"),
        ("dylan","mercer",   "16 address st",    "dylmer@gmail.com",     "XXX-XXX-4565"),
        ("josh","Oram",   "32 address ave",   "joshar@hotmail.ca",    "XXX-XXX-7895"),
        ("sheham","mohammed",  "57 address cr",    "sheha@protom.lol",     "XXX-XXX-3698");


-- sample data for products --

INSERT INTO products (name, product_desc, vendor_id, in_store_qty, price)
VALUES  ("brie",      "a soft disc of cheese",  1, 17, 10.99),
        ("cheddar",   "a sharp classic",        2, 50, 5.49),
        ("parmesian", "a hard italian cheese",  1, 10, 25.99);


-- sample data for invoices --

INSERT INTO invoices (invoice_id, customer_id, date)
VALUES  (1,3,"2023-03-27"),
        (2,4,"2023-01-20"),
        (3,2,"2000-08-19"),
        (4,2,"2020-12-25");

-- sample data for invoice line item

insert into invoice_line_items(invoice_id, product_id, qty)
VALUES  (1,1,42),   (1,2,23),   (1,3,69),   (1,4,27),
        (2,1,1642), (2,2,7),    (2,3,8),    (2,4,1),
        (3,1,6),    (3,2,4),    (3,3,4),    (3,4,2),
        (4,1,12),   (4,2,30),   (4,3,7),    (4,4,5);



