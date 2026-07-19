---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 14. Canales y ACH"
source_id: 9000022
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 14. Canales y ACH

### Tablas de Cámaras

```sql
SELECT * FROM MPE001  -- Transaccional
SELECT * FROM MPE002  -- Transaccional
SELECT * FROM MPE005  -- Servicio ACH
SELECT * FROM MPE006  -- Cámara
SELECT * FROM MPE007  -- Ciclos
SELECT * FROM MPE008  -- Archivos ciclos
SELECT * FROM MPE009  -- Ciclos procesados
SELECT * FROM MPE010  -- Ciclos ID Módulo y Transacción
SELECT * FROM MPE011  -- Configuración Módulos y Transacciones
SELECT * FROM MPE020  -- Bancos
SELECT * FROM MPE024  -- Mensajes
```

### Procesos en ejecución

```sql
SELECT * FROM MPE009 ORDER BY 1 DESC
SELECT * FROM MPE005 ORDER BY 1 DESC
SELECT * FROM MPE006
```

### Ajuste ACH

```sql
SELECT * FROM MPE001 WHERE MPE001FET='2025-02-03' AND MPE001IDL IN (20983,20984);
-- Campo MPE001EST = PP
SELECT * FROM MPE002 WHERE MPE002IDL IN (20983,20984);
-- MPE002EST = 0
```

### Programas ACH

| Nro | Programa | Función |
|-----|----------|---------|
| 1 | `HARQ001` | Publicación de Servicios Bantotal |
| 2 | `HBTI025` | SDTs - Estructuras de datos |
| 3 | `HMPE0050` | Mantenimiento de Cámaras (MPE005 / MPE006) |
| 4 | `HMPE0056` | Operaciones de Cámara |
| 5 | `HIF00154` | Formatos de Cuenta en Interfaces |
| 6 | `HMPE0053` | Ciclos de cámaras |
| 7 | `HMPE0280` | Panel de Consultas de Transferencias ACH |
| 8 | `hbtsbt1t` | Mantenimiento de Transacciones por Servicio (BTSBT1) |
| 9 | `hrep001` | Reportes |

### Proceso creación entidad financiera ACH

```
1. Comunicado a operaciones (Heyman)
2. Operaciones coloca un GLPI
3. Generar script MPE020
4. Descargar Test Fly (verificar versión) — eliminar producción y token antes
5. Activar cliente con cuenta activa, saldo y token
6. Hacer transferencias por portal con token de la app
7. URL pruebas: http://172.31.57.232:4000/Contactar/login
8. Probar descarga y carga del NACHAN a Integra:
   BT / Menú Cadena de Cierre / Agregar y Descargar Archivos (PMPE0030 - ACH)
   → Solo subir, no abrir
9. Integra ACH: https://172.30.19.22/VolPayHubUI/#/hybridlogin
```

---
