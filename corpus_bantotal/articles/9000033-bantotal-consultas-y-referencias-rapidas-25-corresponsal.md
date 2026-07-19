---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 25. Corresponsal"
source_id: 9000033
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 25. Corresponsal

```sql
SELECT TOP 10 * FROM dbo.DECO21  -- Corresponsalía (TMo: 1=Recaudo, 2=Reverso)
SELECT * FROM XCR060             -- Banco Corresponsales
```

### Proceso creación/actualización punto corresponsal

```
1. Solicitar a Carlos Leal la base para cruzar
2. Crear un punto o actualización de puntos
3. GLPI de Operaciones
4. Prueba revisión por front de BT → revisión sube a Producción
```

### Corresponsal — Comisiones

```
1. Creación nueva oficina
2. Script en FSD526:
   - 148: Comisión depósito $3.200 (asume banco)
   - 149: Comisión retiro $2.500 (asumido cliente — 100%)
3. Sube a pre-prod
```

---
