SELECT objectid as gid, nom_comunidad as nom_comun, st_asbinary(shape), st_srid(shape) 
FROM sde.p_comunidades_campesinas
LIMIT 1;
	
CREATE OR REPLACE VIEW public.v_comunidades_campesinas AS 
	SELECT cc.gid,
		cc.nom_comun,		
		cc.geom
	   FROM dblink('host=10.3.0.198 user=consulta2 password=Minagri2020 dbname=georural'::text, 'SELECT objectid as gid, nom_comunidad as nom_comun, st_asbinary(shape) FROM sde.p_comunidades_campesinas' ::text) cc(gid integer, nom_comun character varying(250), geom bytea);