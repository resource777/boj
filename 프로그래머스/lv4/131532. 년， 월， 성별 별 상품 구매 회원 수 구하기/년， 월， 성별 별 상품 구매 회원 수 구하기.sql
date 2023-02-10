-- 년, 월, 성별 별 상품 구매 회원 수 구하기
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT U.USER_ID) USERS
FROM USER_INFO U JOIN ONLINE_SALE O ON U.USER_ID=O.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY YEAR,MONTH,GENDER
ORDER BY YEAR,MONTH,GENDER