---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 22. Autorizaciones y Excepciones"
source_id: 9000030
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 22. Autorizaciones y Excepciones

```sql
SELECT * FROM FST039 WHERE EXCOD = 22   -- Si es Ligada (L) o Desligada (D)
SELECT * FROM FST098 WHERE TPCOD=203 AND TPCORR=22      -- Módulo
SELECT * FROM FST098 WHERE TPCOD=1495 AND TPCORR=22
SELECT * FROM FST198 WHERE TP1COD1=5557                 -- Transacciones
SELECT * FROM AUT000  WHERE JAutExCod=22
SELECT * FROM AUT0001 WHERE JAutExCod=22   -- Módulos excluidos
SELECT * FROM AUT0002 WHERE JAutExCod=22   -- Niveles de Autorización
SELECT * FROM AUT0003 WHERE JAutExCod=22   -- Montos o Rangos
SELECT * FROM AUT0004 WHERE JAutExCod=22   -- Perfiles de Autorización
```

### Árbol de Autorizaciones

| Tabla | Descripción |
|-------|-------------|
| `AUM000` | Códigos Árbol Autorizaciones |
| `AUM001` | Árbol / Nivel |
| `AUM003` | Grupos de Autorización |
| `AUM004` | Subniveles del Grupo |
| `AUM005` | Relación Mod/Trn con Árbol |
| `AUM006` | Autorización por Excepción |
| `AUT000` | Excepción por tasa o por monto |
| `AUT0002` | Excepción por Nivel |
| `AUT0003` | Excepción por Nivel/monto/tasa |
| `AUT0004` | Excepción por Nivel/Sucursal |

### Reglas de negocio

```sql
SELECT * FROM frng49 WHERE rng49cod=1187   -- Niveles Autorización Crédito
SELECT * FROM frng49 WHERE rng49cod=11400  -- Autorizaciones Créditos
SELECT * FROM FRNG49 WHERE rng49cod=12001  -- Arrendamiento Consumo
SELECT * FROM frng49 WHERE rng49cod=77101  -- Check ID
```

### Programa: `HRNG400` — Trabajar con Reglas de Negocio

---
