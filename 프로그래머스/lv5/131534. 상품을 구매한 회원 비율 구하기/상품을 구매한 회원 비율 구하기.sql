SELECT
    YEAR(ONLINE_SALE.SALES_DATE) AS YEAR,
    MONTH(ONLINE_SALE.SALES_DATE) AS MONTH,
    count(DISTINCT ONLINE_SALE.USER_ID) AS PURCHASED_USERS,
    -- 이용자 정보의 수(전체 이용자 수)를 결제 회원의 수로 나눈 것 (전체 이용자 대비 결제 회원의 비율)
    round (count(DISTINCT ONLINE_SALE.USER_ID) / 
           -- 서브 쿼리를 이용하여 그룹화 되지 않은 테이블의 2021년 총 가입자수를 가져온다
           (SELECT count(USER_ID) FROM USER_INFO WHERE YEAR(USER_INFO.JOINED) = 2021)
           -- 2번째 자리에서 반올림
           ,1) AS PURCHASED_RATIO

-- USER_ID 컬럼을 기준으로 이용자 정보와 결제 정보 테이블을 INNER JOIN
FROM ONLINE_SALE JOIN USER_INFO
ON ONLINE_SALE.USER_ID = USER_INFO.USER_ID

-- 가입일이 2021년인 회원만 JOIN
WHERE YEAR(USER_INFO.JOINED) = 2021

# -- 각 (결제) 월별로 집계 (연도를 따로 집계할 필요 없음)
GROUP BY YEAR,MONTH

-- 연도와 월별로 순차 정렬
ORDER BY YEAR, MONTH ASC