---
title: "📚 Bantotal — Consultas y Referencias Rápidas — 2. Usuarios y Asesores"
source_id: 9000010
source_url: "local:extra_docs/bantotal/Bantotal_Rapidas.md"
ingested_by: ingest_docs.py
---

## 2. Usuarios y Asesores

```sql
SELECT TOP 10 * FROM dbo.SNGAS2                                    -- Código asesor
SELECT TOP 10 * FROM dbo.FST746                                    -- Nombre usuario asesor
SELECT TOP 10 * FROM dbo.FST046                                    -- Asesor sucursal / Módulos permitidos
SELECT TOP 10 * FROM dbo.FSE046                                    -- Correo usuario asesor
SELECT TOP 10 * FROM dbo.FSE046 WHERE Atributo = 'RELACIONCTA'    -- Cuenta del usuario
SELECT TOP 10 * FROM dbo.SNG057                                    -- Parametrización de cargos
SELECT TOP 10 * FROM dbo.JCCN22                                    -- Barrios asignados a asesores
SELECT TOP 10 * FROM dbo.FST846                                    -- Barra menús usuarios
SELECT TOP 10 * FROM dbo.PRFU00                                    -- Perfil de usuarios
SELECT TOP 10 * FROM dbo.FST047                                    -- Módulo-Usuarios
SELECT TOP 10 * FROM dbo.FST048                                    -- Transacción-Usuarios
SELECT TOP 10 * FROM dbo.FPP190                                    -- Relación préstamos con asesor
```

### Programas de administración de usuarios

| Programa | Función |
|----------|---------|
| `Hprf093` | Consulta permisos por módulo y transacción |
| `Hprf080` | Consulta programa donde entra |
| `Hprf075` | Consulta usuario programas |
| `Hprf072` | Consulta menú que programas tiene |
| `Hprf071` | Consulta programa en perfiles |
| `Hprf070` | Consulta perfiles que programas tiene |
| `Hstd0001` | Cambio de clave |
| `HPRF172` | Mantenimiento permisos por perfil/módulo/transacción |
| `HMNU001` | Mantenimiento de menús |
| `HTRT746` | Perfiles |
| `HPRF000` | Mantenimiento de perfiles |
| `hprf042` | Mantenimiento de perfiles - Usuarios |
| `hsngu02` | Panel asesores cuenta cliente / Suplentes |
| `hmbc009` | Habilitación/Inhabilitación de Usuarios Cajeros |

---
