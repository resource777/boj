-- 주문량이 많은 아이스크림들 조회하기
SELECT FLAVOR
FROM
(
    SELECT *, SUM(TOTAL_ORDER) SO
    FROM
    (
        SELECT *
        FROM FIRST_HALF 
        UNION ALL 
        SELECT *
        FROM JULY    
    ) A
    GROUP BY A.FLAVOR
    ORDER BY SO DESC
    LIMIT 3
) B