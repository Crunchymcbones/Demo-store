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
    in_store_qty    INT             NOT NULL,
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
VALUES  
	("parker","wallace","45addressway","parwal@yahoo.com","XXX-XXX-1234"),("dylan","mercer","16addressst","dylmer@gmail.com","XXX-XXX-4565"),
	("josh","Oram","32addressave","joshar@hotmail.ca","XXX-XXX-7895"),("sheham","mohammed","57addresscr","sheha@protom.lol","XXX-XXX-3698"),
	('Nichol','Tarver','1261SpringviewAvenue','ntarver0@paypal.com','933-686-3927'),('Adel','Kydd','07823EschPlace','akydd1@unblog.fr','450-811-3462'),
	('Hinda','Tidder','4719RedwingHill','htidder2@wsj.com','722-698-1338'),('Thoma','Cashford','7987TalismanTerrace','tcashford3@spotify.com','989-968-0224'),
	('Sallyanne','Oxbie','12WaxwingAvenue','soxbie4@biglobe.ne.jp','865-520-2570'),('Gwenni','Roalfe','35WayridgeCourt','groalfe5@mashable.com','679-868-3251'),
	('Valerie','Willerton','7234EschTrail','vwillerton6@ftc.gov','823-587-2640'),('Angie','Lammertz','8549ManleyParkway','alammertz7@tripadvisor.com','289-806-1995'),
	('Broderic','Bonnette','3MonumentPlaza','bbonnette8@seattletimes.com','456-155-1220'),('Bree','Lusher','35678GinaLane','blusher9@webnode.com','295-526-9920'),
	('Tiler','Towsie','52165CrownhardtJunction','ttowsiea@hugedomains.com','191-150-5788'),('Jenilee','Keech','642DelladonnaTerrace','jkeechb@intel.com','435-778-9711'),
	('Roseann','Turmel','213StuartJunction','rturmelc@epa.gov','943-666-7277'),('Fay','Coad','3256OrioleStreet','fcoadd@nba.com','217-925-7301'),
	('Derron','Pavlenko','9AmericanAshTrail','dpavlenkoe@barnesandnoble.com','383-459-1983'),('Eleonora','Bunce','57GolfViewParkway','ebuncef@ed.gov','365-572-4146'),
	('Arch','Freckleton','84244ShastaPlace','afreckletong@chicagotribune.com','727-792-5676'),('Isacco','Libbie','79845GolfPlaza','ilibbieh@drupal.org','832-607-7913'),
	('Dilan','Yewdall','4912ndAvenue','dyewdalli@mapy.cz','251-480-2210'),('Matthias','Sandon','8268ThompsonCenter','msandonj@addtoany.com','681-140-4937'),
	('Franky','Christauffour','4CaliangtParkway','fchristauffourk@over-blog.com','990-233-7891'),('Randi','Pauls','856ScovilleDrive','rpaulsl@simplemachines.org','742-855-8261'),
	('Brooke','Whichelow','258MapleWoodAlley','bwhichelowm@icq.com','636-650-9264'),('Hali','Osgorby','8739LindenPoint','hosgorbyn@arizona.edu','222-330-6166'),
	('Mirabel','Dillow','6303EverettParkway','mdillowo@oracle.com','753-743-9474'),('Brina','Stork','232MerchantParkway','bstorkp@yellowbook.com','373-224-4907'),
	('Reba','Perrington','9MerryTerrace','rperringtonq@mashable.com','502-396-9726'),('Emlynn','Tulip','263LoftsgordonRoad','etulipr@skyrock.com','312-269-0335'),
	('Alexandre','Ashborn','0MayerLane','aashborns@statcounter.com','749-729-5994'),('Carlee','Crack','97IowaJunction','ccrackt@cam.ac.uk','191-952-3968'),
	('Elwin','Ishak','6UnionWay','eishaku@fema.gov','169-741-1415'),('Kerry','Dimberline','3482OneillPlaza','kdimberlinev@columbia.edu','837-784-4053'),
	('Sapphire','Overton','6DrewryPoint','sovertonw@arstechnica.com','737-101-1242'),('Joshuah','Jerche','49MockingbirdDrive','jjerchex@sbwire.com','445-925-3257'),
	('Edwin','Gabriely','3138FlorenceDrive','egabrielyy@webmd.com','870-824-9963'),('Leicester','Jozsa','715KilldeerStreet','ljozsaz@csmonitor.com','348-256-1011'),
	('Etheline','Mellsop','213017thCourt','emellsop10@163.com','132-691-2516'),('Anissa','Kensall','9755MuirParkway','akensall11@foxnews.com','356-737-1715'),
	('Maud','Burberry','59MapleWoodTrail','mburberry12@naver.com','524-647-9756'),('Carmelina','Wareing','7393StangPlace','cwareing13@imageshack.us','702-427-6247'),
	('Krystle','Spivey','2BluestemCrossing','kspivey14@joomla.org','155-645-0815'),('Colas','Jochens','4361NorthlandParkway','cjochens15@bing.com','438-365-3542'),
	('Lesly','Gilman','39MarcyCenter','lgilman16@deviantart.com','917-386-0847'),('Klarika','Haire','6RidgeOakWay','khaire17@opensource.org','844-591-3215'),
	('Mahalia','Jendrach','3214WaxwingCourt','mjendrach18@plala.or.jp','479-152-2645'),('Cyrillus','Laurentin','8392GeraldPoint','claurentin19@tinypic.com','830-847-2190'),
	('Merry','Slimings','42SullivanLane','mslimings1a@nyu.edu','609-714-1444'),('Bridgette','Spilisy','08LindenTerrace','bspilisy1b@noaa.gov','332-260-0108'),
	('Shelia','Berndsen','97BrowningCircle','sberndsen1c@163.com','755-212-9802'),('Marice','Genever','5AbergStreet','mgenever1d@upenn.edu','951-771-1091'),
	('Cassy','Vaughten','1349DaystarPlace','cvaughten1e@google.co.jp','426-422-7013');
        


-- sample data for products --
INSERT INTO products (name, product_desc, vendor_id, in_store_qty, price)
VALUES  
	("brie","asoftdiscofcheese",1,17,10.99),("cheddar","asharpclassic",2,50,5.49),
	("parmesian","aharditaliancheese",1,10,25.99),('QuesoMajorero','placeratante',4,39,2.95),
	('Northumberland','suscipitafeugiat',9,4,4.36),('Kikorangi','justositametsapiendigni',14,86,1.51),
	('Selva','erattortorsollicitudinmisitametlobortis',12,25,1.02),('Beauvoorde','interdummauris',8,88,9.94),
	('MozzarellaFresh','quamfringillarhoncus',6,18,1.16),('LlanglofanFarmhouse','pedejusto',1,43,1.36),
	('Friesla','tinciduntlacusatvelitvivamusvelnulla',9,19,4.58),('Anthoriro','phasellusinfelisdonecsempersapiena',4,64,1.65),
	('DreuxalaFeuille','ultricesposuerecubiliacurae',14,45,4.10),('Rustinu','nullammolestienibhinlectuspellentesqueat',7,54,8.04),
	('SomersetBrie','suscipitafeugiateterosvestibulum',11,5,6.03),('Civray','euminullaacenimin',3,71,3.15),
	('Cheddar','dapibusdolor',7,33,6.02),('FreshTruffles','tortorduismattisegestasmetusaenean',11,87,9.75),
	('Chaource','vehiculacondimentumcurabiturinlibero',14,85,1.46),('Acorn','fermentumjustoneccondimentum',8,46,5.93),
	('Fougerus','ultriceserattortor',11,6,1.13),('Parmesan','maurislaciniasapienquisliberonullamsit',1,28,0.64),
	('Juustoleipa','donecutmaurisegetmassa',8,20,3.51),('Lavistown','sapienplaceratantenullajusto',7,99,5.95),
	('BeerCheese','curaeduisfaucibusaccumsan',12,67,0.91),('CypressGroveChevre','namduiproinleo',2,42,3.35),
	('Rubens','sedmagnaatnunccommodo',14,11,5.74),('Explorateur','crasnon',9,40,7.52),
	('FromageFrais','velaccumsan',13,78,9.60),('Roule','tempussemperestquampharetramagnaac',15,94,9.72),
	('Blarney','eunibhquisqueidjustositamet',9,70,7.70),('Coquetdale','actellus',6,38,4.03),
	('RoyalpTilsit','sedtristiqueintempussitamet',2,58,0.44),('Castigliano','sedsagittisnamconguerisussemper',14,15,5.57),
	('WhiteStilton','euismodscelerisdipiscingloremvitae',13,66,1.36),('Roule','pellentesqueultricesphasellusid',15,16,7.26),
	('WoodsideCabecou','consequatvariusintegeracleopellentesque',14,87,7.37),('Danbo','quisaugueluctustinciduntnulla',12,57,1.98),
	('BrebisduLavort','consequatmetussapienut',6,28,2.92),('SainteMaure','morbiaipsumintegeranibhin',9,97,4.39),
	('Button','aliquameratvolutpatincongueetiamjusto',5,94,6.83),('BaguetteLaonnaise','infeliseusapiencursusvestibulum',11,73,5.74),
	('CypressGroveChevre','habitasseplateadictumstetiam',5,62,2.92),('DryJack','convallisegeteleifend',12,63,1.75),
	('GrandVatel','convallisegeteleifend',8,68,9.54),('Tibet','augueasuscipitnullaelitacnulla',15,44,5.05),
	('Babybel','duivelnislduisacnibhfusce',4,93,3.88),('Gouda','maecenastristiqueestet',3,17,2.27),
	('Geitost','aliquamauguequamsollicit',13,2,3.61),('QuesoMajorero','adipiscispraesent',11,41,0.34),
	('Cabrales','aliquetmassaidlobortisconvallis',10,51,1.08),('BrusselaeKaas','nibhinlectus',4,90,0.72);

-- sample data for invoices --
INSERT INTO invoices (invoice_id, customer_id, date)
VALUES  
	(1,13,'2022-05-22'),(2,30,'2021-03-05'),(3,16,'2016-12-31'),(4,37,'2021-09-16'),
	(5,14,'2018-01-03'),(6,1,'2019-01-18'),(7,22,'2020-03-12'),(8,28,'2017-08-11'),
	(9,5,'2021-10-07'),(10,49,'2022-08-05'),(11,1,'2016-03-22'),(12,28,'2018-09-12'),
	(13,40,'2023-01-26'),(14,27,'2020-04-13'),(15,50,'2015-11-10'),(16,2,'2021-11-25'),
	(17,19,'2017-10-26'),(18,45,'2021-09-18'),(19,42,'2019-12-19'),(20,35,'2020-06-19'),
	(21,22,'2020-04-16'),(22,11,'2015-07-24'),(23,6,'2018-10-08'),(24,41,'2019-03-28'),
	(25,19,'2019-07-08'),(26,33,'2022-04-09'),(27,35,'2016-04-17'),(28,49,'2021-06-20'),
	(29,21,'2016-01-28'),(30,9,'2017-02-21'),(31,20,'2018-02-14'),(32,47,'2021-02-23'),
	(33,28,'2017-12-21'),(34,23,'2018-02-08'),(35,8,'2021-08-21'),(36,8,'2022-04-17'),
	(37,33,'2022-07-14'),(38,41,'2022-03-16'),(39,21,'2021-10-15'),(40,29,'2015-12-03'),
	(41,27,'2019-07-06'),(42,1,'2016-05-23'),(43,10,'2018-02-27'),(44,1,'2022-11-15'),
	(45,18,'2019-07-29'),(46,25,'2015-05-10'),(47,48,'2017-02-01'),(48,46,'2021-04-30'),
	(49,13,'2017-10-12'),(50,49,'2017-04-26'),(51,8,'2020-12-24'),(52,34,'2022-01-11'),
	(53,48,'2022-10-12'),(54,32,'2018-02-26'),(55,21,'2015-06-28'),(56,19,'2016-01-02'),
	(57,27,'2022-03-12'),(58,35,'2021-02-06'),(59,11,'2020-03-30'),(60,28,'2021-08-10'),
	(61,15,'2015-06-21'),(62,46,'2015-12-13'),(63,40,'2015-09-03'),(64,42,'2018-04-10'),
	(65,14,'2017-04-01'),(66,42,'2023-01-09'),(67,29,'2019-05-08'),(68,12,'2016-03-18'),
	(69,50,'2019-10-09'),(70,46,'2021-01-30'),(71,21,'2018-10-29'),(72,11,'2020-11-14'),
	(73,2,'2017-12-28'),(74,3,'2020-08-18'),(75,3,'2021-12-11'),(76,6,'2019-03-01'),
	(77,10,'2019-11-06'),(78,15,'2022-12-28'),(79,4,'2015-07-24'),(80,26,'2019-04-09'),
	(81,50,'2016-05-08'),(82,16,'2018-03-03'),(83,25,'2015-08-19'),(84,49,'2018-04-06'),
	(85,35,'2020-04-09'),(86,28,'2020-10-01'),(87,22,'2022-12-20'),(88,19,'2022-09-25'),
	(89,32,'2020-08-14'),(90,41,'2019-10-15'),(91,33,'2018-01-05'),(92,8,'2021-09-25'),
	(93,29,'2016-01-20'),(94,19,'2015-07-19'),(95,41,'2016-11-16'),(96,25,'2016-08-11'),
	(97,49,'2022-03-18'),(98,46,'2015-11-27'),(99,18,'2023-02-06'),(100,15,'2022-08-24');
    
-- sample data for invoice line item
insert into invoice_line_items(invoice_id, product_id, qty)
VALUES  (1,1,42),(1,2,23),(1,4,27),(2,2,7),(2,3,8),(2,4,1),(1,3,69),
		(2,1,16),(2,3,8),(2,4,1),(3,1,6),(1,4,27),(2,3,8),
        (2,4,1),(3,1,6),(3,2,4),(2,3,8),(2,4,1),(3,1,6),(3,2,4),(3,3,4),
        (2,3,8),(2,4,1),(3,1,6),(3,2,4),(3,3,4),(3,4,2),(2,3,8),(2,4,1),(3,1,6),(3,2,4),
        (3,3,4),(3,4,2),(4,1,12),(2,3,8),(2,4,1),(3,1,6),(3,2,4),(3,3,4),(3,4,2),(4,1,12),(4,2,30),(2,4,1),
        (3,1,6),(3,2,4),(3,3,4),(3,4,2),(4,1,12),(4,2,30),(4,3,7),(3,1,6),(3,2,4),(3,3,4),(3,4,2),(4,1,12),
        (4,2,30),(4,3,7),(4,4,5),(3,2,4),(3,3,4),(3,4,2),(4,1,12),(4,2,30),(4,3,7),(4,4,5),(79,76,7),(3,3,4),
        (3,4,2),(4,1,12),(4,2,30),(4,3,7),(4,4,5),(79,76,7),(73,26,9),(3,4,2),(4,1,12),(4,2,30),(4,3,7),(4,4,5),
        (79,76,7),(73,26,9),(16,50,2),(4,1,12),(4,2,30),(4,3,7),(4,4,5),(79,76,7),(73,26,9),(16,50,2),(56,99,10),
        (4,2,30),(4,3,7),(4,4,5),(79,76,7),(73,26,9),(16,50,2),(56,99,10),(80,61,3),(4,3,7),(4,4,5),(79,76,7),(73,26,9),
        (16,50,2),(56,99,10),(80,61,3),(40,58,4),(4,4,5),(79,76,7),(73,26,9),(16,50,2),(56,99,10),(80,61,3),(40,58,4),
        (17,73,7),(79,76,7),(73,26,9),(16,50,2),(56,99,10),(80,61,3),(40,58,4),(17,73,7),(34,27,1),(73,26,9),(16,50,2),
        (56,99,10),(80,61,3),(40,58,4),(17,73,7),(34,27,1),(70,69,7),(16,50,2),(56,99,10),(80,61,3),(40,58,4),(17,73,7),
        (34,27,1),(70,69,7),(58,77,8),(56,99,10),(80,61,3),(40,58,4),(17,73,7),(34,27,1),(70,69,7),(58,77,8),(58,82,12),
        (80,61,3),(40,58,4),(17,73,7),(34,27,1),(70,69,7),(58,77,8),(58,82,12),(20,13,6),(40,58,4),(17,73,7),(34,27,1),
        (70,69,7),(58,77,8),(58,82,12),(20,13,6),(37,83,10),(17,73,7),(34,27,1),(70,69,7),(58,77,8),(58,82,12),(20,13,6),
        (37,83,10),(24,67,10),(34,27,1),(70,69,7),(58,77,8),(58,82,12),(20,13,6),(37,83,10),(24,67,10),(85,58,6),(70,69,7),
        (58,77,8),(58,82,12),(20,13,6),(37,83,10),(24,67,10),(85,58,6),(20,33,13),(58,77,8),(58,82,12),(20,13,6),(37,83,10),
        (24,67,10),(85,58,6),(20,33,13),(22,85,4),(58,82,12),(20,13,6),(37,83,10),(24,67,10),(85,58,6),(20,33,13),(22,85,4),
        (2,12,7),(20,13,6),(37,83,10),(24,67,10),(85,58,6),(20,33,13),(22,85,4),(2,12,7),(95,88,3),(37,83,10),(24,67,10),
        (85,58,6),(20,33,13),(22,85,4),(2,12,7),(95,88,3),(19,68,2),(24,67,10),(85,58,6),(20,33,13),(22,85,4),(2,12,7),
        (95,88,3),(19,68,2),(26,49,4),(85,58,6),(20,33,13),(22,85,4),(2,12,7),(95,88,3),(19,68,2),(26,49,4),(45,39,8),
        (20,33,13),(22,85,4),(2,12,7),(95,88,3),(19,68,2),(26,49,4),(45,39,8),(32,36,8),(22,85,4),(2,12,7),(95,88,3),
        (19,68,2),(26,49,4),(45,39,8),(32,36,8),(13,72,9),(2,12,7),(95,88,3),(19,68,2),(26,49,4),(45,39,8),(32,36,8),
        (13,72,9),(31,5,11),(95,88,3),(19,68,2),(26,49,4),(45,39,8),(32,36,8),(13,72,9),(31,5,11),(28,76,15),(19,68,2),
        (26,49,4),(45,39,8),(32,36,8),(13,72,9),(31,5,11),(28,76,15),(44,79,13),(26,49,4),(45,39,8),(32,36,8),(13,72,9),
        (31,5,11),(28,76,15),(44,79,13),(25,99,12),(45,39,8),(32,36,8),(13,72,9),(31,5,11),(28,76,15),(44,79,13),(25,99,12),
        (92,80,3),(32,36,8),(13,72,9),(31,5,11),(28,76,15),(44,79,13),(25,99,12),(92,80,3),(60,60,5),(13,72,9),(31,5,11),
        (28,76,15),(44,79,13),(25,99,12),(92,80,3),(60,60,5),(96,62,12),(31,5,11),(28,76,15),(44,79,13),(25,99,12),(92,80,3),
        (60,60,5),(96,62,12),(38,34,8),(28,76,15),(44,79,13),(25,99,12),(92,80,3),(60,60,5),(96,62,12),(38,34,8),(10,54,6),
        (44,79,13),(25,99,12),(92,80,3),(60,60,5),(96,62,12),(38,34,8),(10,54,6),(38,50,11),(25,99,12),(92,80,3),(60,60,5),
        (96,62,12),(38,34,8),(10,54,6),(38,50,11),(7,11,5),(92,80,3),(60,60,5),(96,62,12),(38,34,8),(10,54,6),(38,50,11),
        (7,11,5),(39,27,9),(60,60,5),(96,62,12),(38,34,8),(10,54,6),(38,50,11),(7,11,5),(39,27,9),(56,70,12),(96,62,12),
        (38,34,8),(10,54,6),(38,50,11),(7,11,5),(39,27,9),(56,70,12),(79,20,1);