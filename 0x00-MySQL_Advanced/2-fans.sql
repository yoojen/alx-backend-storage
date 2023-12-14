-- SELECT ORIGIN AND SUM OF FANS BASED ON THEIR ORIGIN

SELECT
    origin AS origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;
