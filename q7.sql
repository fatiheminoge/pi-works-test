UPDATE cvs
SET
cvs.daily_vaccinations =  cvs1.median
FROM country_vaccination_stats cvs 
JOIN
(SELECT country, (CASE WHEN AVG(daily_vaccinations) IS NULL THEN 0 ELSE avg(daily_vaccinations) END) AS median FROM country_vaccination_stats cvs GROUP BY country ) AS cvs1
ON cvs.country = cvs1.country
WHERE cvs.daily_vaccinations IS NULL;