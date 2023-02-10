-- 입양 시각 구하기(2)
SET @hour := -1;

SELECT (@hour := @hour + 1) as HOUR,
(	
    SELECT COUNT(DATETIME) 
	FROM ANIMAL_OUTS 
	WHERE HOUR(DATETIME) = @hour
) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23