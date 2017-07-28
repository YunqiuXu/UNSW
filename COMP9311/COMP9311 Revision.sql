-- Revision in Lab & Assignment
Lab 1 Set up PostgreSQL server -- PASSED
Lab 2 Schema definition; data constraints --PASSED
Lab 3 Assignment 1 --PASSED
Lab 4 SQL queries, views, aggregates --PASSED
Lab 5 User-defined functions and aggregates; PLpgSQL --Still has some problems
    -- Q6
    -- Q7
    -- Q8
Lab 6 Updates and triggers




Lab 7 Assignment 2 --PASSED
Ex 1
Ex 2
Assignment 3






-- Something new in revision

##########
1. BASIC
##########
-- Basic : create a new table
CREATE TABLE SB(
    att1    domain    check(att1 ... ),
    att2    domain    references  SB1(attx),
    att3    domain    not null,
    "att4"  domain    unique,
    foreign key (xxx) references SB2(attxx),
    primary key (att1)
);

CREATE TABLE tablename(
    att1 dom1 constraint1,
    att2 dom2 constraint2,
    ...
    primary key(att),
    foreign key() references OtherTable(att),
    check tablelevel constraints
);


-- Basic : table-level constraint
CONSTRAINT fuckyou CHECK(ass>hole)
CONSTRAINT asshole CHECK(bitch> (select max(bitch) from whores))
not null
unique(att1,att2)

-- Basic : Alter table
-- add&drop column
alter table fuck ADD COLUMN name domain constraint;
alter table fuck DROP COLUMN name CASCADE; --cascade: drop related constraint
ALTER TABLE fuck ALTER COLUMN name SET DEFAULT 'fuckyou';
ALTER TABLE fcuk ALTER COLUMN name DROP DEFAULT;
ALTER TABLE fuck ALTER COLUMN name DROP NOT NULL; -- drop null
-- alter constraint
alter table fuck ADD CHECK(...);
alter table fuck ADD CONSTRAINT ...;
ALTER TABLE fuck ADD FOREIGN KEY () REFERENCES ...;
ALTER TABLE fuck DROP CONSTRAINT name;
-- alter type : based on alter column
ALTER COLUMN name TYPE newtype
-- Rename the column
ALTER TABLE fuck RENAME COLUMN fuckme TO fuckyou;
-- Rename the table
ALTER TABLE fuck RENAME TO fuckhahaha;

-- Basic : drop table
drop table tablename;


-- Basic : create a new domain
CREATE DOMAIN SBType AS
    varchar(10) check( value ~ 'xxx');
create domain UnswGradesDomain as
    char(2) check (value in ('FL','PS','CR','DN','HD'))


-- Basic : create a new type
CREATE TYPE fuck as (sb integer,asshole text);
CREATE TYPE fucks AS ENUM('a','b','c')
-- only type can use enum!!

-- Add new enumerate
ALTER TYPE fuck 
ADD VALUE 'asshole' after/before 'a';
-- Note that you can not delete enum


-- Basic : data type
text,char(n),varchar(n)
Integer,Numeric(a,b),real,SERIAL
Date,Time,Timestamp,interval

-- Basic : constants
select 'xyq'
'sb'; --euqal to select 'xyqsb';

-- Basic : type casting
expression::newtype 
select 2::numeric/4::numeric;
select array[1,2,22.7]::integer[]; -- {1,2,23}
select cast('xxx' as type); --another method
select now()::Timestamp; -- change now() to timestamp

-- Basic : escape
E'xxx \escape ';
select E'select xyq\'s head'; -- xyq's head
select 'select xyq\'s head'; --error

-- Basic : priority
select 5!-6; --error
select (5!)-6; --114

---------------------------------------
##########
2. SQL Syntax
##########

-- SQL Syntax : dealing with Null
select 3=null; -- return null
select 3 <> null; --return null
select 3 is null; --return 'f', boolean

-- SQL Syntax : coalesce
-- return the first not-null para
select coalesce(null,null,null,'fuck',null,'you'); --'fuck'


-- SQL Syntax : nullif
nullif(val1,val2) --if val1=val2, return null ,else return val1


-- SQL Syntax : dealing with different conditions
CASE 
WHEN condition1 THEN operation1
WHEN condition2 THEN operation2
...
ELSE operationX -- this is optional
END

---------------------------------------
##########
3. General functions
##########
-- numeric function
power(a,b)
round(a,b)
sqrt()/mod(a,b)/floor()/ceiling()

-- string function
string1 || string2 -- concat: 'a' || 'b' --> 'ab'
string1 || non-string || string2 -- 'a'||'b'||10 --> null
char_length('asshole') -- 7
lower()/upper()
overlay('Txxxxas' placing 'hom' from 2 for 4) -- replace 'xxxx'(start from 2, length 4) with 'hom'
position('sb' in 'fuckyousbasshole') -- position of 'sb'

substring('asshole',4,2) -- start from 'h', length=2
substring('asshole' from 4 for 2) -- equal to above
trim(leading|trailing|both 'x' from 'xxsdfsdfdxxx') --delete given char(default both space)
ltrim()/rtrim()
repeat('sb',3) -- 'sbsbsb'

-- format function
to_char(125, '999')
to_date('05 Dec 2000', 'DD Mon YYYY')
to_number('12,454.8-', '99G999D9S')

---------------------------------------
##########
4. Pattern matching
##########

-- regexp function
regexp_matches(text,pattern)
regexp_replace(text,pattern,replaceString) --replace pattern with replaceString
substring(text from pattern)

-- SQL Syntax  : Like ReExp
like '%sb%'
like '_i%' --i is the second letter
like 'fuck' --equal to 'fuck'

-- SQL Syntax : ~ ReExp
~ '^sb$' -- case intensive ~*
~ '^.i' -- i is the second letter
~ '.*o.*o.*' -- contain 2 'o'
~ 'fuck' -- contains 'fuck'

{m,n} -- [m,n]
{m} -- m
{m,} -- >=m

select 'abc' ~ 'abc'; -- t
select 'abc' like '%bc%'; --t
select 'babccccc' ~'abc'; --t
select 'babccccc' like'abc'; --f
select 'abc' ~ '(b|c)'; --t
select 'abc' ~ '^(b|c)'; --f

---------------------------------------
##########
5. Data operation
##########

-- Data operation:
insert into table values (...);
insert into table(att1,att2) values(...);
update table set ... where ...;
delete * from table where ...;
delete from table;--drop all tuples

---------------------------------------
##########
6. Query
##########

-- Query : basic keywords
SELECT
FROM
JOIN
ON
GROUP BY
HAVING
ORDER BY
LIMIT
OFFSET

-- Query : view
create or replace view viewName as ... ;

-- Query : combination
Query1 UNION Query2;
Query1 INTERSECT Query2;
Query1 EXCEPT Query2;

-- Query : With --> similar to view
WITH VIEWNAME1 AS(),
VIEWNAME2 AS()
SELECT ... FROM ... 

-- Query : recursion
WITH RECURSIVE recursiveName(para1,para2,...) AS
(
    BASE CASE
    UNION
    RECURSIVE CASE
)
SELECT ... FROM recursiveName ...;

-- Query : subquery
SELECT col1
FROM tab1
WHERE EXISTS (SELECT 1 FROM tab2 WHERE col2 = tab1.col2);
expression IN (subquery);
expression NOT IN (subquery);

-- COMP 9311 till lec 4
-- NEXT: lec 5-7  && ass 2 && lab 5-7 tomorrow 21:00-24:00

-- Query : windows function
GROUPBY ...
SELECT AVG(...) OVER(PARTITION BY ...) FROM ...;

---------------------------------------
##########
7. functions
##########

-- sql function
CREATE OR REPLACE FUNCTION fuck(varName text)
RETURNS integer 
AS $$
SELECT QUERY 
$$ language sql;

-- return types
create type typename as (ass1 type, ass2 type);
create or replace function fuck(fucking integer)
    returns setof typename
    as $$
    ...
    $$ language sql;

-- plpgsql
create function xxx(type1, type2)
returns type3
as $$
declare
    var1 type;
    var2 type;
begin
    function body;
end;
$$ language plpgsql;

-- plpgsql assignment
user_id := 20;
fuck := ass* hole;
bitch := select ...;
SELECT * INTO your_var FROM table ...;
-- plpgsql condition
IF (...) THEN 
    ...;
ELSIF (...) THEN
    ...;
ELSE
    raise exception 'fuck you';
END IF;
-- plpgsql loop
FOR ... IN ...
LOOP 
    ...;
END LOOP;

WHILE (...) LOOP
    ...
END LOOP;

-- Aggregate function
create aggregate aggName(int)(
    stype = int, -- type of intermediate
    sfunc = ...,
    initcond = 0, -- init value, default null
    finalfunc= ..., --final function, default sfunc
);
create aggregate concat(text)(
    stype = text,
    sfunc = addNext, -- a function created by myself
    initcond='',
    finalfunc=finalText -- a fucntion create by myself
);


-- Assertions
create assertion AssertionName check(
    not exists(select query)
);
-- if the assertion can not be satisfied, raise error

---------------------------------------
##########
8. triggers
##########

create or replace function triggerFunc(...)
    returns trigger as
    $$
    declare
        ...;
    begin
        ...
        return new;
    end;
    $$ language plpgsql;

create trigger triggerName before insertion on tableName 
    for each row execute procedure triggerFunc(...);

TG_OP='INSERT' -- check the operation

--example
CREATE or Replace FUNCTION func_ug_updateTime() RETURNS trigger AS $func_ug_updateTime$  
    BEGIN  
        If (TG_OP = 'UPDATE') THEN  
            If NEW.uptime = OLD.uptime Then  
                return null;  
            END IF;  
        END IF;  
        update ug set uptime = NOW() where uid = NEW.uid and gid = NEW.gid;  
        return null;  
    END;  
$func_ug_updateTime$ LANGUAGE plpgsql;  
CREATE TRIGGER t_ug_updateTime AFTER INSERT OR UPDATE ON ug  
    FOR EACH ROW EXECUTE PROCEDURE func_ug_updateTime();  

-----------------------------------------------------------
///////////////////////////////////////////////////////////

##########
9. Normalization
##########
-- Dependency
-- 1NF,2NF,3NF,BCNF
https://zhuanlan.zhihu.com/p/20028672
-- BCNF Decomposition
-- 3NF Decomposition
https://www.zhihu.com/question/21235096

Note that their answers are wrong
The answer should be {b->d，dg->c，b->e，ag->b}

In our labs exercise, BGH->F should be elimated in the precess of minimum dependency set,
but our final goal should be 3nf decompisition,
so we need to add BGH ar last

---------------------------------------
##########
9. realtional algebra
##########



-- plpg example
create type sb as (sb integer);
CREATE OR REPLACE FUNCTION sbloop(init integer)
returns integer
as $$
declare 
    n integer;
begin
    n:=0;
    while(n<init)
    loop
        n:=n+1;
    end loop;
    return n;
end;
$$ language plpgsql;


---------------------------------------
-- Exam: 2006
