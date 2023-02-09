-- 카테고리 별 도서 판매량 집계하기
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM (
    SELECT B.BOOK_ID, B.CATEGORY,BS.SALES
    FROM BOOK B, BOOK_SALES BS
    WHERE B.BOOK_ID=BS.BOOK_ID
    AND DATE_FORMAT(BS.SALES_DATE,'%Y-%m')='2022-01'
) T
GROUP BY T.CATEGORY
ORDER BY T.CATEGORY