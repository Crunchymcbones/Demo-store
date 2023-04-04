DROP DATABASE IF EXISTS easy_cheese;

--*********************** 
--* CREATE THE DATABASE *
--***********************

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
    in_store_qty    INT             NOT NULL,
    price           DECIMAL(9,2)    NOT NULL,
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

CREATE VIEW complete_invoice AS
SELECT 
	i.invoice_id, 
	concat(c.first_name, " ", c.last_name) AS 'name', 
	c.email_address, c.phone_number, sum(li.qty * p.price) AS 'item total', 
	round(sum(li.qty * p.price)*0.15, 2) AS 'invoice tax',
	round(sum(li.qty * p.price)*1.15, 2) AS "invoice total", 
	sum(li.qty) AS 'items purchased'
FROM 
	invoices i 
	JOIN customers as c ON i.customer_id = c.customer_id
	JOIN invoice_line_items as li ON i.invoice_id = li.invoice_id
	JOIN products as p ON li.product_id = p.product_id
GROUP BY 
	i.invoice_id;

-- create stored procedures --
delimiter //
create procedure active_customers (months int)
begin
select 
	concat(c.last_name, ", ", c.first_name) as 'customer', 
	date(max(i.date)) as 'last active'
from 
	customers c join invoices i on c.customer_id = i.customer_id 
where 
	timestampdiff(month,i.date,date(now())) > 6
group by concat(c.last_name, ", ", c.first_name);
end //
delimiter ;
   
-- *****************
-- *  SAMPLE DATA  *
-- *****************

-- sample data for customers --
INSERT INTO customers (first_name, last_name, address, email_address, phone_number)
VALUES  
	("parker","wallace","45addressway","parwal@yahoo.com","XXX-XXX-1234"),
	("dylan","mercer","16addressst","dylmer@gmail.com","XXX-XXX-4565"),
	("josh","Oram","32addressave","joshar@hotmail.ca","XXX-XXX-7895"),
	("sheham","mohammed","57addresscr","sheha@protom.lol","XXX-XXX-3698"),
	('Nichol','Tarver','1261SpringviewAvenue','ntarver0@paypal.com','933-686-3927'),
	('Adel','Kydd','07823EschPlace','akydd1@unblog.fr','450-811-3462'),
	('Hinda','Tidder','4719RedwingHill','htidder2@wsj.com','722-698-1338'),
	('Thoma','Cashford','7987TalismanTerrace','tcashford3@spotify.com','989-968-0224'),
	('Sallyanne','Oxbie','12WaxwingAvenue','soxbie4@biglobe.ne.jp','865-520-2570'),
	('Gwenni','Roalfe','35WayridgeCourt','groalfe5@mashable.com','679-868-3251'),
	('Valerie','Willerton','7234EschTrail','vwillerton6@ftc.gov','823-587-2640'),
	('Angie','Lammertz','8549ManleyParkway','alammertz7@tripadvisor.com','289-806-1995'),
	('Broderic','Bonnette','3MonumentPlaza','bbonnette8@seattletimes.com','456-155-1220'),
	('Bree','Lusher','35678GinaLane','blusher9@webnode.com','295-526-9920'),
	('Tiler','Towsie','52165CrownhardtJunction','ttowsiea@hugedomains.com','191-150-5788'),
	('Jenilee','Keech','642DelladonnaTerrace','jkeechb@intel.com','435-778-9711'),
	('Roseann','Turmel','213StuartJunction','rturmelc@epa.gov','943-666-7277'),
	('Fay','Coad','3256OrioleStreet','fcoadd@nba.com','217-925-7301'),
	('Derron','Pavlenko','9AmericanAshTrail','dpavlenkoe@barnesandnoble.com','383-459-1983'),
	('Eleonora','Bunce','57GolfViewParkway','ebuncef@ed.gov','365-572-4146');
        
-- sample data for products --
INSERT INTO products (name, product_desc, vendor_id, in_store_qty, price)
VALUES  
	("brie","asoftdiscofcheese",1,17,10.99),
	("cheddar","asharpclassic",2,50,5.49),
	("parmesian","aharditaliancheese",1,10,25.99),
	('QuesoMajorero','placeratante',4,39,2.95),
	('Northumberland','suscipitafeugiat',9,4,4.36),
	('Kikorangi','justositametsapiendigni',3,86,1.51),
	('Selva','erattortorsollicitudinmisitametlobortis',6,25,1.02),
	('Beauvoorde','interdummauris',8,88,9.94),
	('MozzarellaFresh','quamfringillarhoncus',6,18,1.16),
	('LlanglofanFarmhouse','pedejusto',1,43,1.36),
	('Friesla','tinciduntlacusatvelitvivamusvelnulla',9,19,4.58),
	('Anthoriro','phasellusinfelisdonecsempersapiena',4,64,1.65),
	('DreuxalaFeuille','ultricesposuerecubiliacurae',3,45,4.10),
	('Rustinu','nullammolestienibhinlectuspellentesqueat',7,54,8.04),
	('SomersetBrie','suscipitafeugiateterosvestibulum',5,5,6.03),
	('Civray','euminullaacenimin',3,71,3.15),
	('Cheddar','dapibusdolor',7,33,6.02),
	('FreshTruffles','tortorduismattisegestasmetusaenean',5,87,9.75),
	('Chaource','vehiculacondimentumcurabiturinlibero',3,85,1.46),
	('Acorn','fermentumjustoneccondimentum',8,46,5.93);

-- sample data for invoices --
INSERT INTO invoices (invoice_id, customer_id, date)
VALUES  
	(1,13,'2022-05-22'),
	(2,15,'2021-03-05'),
	(3,16,'2016-12-31'),
	(4,17,'2021-09-16'),
	(5,14,'2018-01-03'),
	(6,1,'2019-01-18'),
	(7,11,'2020-03-12'),
	(8,14,'2017-08-11'),
	(9,5,'2021-10-07'),
	(10,12,'2022-08-05'),
	(11,1,'2016-03-22'),
	(12,14,'2018-09-12'),
	(13,20,'2023-01-26'),
	(14,20,'2020-04-13'),
	(15,13,'2015-11-10'),
	(16,2,'2021-11-25'),
	(17,19,'2017-10-26'),
	(18,17,'2021-09-18'),
	(19,11,'2019-12-19'),
	(20,15,'2020-06-19');
    
-- sample data for invoice line item
INSERT INTO invoice_line_items(invoice_id, product_id, qty)
VALUES  
	(17,8,13),
	(18,16,20),
	(19,16,1),
	(20,18,5),
	(1,11,2),
	(2,6,9),
	(3,8,1),
	(4,19,19),
	(5,8,7),
	(6,15,1),
	(7,20,10),
	(8,4,16),
	(9,1,16),
	(10,17,9),
	(11,12,15),
	(12,11,10),
	(13,16,1),
	(14,17,14),
	(15,10,8),
	(16,6,19),
	(17,4,3),
	(18,14,13),
	(19,17,12),
	(20,4,7);