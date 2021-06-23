SELECT * FROM COMUNIDAD_CAMPESINA

SELECT * FROM SISCCN.CCN_VW_COMUNIDAD

SELECT * FROM MINAGRIR.COMUNIDAD


SELECT C.CODIGO,
          DEPARTAMENTO,
          PROVINCIA,
          DISTRITO,
          NOMBRE,
          CASE
             WHEN TIPO_ESTADO IS NULL THEN 'NO VINCULADA'
             ELSE TIPO_ESTADO
          END
             TIPO_ESTADO,
          MDSYS.SDO_UTIL.SIMPLIFY (SHAPE, 6, 0.0000005) AS SHAPE,
          OBJECTID
     FROM comunidad_campesina C LEFT JOIN SISCCN.CCN_VW_COMUNIDAD VC
             ON ide_comunidad = codigo AND tipo_comunidad = 'CAMPESINA'