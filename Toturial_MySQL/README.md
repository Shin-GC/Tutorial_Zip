# Toturial_MySQL
![img](https://user-images.githubusercontent.com/58453569/108453677-4c9a7900-72ae-11eb-95ea-c1dbd9a02823.jpg)

DML : Data Manipulation Language
-------------
> * 데이터 조작 언어
> * DML 구문의 사용 대상은 테이블이다.
> * 즉 DML 구문 사용 이전에 테이블이 정의되어 있어야 한다.
> * SELECT , INSERT , UPDATE , DELETE 가 DML에 속한다.

DDL : Data Definition Language
-------------
> * 데이터 정의 언어
> * DataBase, Table, View, Index 등의 DataBase 개체를 생성/삭제/변경 하는 역활
> * CREAT, DROP, ALTER 등의 구문이 속함
> * DDL은 Transaction 을 발생시키지 않는다.
> * ROLLBACK 이나 COMMIT 사용이 불가하다.
> * DDL문은 실행 즉시 MySQL에 적용된다.

DCL : Data Control Language
-
> * 사용자에게 권한을 부여하거나 빼앗을 때 주로 사용하는 구문이다.
> * GRANT , REVOKE , DENY 가 이에 속한다.

TCL : Transaction Control Language
-
> * DML에 의해 조작된 결과를 작업단위 (Transaction) 별로 제어하는 언어
> * COMMIT , ROLLBACK 등이 이에 속한다!

```
트랜잭션 [ transaction ] : 하나의 작업을 수행하기 위해 필요한 데이터베이스의 연산들을 모아놓은 것으로,
                          데이터 베이스에서 논리적인 작업의 단위를 말한다.
                           
                          장애가 발생했을때 데이터를 복구하는 작업의 단위이기도 하다.
                           
                          일반적으로 데이터 베이스의 연산은 SQL문으로 표현되므로, 트랜잭션은
                          작업의 수행에 필요한 SQL문들의 모임으로 이해하면 쉽다.
```
