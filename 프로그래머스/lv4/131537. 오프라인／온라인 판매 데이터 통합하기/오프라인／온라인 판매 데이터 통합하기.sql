-- 오프라인/온라인 판매 데이터 통합하기
SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE,PRODUCT_ID,USER_ID,SALES_AMOUNT
FROM
(
SELECT SALES_DATE,PRODUCT_ID,USER_ID,SALES_AMOUNT
FROM ONLINE_SALE
UNION
SELECT SALES_DATE,PRODUCT_ID,NULL,SALES_AMOUNT
FROM OFFLINE_SALE 
) AS T
WHERE 1=1
AND MONTH(T.SALES_DATE)=3
AND YEAR(T.SALES_DATE)=2022
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID
