use BikeStores;

select * from sales.customers;

select * from sales.staffs;

--clause
--------------
--where
--	like
--	between
--	in
--	and
--	or
--having
--groupby

--SQL Case  -> IF else

--SQL Joins
--	Inner Join, Left Join, Right Join, Outer Join, Self Join

--SubQuery

--CTE (Common Table Expression)  -> Temporary Tables

--Window Functions
--	Row_Number, Rank, Dense_Rank, NTile, Lead, Lag


-- Where
select * from sales.customers as sc
where first_name = 'Debra';

select * from sales.customers as sc
where state='NY' and zip_code=14127;

select * from sales.customers as sc
where state='NY' or state='CA';

between (range) and in (same column values)

--Like (pattern matching)
--wildcards
-- %
-- _

Like

Concat and concat operator

date
























