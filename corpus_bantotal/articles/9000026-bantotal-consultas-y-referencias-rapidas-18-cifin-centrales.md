---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 18. CIFIN — Centrales de Riesgo"
source_id: 9000026
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 18. CIFIN — Centrales de Riesgo

```sql
SELECT * FROM FST050 WHERE COCOD = 205
SELECT * FROM fsp026 WHERE cocod = 205 ORDER BY cofech
SELECT * FROM fst098 WHERE tpdesc LIKE '%cifin%'
SELECT * FROM fst198 WHERE tp1desc LIKE '%cifin%'
SELECT * FROM FST098 WHERE Pgcod=1 AND Tpcod=13600 AND Tp1corr1=205  -- % Centrales de riesgo
SELECT * FROM FST098 WHERE Pgcod=1 AND Tpcod=13404 AND Tpcorr IN (122,123)  -- Papelería/Centrales
SELECT * FROM FST098 WHERE Pgcod=1 AND Tpcod=81020  -- Calificación cliente
```

### CIFIN — Creación oficina

```sql
SELECT * FROM FST001  -- Oficina
SELECT * FROM FBC205  -- Región
SELECT * FROM FBC206  -- Zona
SELECT * FROM FST810  -- Zona
SELECT * FROM FST811  -- Zona y Oficina
SELECT * FROM FST098 WHERE tpcod = 3967  -- Código CIFIN

INSERT INTO CIFINCONSULTA.CONSULTACIFIN_OFICINA
    (CODIGOTIPOPRODUCTO, SECUENCIALOFICINA, NOMBREOFICINA, CODIGOOFICINACIFIN, CODIGOBANTOTAL, ESTAACTIVO)
VALUES ('PSLT', 1, 'Zipaquira', '85', '84', 1);

INSERT INTO FST098 (Pgcod, Tpcod, Tpcorr, Tpnro, Tpdesc, Tpimp)
VALUES (1, 3967, 103, 501, N'Pasto MiPyme                  ', 51.00);
```

---
