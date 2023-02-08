-- 진료과별 총 예약 횟수 출력하기
SELECT
    MCDP_CD AS 진료과코드, COUNT(*) AS 5월예약건수
FROM
    APPOINTMENT
WHERE
    YEAR(APNT_YMD)=2022 
AND
    MONTH(APNT_YMD)=5
GROUP BY
    MCDP_CD
ORDER BY
    5월예약건수,진료과코드