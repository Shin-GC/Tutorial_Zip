#SHOW DATABASES; 모든 데이터베이스 보여주기
#USE database_name; 사용할 데이터 베이스 지정
#USE world;
#SHOW TABLES; 데이터 베이스 의 테이블 이름 보기
#SHOW TABLE STATUS; 데이터 베이스의 테이블 정보 조회

#DESCRIBE city 테이블에 무슨 열[칼럼]이 있는지 확인 [DESC]
#DESC country;
#SELECT * FROM city; 모든 city 열 조회
#SELECT Name FROM city; #모든 city열의 이름값만 출력

#WHERE = 조회하는 결과에 특정한 조건으로 원하는 데이터만 보고 싶을 때 사용

/* 도시 중 이름이 New York 인 조건을 만족하는 값의 열 모두 출력
SELECT * 
FROM city
WHERE Name = 'New York';
한국에 있는 모든 도시 출력
SELECT * 
FROM city
WHERE CountryCode = 'KOR';

---
한국 도시중 인구가 백만 이상 3백만 이하만 나오게 하기
SELECT *
FROM city
WHERE countryCode = 'KOR'
AND Population BETWEEN 1000000 AND 3000000;

---
원하는 걸 여러개 묶을때 IN 사용
SELECT *
FROM city
WHERE Name IN('Seoul','New York', 'Tokyo');

---
문자열의 내용을 검색하기 위해 LIKE 연산자 사용 [ 문자 뒤에 %- 무엇이든 허용] [ 한글자와 매치하기 위해서는 '_' 사용]

SELECT *
FROM city
WHERE CountryCode LIKE 'K%' OR 'KO_'

---
서브 쿼리 :SubQuery 쿼리 문 안에 다른 쿼리 문이 들어있는 것으로 서브 쿼리 결과가 둘 이상이 되면 에러가 발생한다.
SELECT *
FROM city
WHERE CountryCode = ( SELECT CountryCode FROM city WHERE Name = 'Seoul');

---
ANY 를 사용하면 하나라도 만족하면 이란 뜻으로 SOME과 동일한 의미로 사용한다
SELECT *
FROM city
WHERE Population > ANY (SELECT Population
						FROM city 
						WHERE District = 'New York');
---
ALL = 서브쿼리의 여러 개의 결과를 모두 만족 시켜야한다.

SELECT *
FROM city
WHERE Population > ALL (SELECT Population
						FROM city 
						WHERE District = 'New York');
---
ORDER BY : 결과가 출력되는 순서를 조절하는 구문 [ 기본적으로 오름차 순 으로 정렬 ]
열 이름 뒤에 DESC 를 적어주면 내림차순으로 정렬 가능 [오름차는 ASC 지만 default 므로 생략가능]

SELECT *
FROM city
ORDER BY Population DESC;

또한 ORDER BY는 혼합해서 사용이 가능하다.
SELECT *
FROM city
ORDER BY Population DESC, ID;

---
인구 수로 내림 차 순 하여 한국에 있는 도시 나열
SELECT *
FROM city
WHERE CountryCode = 'KOR'
ORDER BY Population DESC;
---
국가 면적 크기로 내림차순 정렬
SELECT *
FROM country
ORDER BY SurfaceArea DESC;

DISTINCT: 중복 제거
SELECT DISTINCT CountryCode
FROM city;

---

LIMIT : 출력의 개수를 제한
[상위의 N개만 출력하는 LIMIT N 구문]
서버의 처리량을 많이 사용해 서버의 전반적인 성능을 나쁘게 하는 악성 쿼리문을 개선할 때 사용

SELECT *
FROM city
ORDER BY Population DESC
LIMIT 10

---
GROUP BY : 글부으로 묶어 주는 역활
[ 집계함수 : Aggregate Function 을 함께 사용]
AVG:(): 평균
MIN(): 최소
MAX(): 최대
COUNT(): 행의 개수
COUNT(DISTINCT): 중복 제외된 행의 개수
STDEV(): 표준 편차
VARIANCE(): 분산 
효율적인 데이터 그룹화 : Grouping
읽기 좋게 하기 위해 별칭 : Alias 사용 [AS : 별칭]

SELECT CountryCode, MIN(Population) AS 'Average'
FROM city
GROUP BY CountryCode
LIMIT 20

SELECT COUNT(*) #도시의 총 갯수
FROM city;

SELECT AVG(Population) #인구의 평균
FROM city;

----

HAVING : 조건 제한
집계함수에 대해서 조건을 제한하는 편리한 개념
!!HAVING절은 반드시 GROUP BY 절 다음에 나와야 한다.!!
[WHERE절 : SELECT ~ FROM절에서 발췌된 데이터에 대한 제한조건을 부여하여 필요한 데이터만을 조회할 때 사용하는 조건절
[-HAVING절 : 그룹함수를 사용해 GROUP BY절을 사용할 때 그룹들에 대한 제한 조건이 필요하여 사용하는, 그룹에 대한 조건절

SELECT CountryCode, MAX(Population) AS 'MAX'
FROM city
GROUP BY CountryCode
HAVING MAX > 10000
ORDER BY MAX ASC

----

ROLLUP: 총합 또는 중간합계가 필요한 경우에 사용한다.
[ GROUP BY 절과 함께 WITH ROLLUP문을 사용!]

SELECT CountryCode, Name, SUM(Population)
FROM city
GROUP BY CountryCode, Name With ROLLUP

---

JOIN : 데이터베이스 내의 여러 테이블에서 가져온 레코드를 조합하여 하나의 테이블이나 결과 집합으로 표현한다.

SELECT DISTINCT *
FROM country
JOIN city ON city.CountryCode = country.Code
JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode
WHERE city.CountryCode = 'KOR'
ORDER BY ID ASC
LIMIT 10

----
length ('문자열') : 문자열 길이를 반환해주는 함수
SELECT length('1232131');
----
CONCAT('문자열','문자열',...) : 전달받은 문자열을 모두 결합하여 하나의 문자열로 반환 해주는 함수
! 전달받은 문자열 중 하나라도 NULL이 존재한다면 NULL을 반환 !
SELECT concat('감자',' 튀김',' 햄버거')
---
LOCATE('찾을 문자열','문자열','찾을 위치 default = 1') : 문자열 내에서 찾는 문자열이 처음으로 나타나는 위치를 찾아서 해당 위치를 반환
! 찾는 문자열이 문자열 내에 존재하지 않는다면 0을 반환 !
!! MySQL에서는 문자열의 시작 인덱스를 1부터 계산 !!
SELECT locate('다','가나다라마바사다')
---
LEFT('문자열','문자 개수'): 문자열의 왼족에서 지정한 개수만큼 문자를 반환
RIGHT('문자열','문자 개수): 문자열의 오른쪽에서 지정한 개수만큼 문자를 반환
SELECT LEFT('가나다라마바사아자차카',3);
SELECT RIGHT('가나다라마바사아자차카',3);
---
LOWER() : 문자열의 문자를 모두 소문자로 변경
UPPER() : 문자열의 문자를 모두 대문자로 변경
SELECT lower('AbCd');
SELECT UPPER('AbCd');
---
REPLACE('문자열','특정 문자열','대체 문자열') : 문자열에서 특정 문자열을 대체 문자열로 교체
SELECT replace('가나다라마바사','가나다','abc')
---
TRIM() : 문자열의 앞이나 뒤, 또는 양쪽 모두에 있는 특정 문자를 제거하기
사용할수있는 지정자
-BOTH:전달받은 문자열의 양끝에 존재하는 특정 문자를 제거(기본설정)
-LEADING: 전달받은 문자열 앞에 존재하는 특정문자를 제거
-TRAILING: 전달받은 문자열 뒤에 존재하는 특정 문자를 제거
SELECT TRIM('a' FROM 'a감자튀김a'),TRIM(LEADING 'a' FROM 'a감자튀김a'),TRIM(TRAILING 'a' FROM 'a감자튀김a');
---
FLOOR() : 내림
CEIL() : 올림
ROUND() : 반올림
SELECT FLOOR(10.6),CEIL(10.1),ROUND(10.6)
---
FORMAT('숫자타입데이터','소수점 자릿수')
숫자 타입의 데이터를 세 자리마다 쉼표를 사용하는 '#,###,###.##'형식으로 변환
! 반환되는 데이터 형식은 문자열 타입!
SELECT FORMAT('110000',0);
---
SQRT() : 양의 제곱근
POW() : 첫번째 인수로는 밑수를 전달하고. 두번째 인수로는 지수를 전달하여 거듭제곱 계산
EXP() : 인수로 지수를 전달받아, e의 거듭 제곱을 계산
LOG() : 자연로그 값을 계산
SELECT SQRT(4), POW(2,3), EXP(10), LOG(10);
#SELECT SIN(1/2), COS(1/2), TAN(PI()/2)
----
ABS():절대값을 반환
RAND(): 0.0보다 크거나 같고 1.0보다 작은 하나의 실수를 무작위로 생성
#RAND랜덤함수를 그냥 쓰면 안되고 실수값을 줘야되는데 range를 주기 힘드니 round 로 반올림 해준다.
SELECT ABS(-3), RAND(), ROUND(RAND()*100,1); 
----
NOW(): 현재 날짜와 시간을 반환, 반환되는 값은 'YYYY-MM-DD-HH:MM:SS' 또는 'YYYYMMDDHHMMSS'
CURDATE(): 현재 날짜를 반환, 이때 반환되는 값은 'YYYY-MM-DD' 또는 붙여서
CURTIME(): 현재 시각을 반환, 이때 반환되는 값은 'HH:MM:SS'또는 HHMMSS 형태
SELECT NOW(),CURDATE(),CURTIME()
----
DATE(): 날짜
MONTH(): 월
DAY(): 일
HOUR(): 시
MINUTE(): 분
SECOND(): 초

SELECT NOW(),
DATE(NOW()),
MONTH(NOW()),
DAY(NOW()),
HOUR(NOW()),
MINUTE(NOW()),
SECOND(NOW())
---

MONTHNAME() :현재 시간의 월 이름
DAYNAME(): 요일 이름

SELECT monthname(NOW()) as 'Month',DAYNAME(NOW()) as 'Day'
---

DAYOFWEEK(): 일자가 해당주에서 몇번째 날인지, 1부터 7사이의 값을 반환 (일요일 =1, 토요일 =7)
DAYOFMONTH(): 일자가 해당월에서 몇번째 날인지, 0-31사이의 값 반환
DAYOFYEAR(): 일자가 해당 연도에서 몇번째 날인지, 1-366 사이의 값 반환
SELECT dayofweek(now()) as 'DayNumber', dayofmonth(now()) as 'Month Number',dayofyear(now()) as 'year of day num'
---

DATE_FORMAT() : 전달받은 형식에 맞춰 날짜와 시간 정보를 문자열로 반환
%D = 일수
%y = 년수 뒤 2021 = 21
%a = 일
%d = 일수
%m = 월
%n = 
%j = 1월 1일부터 경과한 일수
SELECT 
DATE_FORMAT(NOW(), '%D %y %a %m %d %j') 
---
원래 있던 테이블 복사하기
CREATE TABLE copy_city as select * from city;
SELECT *
from copy_city

---
데이터 베이스 생성
CREATE DATABASE shin;
---
테이블 생성
create table first (
	id INT NOT NULL PRIMARY KEY,
    col1 INT NULL,
    col2 FLOAT NULL,
    col3 varchar(10) NULL
);
---
ALTER TABLE ADD : ADD 문을 함께 사용하면 테이블에 칼럼을 추가할 수 있다.

ALTER TABLE first
ADD col4 INT NULL;

MODIFY: ALTER TABLE문과 함께 MODIFY 문을 사용하면 , 테이블의 칼럼 타입을 변경가능하다.
ALTER TABLE first
modify col4 varchar(20) NULL;

DROP: ALTER TABLE문과 함께 DROP문을 사용하면, 테이블의 칼럼을 제거할 수 있다.

alter table first
drop col4;

-----
인덱스 : Index
테이블에서 원하는 데이터를 빠르게 찾기위해 사용한다.
검색과 질의를 할 때 테이블 전체를 읽지 않기 때문에 빠르다.

설정된 컬럼 값을 포함한 데이터의 삽입, 삭제, 수정 작업이 원본 테이블에서 이루어질 경우, 인덱스도 함께 수정되어야 한다.
인덱스가 있는 테이블은 처리 속도가 느려질 수 있으므로 수정보다는 검색이 자주 사용되는 테이블에서 사용하는 것이 좋다.

인덱스 생성
create index col1idx
on first (col1);

중복 값을 허용하지 않는 인덱스 생성
create unique index col2idx
on first (col2);

FULLTEXT INDEX : 일반적인 인덱스와는 달리 매우 빠르게 테이블의 모든 텍스트 컬럼을 검색 [문자열 검색용]
alter table first
add fulltext col3idx(col3);

인덱스 정보 보기
show index from first;

인덱스 삭제(ALTER)

1. ALTER문을 이용해 테이블에 추가된 인덱스 삭제
alter table first
drop index col3idx;

2. DROP 문을 이용하여 삭제 [ 내부적으로 ALTER 문으로 자동 변환되어 명시된 이름의 인덱스를 삭제
drop index col2idx on first;
======

뷰: VIEW
데이터 베이스에 존재하는 일종의 가상 테이블
실제 테이블처럼 행과 열을 가지고 있지만, 실제로 데이터를 저장하지는 않음.

MySQL에서 뷰는 다른 테이블이나 다른 뷰에 저장되어 있는 데이터를 보여주는 역활만 수행
뷰를 사용하면 여러 테이블이나 뷰를 하나의 테이블 처럼 볼 수 있음

장점
1. 특정 사용자에게 테이블 전체가 아닌 필요한 컬럼만 보여줄 수 있음.
2. 복잡한 쿼리를 단순화 해서 사용이 가능하다.
3. 쿼리 재사용이 가능하다.

단점
1. 한번 정의된 뷰는 변경할 수 없다.
2. 삽입, 삭제, 갱신 작업에 많은 제한 사항을 가진다.
3. 자신만의 인덱스를 가질 수 없다.
=======
CREATE VIEW :VIEW 생성
create view testview as
select col1,col2
from first;

-----
ALTER VIEW : 뷰를 수정
ALTER VIEW testview as
select col1,col2,col3
from first;
----
DROP VIEW : 뷰 삭제

USE world;
alter view Koreanview as
SELECT DISTINCT city.Name,country.SurfaceArea, city.Population,Countrylanguage.Language
FROM country
JOIN city ON city.CountryCode = country.Code
JOIN countrylanguage ON city.CountryCode = Countrylanguage.CountryCode
WHERE city.CountryCode = 'KOR'
ORDER BY ID ASC;

select *
from Koreanview;
=====
INSERT
테이블 이름 다음에 나오는 열 생략 가능
생략할 경우 VALUE 다음에 나오는 값들의 순서 및 개수가 테이블이 정의된 열 순서 및 개수와 동일해야 한다.
insert into first
value(1,123,1.1,'first');
---
INSERT INTO SELECT
test 테이블에 있는 내용을 test2 테이블에 삽입 [복사]

create table twice(
id INT NOT NULL PRIMARY KEY,
    col1 INT NULL,
    col2 FLOAT NULL,
    col3 varchar(10) NULL
);
insert into twice select * from first;
select * from twice;

---
UPDATE : 기존에 입력되어 있는 값을 변경하는 구문
WHERE 절 생략 가능하나 테이블의 전체 행의 내용이 변경
update first
set id = 1 ,col1 = 1, col2 = 2 , col3 = 'update'
where id = 1;

----
DELETE : 행 단위로 데이터를 삭제하는 구문
DELETE FROM 테이블 이름 WHERE 조건;
! 데이터는 지워지지만 테이블 용량은 줄어들지 않는다! [ 복구가 가능하기 때문 ]
원하는 데이터만 지울 수 있다.
삭제 후 잘못 삭제한 것을 되돌릴 수 있다.

delete from first
where id = 1;
select *
from first;
-----
TRUNCATE : 용량도 줄어들고 , 인덱스 등 모두 삭제
테이블은 삭제하지 않고, 데이터만 사ㅛㄱ제
한꺼번에 다 지워야 한다.
!!삭제 후 절대 되돌릴 수 없다!!
------
DROP TABLE : 테이블 전체를 삭제, 공간, 객체를 삭제
DROP TABLE first;
!!삭제 후 되돌릴 수 없다!!
-----
DROP DATABASE : 해당 데이터 베이스 삭제
DROP DATABASE shin;
*/
# 핸드폭 연락처 주소록 만들기!
/*
create database my;
use my;
create table contact(
id INT NOT NULL PRIMARY KEY,
people varchar(40) NULL,
phone varchar(15) NULL
);

insert into contact
value(1,'shin','010-****-****');

update contact
set people = 'Shin',addday=now()
where id = 1;

insert into contact
value(2,'KMJ','010-????-????');

update contact
set addday=now()
where id = 2;

ALTER TABLE contact
ADD addday varchar(40) NULL;

select * from contact;
desc contact;
*/


















