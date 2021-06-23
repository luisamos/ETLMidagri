CREATE OR REPLACE VIEW public.v_comunidades_campesinas AS 
	SELECT cc.gid, cc.nom_comun, cc.geom
	   FROM dblink('host=10.3.0.198 user=consulta2 password=Minagri2020 dbname=georural'::text, 'SELECT objectid as gid, nom_comunidad as nom_comun, st_asbinary(shape) FROM sde.p_comunidades_campesinas' ::text) 
	   cc(gid integer, nom_comun character varying(250), geom bytea)
	   
CREATE OR REPLACE VIEW public.p_comunidades_campesinas AS	   
	   SELECT gid, nom_comun, st_geomfromwkb(geom,4248) as geom FROM public.v_comunidades_campesinas;



SELECT column_name, udt_name
FROM information_schema.columns
WHERE table_schema = 'sde' AND column_name IN ('nom_comun', 'nom_dpto', 'nom_prov', 'nom_dist')
AND table_name   = 'p_comunidades_campesinas'

SELECT st_srid(shape), st_geometrytype(shape) FROM sde.p_comunidades_campesinas;