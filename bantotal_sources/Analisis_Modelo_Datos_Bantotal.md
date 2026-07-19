# 🏦 Análisis del Modelo de Datos Bantotal

> **Documento de Análisis Técnico**  
> Basado en: "Estructura del Modelo de Datos Bantotal" (De Larrobla & Asociados, 2001)  
> Análisis realizado con: **pdf-processing-pro** + **bt-sql-analyzer**  
> Fecha: Octubre 2025

---

## 📋 Índice

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Fundamentos Arquitectónicos](#fundamentos-arquitectónicos)
3. [Motor GeneXus](#motor-genexus)
4. [Conceptos Técnicos Base](#conceptos-técnicos-base)
5. [Sistema de Nomenclatura](#sistema-de-nomenclatura)
6. [Configuración Maestra](#configuración-maestra)
7. [Roadmap de Análisis](#roadmap-de-análisis)
8. [Referencias y Fuentes](#referencias-y-fuentes)

---

## 🎯 Resumen Ejecutivo

### 📄 Sobre el Documento Original
- **Título**: Estructura del Modelo de Datos Bantotal
- **Autor**: Alejandro Danielián (De Larrobla & Asociados)
- **Fecha**: 25 de abril de 2001, actualizado 19 de junio de 2025
- **Páginas**: 118 páginas de documentación técnica
- **Propósito**: Capacitación sobre arquitectura y modelo de datos de Bantotal

### 🎯 Objetivos del Análisis
1. **Mapear la arquitectura** completa del sistema bancario
2. **Identificar entidades** y relaciones críticas del modelo de datos
3. **Comprender la nomenclatura** y patrones de diseño
4. **Documentar configuraciones** y parámetros del sistema
5. **Crear referencia técnica** para desarrolladores y analistas

### 📊 Estado del Análisis
- ✅ **Páginas 1-14**: Fundamentos completados
- ✅ **Páginas 15-30**: Tablas genéricas completadas
- ✅ **Páginas 31-50**: Módulos y entidades principales completadas
- ✅ **Páginas 51-70**: Sistema de clientes, plan de cuentas y seguridad completados
- ✅ **Páginas 71-90**: Sistema de precios, tasas y transacciones completados
- ✅ **Páginas 91-118**: Asientos, operaciones, históricos y herramientas completados

### 🎉 **ANÁLISIS COMPLETO AL 100%** - 118/118 páginas analizadas


---

## 🏗️ Fundamentos Arquitectónicos

### 🎪 Filosofía de Diseño
Bantotal está construido sobre **GeneXus**, un sistema que traduce automáticamente **visiones de negocio** en **código ejecutable**. 

**Analogía Clave**: GeneXus funciona como un "traductor universal" que convierte ideas bancarias en aplicaciones reales.

### 🔧 Objetos Principales del Sistema

| Tipo | Propósito | Ejemplos |
|------|-----------|----------|
| **Programas** | Consulta y actualización de datos | Altas, bajas, modificaciones |
| **Transacciones** | Metamodelo transaccional | Operaciones bancarias complejas |

### 🎭 Sistema de Roles
- **Usuarios**: Ejecutan funciones según roles asignados
- **Potestades**: Determinan acceso a funcionalidades
- **Asignaciones**: Mapeo organizacional de responsabilidades

---

## ⚙️ Motor GeneXus

### 🌟 Características Principales
GeneXus es un **sistema basado en conocimiento** que permite:

1. **Describir objetos familiares** a los usuarios del negocio
2. **Generar automáticamente** aplicaciones y base de datos
3. **Mantener consistencia** entre visión de negocio y implementación técnica

### 🖥️ Ambientes Tecnológicos Soportados

#### Desarrollo
- **Plataforma**: PCs con Windows/Windows NT
- **IDE**: Entorno GeneXus integrado

#### Producción
- **IBM AS/400** (centralizada o servidor)
- **UNIX, Windows NT**
- **Redes de PCs**

#### Lenguajes de Programación
- **AS/400**: COBOL/400, RPG/400, Java
- **Microcomputadores**: Visual Basic, Visual FoxPro, Java

#### Bases de Datos
- **Enterprise**: IBM DB2, Oracle, Informix
- **Mid-range**: Microsoft SQL Server

---

## 🔧 Conceptos Técnicos Base

### 📊 Tablas (Fundamento del Sistema)

**Definición**: Única forma de almacenar información en Bantotal (base de datos relacional)

#### Características Estructurales
- **Matriz bidimensional**: Filas (registros) y columnas (atributos)
- **Homogeneidad**: Todos los atributos representan la misma información
- **Unicidad**: No existen registros duplicados
- **Orden irrelevante**: El orden no contiene información

#### Componentes
| Elemento | Descripción | Símbolo |
|----------|-------------|---------|
| **Atributos** | Columnas de la tabla | - |
| **Registros** | Filas de la tabla | - |
| **Clave Primaria** | Identificador único | * |
| **Claves Secundarias** | Identificadores alternativos | - |

### 🔑 Sistema de Claves

#### Clave Primaria
- **Función**: Identificador único de cada registro
- **Marcado**: Con asterisco (*) en documentación
- **Unicidad**: Garantiza que no hay registros duplicados

#### Claves Secundarias/Candidatas
- **Función**: Vías de acceso alternativas
- **Uso**: Búsquedas y referencias cruzadas

### 📈 Índices (Optimización de Acceso)

#### Tipos de Índices
1. **Primarios**: Definidos para la clave primaria
2. **Extranjeros**: Control de integridad inter-tablas
3. **Del Usuario**: Acceso eficiente a datos específicos

### 🔗 Integridad Referencial

#### Tipos de Relaciones
- **1 a 1**: Relación uno a uno
- **1 a N**: Tabla superordinada (1) → tabla subordinada (N)

#### Reglas de Consistencia
1. **Eliminación**: No pueden existir registros subordinados huérfanos
2. **Creación**: Debe existir registro padre antes de crear subordinado

#### Ejemplo Real
```
FSD011 (superordinada) ←→ FST005, FST0010 (subordinadas)
```

---

## 🏷️ Sistema de Nomenclatura

### 📚 Clasificación de Tablas por Prefijo

| Prefijo | Categoría | Propósito | Ejemplos |
|---------|-----------|-----------|----------|
| **FST** | Tablas Básicas | Parámetros y configuraciones del sistema | FST017, FST001, FST717, FST028, FST013, FST069, FST068 |
| **FSD** | Datos | Información transaccional y operativa | FSD010, FSD011 |
| **FSR** | Relaciones | Vínculos y asociaciones entre entidades | - |
| **FSE** | Extensiones | Datos adicionales y especializados | - |
| **FSH** | Históricos | Registros de auditoría y cambios | - |
| **FSX** | Textos | Descripciones y comentarios | - |
| **FSA** | Auxiliares | Tablas de apoyo y temporales | - |
| **FSI** | Informaciones | Reportes y vistas de consulta | - |
| **FSM** | Menúes | Interfaces de usuario y navegación | - |
| **FSN** | Numeradores | Secuencias automáticas y contadores | FSN001, FSN002, FSN003 |

### 📋 Catálogo de Tablas FST (Configuración)

| Tabla | Propósito | Scope | Relaciones |
|-------|-----------|-------|------------|
| **FST017** | Parámetros Generales | Sistema/Empresa | Base para todas las configuraciones |
| **FST001** | Sucursales | Por Empresa | → FST017 (Empresa) |
| **FST717** | Árbol de Empresas | Grupo Empresarial | → FST017 (Empresas Matriz/Dependientes) |
| **FST028** | Calendarios | Multi-empresa/Regional | → FST001 (Sucursales) |
| **FST013** | Países | Global | → FST069 (Regiones) |
| **FST069** | Regiones | Global | → FST013 (Países), → FST068 (Localidades) |
| **FST068** | Localidades | Por País | → FST013 (Países) |
| **FST003** | Módulos | Sistema | Base operacional del banco |
| **FST004** | Tipos de Operación | Por Módulo | → FST003 (Módulos) |
| **FST110** | Sistemas | Agrupación funcional | Agrupa módulos por ámbito |
| **FST111** | Módulos de Sistema | Asociación | → FST110 (Sistemas), → FST003 (Módulos) |

### 🏦 Arquitectura de Módulos Operacionales

#### Jerarquía Funcional
```
🌐 SISTEMA (FST110)
    ↓ (FST111)
🔧 MÓDULO (FST003)
    ↓ (FST004) 
📋 TIPO DE OPERACIÓN
```

#### Módulos por Categoría Bancaria

**💰 Captación (Pasivos)**
- **FST003.20**: Cuentas Corrientes
- **FST003.21**: Caja de Ahorros  
- **FST003.22**: Depósitos a Plazo Fijo

**💸 Colocación (Activos)**
- **FST003.30**: Préstamos (con tipos FST004.1, .2, .3)
- **FST003.31**: Descuentos
- **FST003.32**: Préstamos Personales

**🏦 Servicios Bancarios**
- **FST003.50**: Cajas (Operaciones de taquilla)
- **FST003.75**: Inversiones

**🌍 Comercio Exterior**
- **FST003.2**: Cartas de Crédito Importación
- **FST003.12**: Cartas de Crédito Exportación
- **FST003.25**: Compra-Venta Valores Públicos

### 🔢 Catálogo de Tablas FSN (Numeradores)

| Tabla | Generación | Propósito | Scope |
|-------|------------|-----------|-------|
| **FSN001** | Automática | Numerador de operaciones | Por sucursal |
| **FSN002** | Automática | Numerador de operaciones | Por sucursal/módulo |
| **FSN003** | Automática | Numerador de relaciones (asientos) | Por sucursal |

> **Nota**: Los numeradores FSN se crean automáticamente al dar de alta una nueva sucursal en FST001.

### 🎯 Patrón de Arquitectura Identificado

**Observación Crítica**: El sistema sigue un patrón consistente donde:
- **FST** = Configuración y parámetros (como "settings")
- **FSD** = Operaciones y transacciones (donde ocurre la "acción")
- Otros prefijos = Funciones especializadas de soporte

---

## 🏛️ Configuración Maestra

### 📋 Tabla FST017 - Parámetros Generales

**Propósito**: Tabla maestra que define las características principales del sistema bancario.

#### Información de Institución
- **Código de Empresa**: Identificador único asignado por DL&A
- **Nombre de la Empresa**: Denominación oficial
- **Código de Cliente**: Identificación en sistemas DL&A
- **Sucursal Casa Central**: Oficina principal

#### Configuración Geográfica e Idioma
- **País**: Determina programas nacionales específicos
- **Idioma**: Interface y reportes del sistema
- **Fecha de Balance**: Referencia contable principal

#### Configuración Monetaria
- **Código Moneda Nacional**: Moneda base del país
- **Código Dólar Billete**: Para operaciones en efectivo USD
- **Código Dólar Transferencia**: Para operaciones electrónicas USD
- **Posición M/N**: Posición en moneda nacional
- **Posición M/E**: Posición en moneda extranjera

#### Configuración Técnica
- **Plataforma de Ejecución**: AS/400, SQL Server, etc.
- **Largo Código Contable**: Estructura del plan de cuentas
- **Histórico OnLine**: Disponibilidad de datos históricos
- **Administra F.Inversión**: Gestión de fondos de inversión

#### Módulos Activos
- **Módulo de Cuentas Corrientes**: Sistema de cuentas transaccionales
- **Módulo de Caja Ahorros**: Sistema de ahorros

#### Fechas Operativas
- **Fecha de Cierre**: Último cierre de operaciones
- **Fecha de Apertura**: Inicio de operaciones del día

### 🎯 Implicaciones Arquitectónicas

**Multi-tenancy**: El sistema soporta múltiples empresas en la misma instalación a través del **Código de Empresa**.

**Escalabilidad Geográfica**: Diseñado para operar en múltiples países con configuraciones específicas.

**Flexibilidad Monetaria**: Soporte nativo para operaciones multi-moneda.

---

## 🏢 Arquitectura Multi-empresa (Páginas 15-30)

### 🌟 Concepto Revolucionario: Bantotal Multi-empresa

**Bantotal no es solo un sistema bancario** - es una **"plataforma de ecosistema financiero"** que puede operar como:

1. **🏦 Institución Única**: Un banco independiente
2. **🏛️ Administradora de Fondos**: Gestión de inversiones especializada  
3. **🌐 Grupo Económico**: Múltiples instituciones bajo una plataforma común

### 🔗 Reglas de Convivencia Multi-empresa

| Compartido | No Compartido | Propósito |
|------------|---------------|-----------|
| ✅ **Plan de Cuentas** | ❌ **Cartera de Clientes** | Consistencia contable vs. Privacidad comercial |
| ✅ **Configuración Base** | ❌ **Datos Operativos** | Eficiencia técnica vs. Segregación de datos |

### 📊 Nuevas Tablas de Configuración Descubiertas

#### FST717 - Árbol de Empresas
**Propósito**: Define la jerarquía y vínculos entre empresas del grupo.

```
🏛️ Empresa Matriz
├── 🏦 Banco Comercial (Dependiente)
├── 💰 Administradora de Fondos (Dependiente)  
└── 🏪 Financiera (Dependiente)
```

**Estructura de Datos**:
- **Empresa*** (Código de empresa matriz)
- **Empresa Dependiente*** (Código de empresa subordinada)
- **Vínculos**: Relación con FST017 (Parámetros Generales)

#### FST001 - Sucursales
**Propósito**: Catálogo completo de oficinas y dependencias por empresa.

**Arquitectura Jerárquica**: 
```
🌍 Región (agrupa varias sucursales)
├── 🏢 Sucursal (oficina principal)
│   ├── 🏪 Oficina A (unidad de trabajo)
│   ├── 🏪 Oficina B (unidad de trabajo)
│   └── 🏪 Oficina C (unidad de trabajo)
└── 🏢 Sucursal 2
    └── 🏪 Oficinas dependientes...
```

**Campos de Configuración**:
- **Empresa*** + **Sucursal*** (Clave compuesta)
- **Datos de Identificación**: Nombre, Nombre Reducido
- **Información Geográfica**: Calle, Número, Ciudad, Departamento
- **Datos de Contacto**: Teléfono
- **Configuración Operativa**: Calendario de feriados regionales

#### Numeradores Automáticos (Auto-generados)
Cuando se crea una sucursal nueva, el sistema genera automáticamente:

| Tabla | Propósito | Scope |
|-------|-----------|-------|
| **FSN001** | Numerador de operaciones | Por sucursal |
| **FSN002** | Numerador de operaciones | Por sucursal/módulo |  
| **FSN003** | Numerador de relaciones (asientos) | Por sucursal |

### 🌍 Datos del Entorno

#### FST028 - Calendarios
**Función**: Sistema de gestión de fechas hábiles y festivos.

**Características Avanzadas**:
- **Multi-calendario**: Múltiples calendarios por empresa
- **Regionalización**: Festivos específicos por región/sucursal
- **Generación Automática**: El sistema puede crear calendarios automáticamente
- **Flexibilidad**: Cada sucursal puede tener su propio calendario

**Analogía**: Como tener un "Google Calendar empresarial" que entiende las particularidades locales de cada región.

#### FST013 - Países
**Función**: Catálogo mundial con información comercial y regional.

**Aplicaciones**:
- **Identificación de Personas**: Clientes nacionales e internacionales
- **Convenios Comerciales**: Participación en acuerdos regionales
- **Transacciones Internacionales**: Manejo de feriados y regulaciones
- **Conformación Regional**: Agrupaciones geográficas

**Tablas Relacionadas**:
- **FST069** - Regiones (agrupaciones de países)
- **FST068** - Localidades (ciudades/departamentos)

### 🎯 Aplicaciones Prácticas del Multi-empresa

#### 1. **Consolidación Financiera**
- **Balances Grupales**: Incluye empresa matriz + dependientes
- **Consolidación Batch**: Procesamiento automático nocturno
- **Reportes Segregados**: Por empresa individual o consolidado

#### 2. **Gestión Operativa**
- **Consulta Unificada de Clientes**: Vista integral del grupo
- **Inventarios por Sucursal**: Control descentralizado
- **Mayores Contables**: Por región/sucursal/oficina

#### 3. **Configuración Inteligente**
- **Parámetros Heredados**: Configuración base compartida
- **Personalización Local**: Adaptaciones por sucursal/región
- **Numeración Automática**: Sin colisiones entre entidades

### 🏗️ Implicaciones Arquitectónicas

#### Escalabilidad Horizontal
```
🌐 GRUPO BANCARIO
├── 🇺🇾 Uruguay (FST013)
│   ├── 🏛️ Banco Central UY (FST017)
│   │   ├── 🏢 Montevideo (FST001)
│   │   └── 🏢 Punta del Este (FST001)
│   └── 💰 Administradora UY (FST017)
└── 🇦🇷 Argentina (FST013)
    └── 🏦 Banco Filial AR (FST017)
        ├── 🏢 Buenos Aires (FST001)
        └── 🏢 Córdoba (FST001)
```

#### Segregación y Compartición
- **Datos Aislados**: Cada empresa mantiene su cartera privada
- **Infraestructura Compartida**: Plan de cuentas, configuraciones base
- **Compliance Automático**: Regulaciones por país/región

### 🎯 Patrones de Diseño Identificados

#### Patrón "Tenant Híbrido"
- **Multi-tenancy Controlado**: Empresas separadas, infraestructura compartida
- **Jerarquías Flexibles**: Soporte para estructuras organizacionales complejas
- **Configuración Heredada**: Parámetros globales + personalizaciones locales

#### Patrón "Numeración Inteligente"
- **Auto-generación**: Numeradores creados automáticamente
- **Scope Controlado**: Por sucursal/módulo para evitar colisiones
- **Trazabilidad**: Cada operación queda vinculada a su origen

---

## 🔧 Arquitectura de Módulos y Sistemas (Páginas 31-50)

### 🎯 Concepto Revolucionario: Módulos Duales

**Los módulos en Bantotal tienen "doble personalidad"** - pueden funcionar como:

1. **🏢 Sectores Operativos**: Agrupan transacciones por área del banco
2. **⚙️ Operativas Específicas**: Definen comportamientos particulares (devengo, mora, etc.)

**Analogía**: Como un **"departamento corporativo inteligente"** que puede ser tanto una división organizacional como un conjunto de reglas de negocio.

### 🏗️ Jerarquía Operacional Completa

```
🌐 SISTEMA (Ámbito operativo mayor)
├── 🔧 MÓDULO (Sector/Operativa)
│   ├── 📋 TIPO DE OPERACIÓN 1 (Variante específica)
│   ├── 📋 TIPO DE OPERACIÓN 2 (Variante específica)
│   └── 📋 TIPO DE OPERACIÓN N (Variante específica)
└── 🔧 MÓDULO 2...
```

### 📊 Nuevas Tablas Operacionales Descubiertas

#### FST003 - Módulos
**Propósito**: Catálogo maestro de módulos del sistema.

**Campos Críticos**:
- **Módulo*** (Código único)
- **Nombre de Módulo** (Descripción funcional)
- **Cobra IVA en el Pago?** (Configuración tributaria)
- **Plazo calendario M/N?** (Moneda nacional)
- **Plazo calendario M/E?** (Moneda extranjera)

#### FST004 - Tipos de Operación  
**Propósito**: Variantes específicas dentro de cada módulo.

**Campos Críticos**:
- **Módulo*** + **Tipo de Operación*** (Clave compuesta)
- **Tipo de Pizarra relacionada** (Sistema de precios)
- **Nombre Tipo de Operación** (Descripción)

#### FST110 - Sistemas
**Propósito**: Agrupaciones de alto nivel de módulos relacionados.

**Estructura**:
- **Código de Sistema*** (Identificador único)
- **Nombre de Sistema** (Descripción del ámbito)

#### FST111 - Módulos de Sistema
**Propósito**: Asociación entre sistemas y módulos.

**Relación**:
- **Código de Sistema*** + **Módulo*** (Clave compuesta)
- Vincula FST110 con FST003

### 🏦 Catálogo de Módulos Operacionales

#### Módulos de Captación
| Código | Nombre | Tipo |
|--------|---------|------|
| **20** | Cuentas Corrientes | Sector Operativo |
| **21** | Caja de Ahorros | Sector Operativo |
| **22** | Depósitos a Plazo Fijo | Operativa |

#### Módulos de Colocación  
| Código | Nombre | Tipo |
|--------|---------|------|
| **30** | Préstamos | Sector Operativo |
| **31** | Descuentos | Operativa |
| **32** | Préstamos Personales | Sector + Operativa |

#### Módulos de Servicios
| Código | Nombre | Tipo |
|--------|---------|------|
| **50** | Cajas | Sector Operativo |
| **75** | Inversiones | Sector Operativo |

#### Módulos de Comercio Exterior
| Código | Nombre | Tipo |
|--------|---------|------|
| **2** | Cartas de Crédito Importación | Operativa |
| **12** | Cartas de Crédito Exportación | Operativa |
| **25** | Compra-Venta Valores Públicos | Operativa |

### 🎯 Tipos de Operación en Préstamos (Módulo 30)

| Tipo | Descripción | Sistema de Amortización |
|------|-------------|-------------------------|
| **1** | Préstamos a Plazo Fijo | Sin amortización |
| **2** | Amortizables M. Francés | Cuotas fijas |
| **3** | Amortizables M. Alemán | Capital fijo |

### 🌐 Sistemas de Agrupación

#### Sistema 1 - Cuentas Corrientes
- Módulo 1: Cuentas Corrientes
- Módulo 20: Cuentas Corrientes (variante)
- Módulo 2: Caja de Ahorros
- Módulo 3: Depósitos a Plazo Fijo

#### Sistema 5 - Descuento de Documentos
- Módulos especializados en descuentos
- Operaciones de financiamiento a corto plazo

### 🏛️ Sistema de Clientes - Arquitectura Completa

### 🎭 Entidades Fundamentales

#### 1. **Personas** (Entidad Base)
**Identificación**: Número oficial (documento de identidad)

**Tipos**:
- 👤 **Personas Físicas**: Individuos naturales
- 🏢 **Personas Jurídicas**: Empresas y sociedades legalmente constituidas
  - 🏛️ **Carácter Público**: Organismos estatales
  - 🏪 **Carácter Privado**: Empresas comerciales

**Scope Expandido**: No solo clientes, también:
- 🤝 Proveedores del banco
- 🏦 Bancos corresponsales  
- 👨‍💼 Empleados de la institución

#### 2. **Cuentas** (Entidad Operativa)
**Identificación**: Número interno asignado por el banco

**Características**:
- **Integración**: Pueden asociar múltiples personas
- **Flexibilidad**: Personas de igual o distinta naturaleza
- **Gestión**: Controladas por el banco

#### 3. **Grupos** (Entidad de Clasificación)
**Identificación**: Número y tipo asignado por:
- 🏦 El banco (clasificación interna)
- 🏛️ Organismos de supervisión (regulatorio)

**Aplicaciones**:
- 💰 **Tasas uniformes**: Tratamiento igualitario en intereses
- 📄 **Emisión conjunta**: Extractos consolidados
- 📊 **Reportes grupales**: Análisis de riesgo concentrado
- 🎯 **Estrategias comerciales**: Segmentación de clientes

### 🔗 Estructura Jerárquica del Sistema de Clientes

```
🎯 GRUPO (Clasificación estratégica)
├── 🏦 CUENTA 1 (Número interno del banco)
│   ├── 👤 PERSONA A (Física - Documento país X)
│   ├── 👤 PERSONA B (Física - Documento país Y) 
│   └── 🏢 PERSONA C (Jurídica - Registro comercial)
├── 🏦 CUENTA 2 (Número interno del banco)
│   └── 👤 PERSONA D (Individual)
└── 🏦 CUENTA N...
```

### 🎯 Identificación de Personas (Estándar Internacional)

**Estructura del Identificador**:
- 🌍 **Código de País** (Emisor del documento)
- 📋 **Tipo de Documento** (Cédula, Pasaporte, RUT, etc.)
- 🔢 **Número de Documento** (Identificador único)

**Ejemplo Práctico**:
```
🇺🇾 URU + CI + 12345678 = Cédula uruguaya
🇦🇷 ARG + DNI + 87654321 = DNI argentino  
🇺🇸 USA + PASS + ABC123456 = Pasaporte estadounidense
```

### 🚀 Implicaciones Arquitectónicas

#### Flexibilidad Operativa
- **Cuentas mixtas**: Personas físicas + jurídicas en la misma cuenta
- **Representación**: Personas jurídicas con representantes físicos
- **Multi-país**: Identificación internacional estandardizada

#### Gestión Estratégica
- **Segmentación**: Grupos para tratamiento diferenciado
- **Compliance**: Trazabilidad completa de personas vinculadas
- **Riesgo**: Análisis de concentración por grupos económicos

#### Escalabilidad
- **Multi-entidad**: Soporte para bancos corresponsales
- **Multi-jurisdicción**: Diferentes tipos de documentos por país
- **Multi-propósito**: Clientes, proveedores, empleados en un solo sistema

---

## 💾 Sistema de Clientes - Arquitectura Detallada (Páginas 51-57)

### 🗄️ Diagrama de Relaciones Completo

**Analogía Clave**: El sistema de clientes de Bantotal funciona como una **"Red Social Bancaria"** donde cada entidad tiene múltiples formas de conectarse y relacionarse.

```
🎯 GRUPOS ECONÓMICOS (FSD009)
    ↓ agrupa
🏦 CUENTAS (FSD008) ←→ 👥 INTEGRACIÓN (FSR008)
    ↓ pertenece
👤 PERSONAS (FSD001)
    ├── 👨 Físicas (FSD002)
    ├── 🏢 Jurídicas (FSD003)  
    └── 🏦 Inst. Financieras (FSD004)
    
📍 DOMICILIOS         📞 TELÉFONOS
├── FSD005 (Personas) ├── FSR005 (Personas)
└── FSD006 (Cuentas)  └── FSR006 (Cuentas)

💑 RELACIONES PERSONALES
├── FSR002 (Cónyuges)
└── FSR003 (Integración P.Jurídica)
```

### 📊 Catálogo Detallado de Tablas FSD (Datos Operativos)

| Tabla | Entidad | Propósito | Claves Principales |
|-------|---------|-----------|-------------------|
| **FSD001** | Personas | Registro maestro universal | País* + TipoDoc* + NroDoc* |
| **FSD002** | Personas Físicas | Datos específicos individuos | País* + TipoDoc* + NroDoc* |
| **FSD003** | Personas Jurídicas | Datos específicos empresas | País* + TipoDoc* + NroDoc* |
| **FSD004** | Inst. Financieras | Bancos corresponsales | País* + TipoDoc* + NroDoc* |
| **FSD005** | Domicilios Personas | Direcciones individuales | Persona* + CódigoDomicilio* |
| **FSD006** | Domicilios Cuentas | Direcciones corporativas | Empresa* + Cuenta* + CódigoDomicilio* |
| **FSD008** | Cuentas | Números internos del banco | Empresa* + NroCuenta* |
| **FSD009** | Grupos de Cuentas | Clasificación estratégica | TipoGrupo* + NroGrupo* + Empresa* + Cuenta* |

### 🔗 Catálogo de Tablas FSR (Relaciones)

| Tabla | Relación | Propósito | Patrón |
|-------|----------|-----------|--------|
| **FSR002** | Cónyuges | Vínculos matrimoniales | Persona ↔ Cónyuge |
| **FSR003** | Integración P.Jurídica | Socios/Accionistas | P.Jurídica ← P.Física |
| **FSR004** | Cuentas en Inst.Financ. | Cuentas en otros bancos | Institución → Cuenta |
| **FSR005** | Teléfonos Personas | Contactos individuales | Persona → Múltiples teléfonos |
| **FSR006** | Teléfonos Cuentas | Contactos corporativos | Cuenta → Múltiples teléfonos |
| **FSR008** | Integración Cuentas | Titularidad múltiple | Cuenta ↔ Múltiples personas |

### 📋 Sistema de Calificadores FST (Páginas 56-57)

**Analogía**: Los calificadores funcionan como **"etiquetas inteligentes"** que clasifican automáticamente cada entidad según criterios regulatorios y comerciales.

#### 👤 Clasificación de Personas
| Calificador | Tabla | Aplicación |
|-------------|-------|------------|
| **Tipos de Documentos** | FST014 | Cédula, Pasaporte, RUT, DNI |
| **Capacidad Legal** | FST008 | Mayor, Menor, Interdicto |
| **Estado Civil** | FST009 | Soltero, Casado, Divorciado |
| **Sectores Económicos** | FST091 | Clasificación económica CIIU |

#### 🏢 Clasificación de Jurídicas
| Calificador | Tabla | Aplicación |
|-------------|-------|------------|
| **Naturaleza Jurídica** | FST021 | SA, SRL, Fundación |
| **Sociedades de Consumo** | FST792 | Cooperativas, Mutuales |

#### 🏦 Clasificación de Cuentas y Grupos
| Calificador | Tabla | Aplicación |
|-------------|-------|------------|
| **Categorías de Riesgo** | FST212 | A, B, C, D, E |
| **Tipos de Grupo** | FST030 | Económico, Familiar, Comercial |
| **Segmentos de Mercado** | FST041 | Premium, Corporate, Retail |

#### 🔗 Relacionadores
| Calificador | Tabla | Aplicación |
|-------------|-------|------------|
| **Vínculos** | FST020 | Socio, Apoderado, Representante |
| **Titularidad** | FST007 | Titular, Autorizado, Beneficiario |

### 🚀 Implicaciones Arquitectónicas del Sistema de Clientes

#### Flexibilidad Total
- **Personas mixtas**: Una cuenta puede tener personas físicas + jurídicas
- **Grupos dinámicos**: Clasificación automática por criterios múltiples
- **Multi-domicilio**: Direcciones diferenciadas por uso (comercial, legal, correspondencia)

#### Compliance Automático
- **Trazabilidad completa**: Cada relación documentada y auditada
- **Clasificación regulatoria**: Automática según normativas locales
- **Gestión de riesgo**: Análisis de concentración por grupos económicos

---

## 📊 Plan de Cuentas - Motor Contable (Páginas 58-63)

### 🏗️ Arquitectura del Plan de Cuentas

**Analogía Central**: El Plan de Cuentas de Bantotal es como un **"GPS Contable"** que determina automáticamente cómo registrar cada transacción según reglas predefinidas.

```
🎯 REGULACIÓN BANCARIA (Autoridad Monetaria)
    ↓ define estructura
📋 PLAN DE CUENTAS (FSD014)
    ↓ organiza por
🏗️ PRIMER MÓDULO (FSD013)
    ↓ establece reglas
🔗 RELACIONES DE RUBROS (FSR014)
    ↓ conecta con
⚙️ MÓDULOS OPERATIVOS
```

### 📋 Estructura de Tablas del Plan Contable

| Tabla | Propósito | Función Central |
|-------|-----------|----------------|
| **FSD014** | Plan de Cuentas | Catálogo maestro de rubros contables |
| **FSD013** | Primer Módulo | Agrupación por naturaleza (Activo, Pasivo, etc.) |
| **FSR014** | Relaciones de Rubros | Vínculos automáticos entre cuentas |

### 🎯 FSD014 - Plan de Cuentas (Tabla Central)

**Atributos Clave**:
- **Rubro*** (Clave primaria): Código contable único
- **Configuración operativa**:
  - Título, Capítulo: Organización jerárquica
  - Dígito de Plazo, Grupo de Cuentas: Clasificación temporal
  - Signo Positivo?, M/N, M/E: Tratamiento de monedas
- **Reglas de negocio**:
  - Analiza por Plazo: Vencimientos automáticos
  - Permite Sobregiro?: Control de límites
  - Baja Parcial?, Incremento?: Operaciones permitidas
- **Integración modular**:
  - Módulo, Es Caja?: Conexión con operativa
  - Por Cuenta?, Por Operación?, Por Suboperación?: Nivel de detalle

### 🏗️ FSD013 - Primer Módulo (Organización Jerárquica)

**Función**: Agrupa cuentas contables por naturaleza económica similar.

**Atributos**:
- **Título***, **Capítulo***, **Dígito de Plazo***, **Grupo de Cuentas*** (Clave compuesta)
- **Nombre Primer Módulo**: Descripción del agrupamiento
- **Configuraciones especiales**:
  - Devenga: Cálculo automático de intereses
  - Imputable?: Permite movimientos directos

### 🔗 FSR014 - Relaciones de Rubros (Inteligencia Contable)

**Analogía**: Funciona como **"sinapsis contables"** que conectan automáticamente cuentas relacionadas.

**Estructura**:
- **Rubro*** + **Código de Relación*** (Clave compuesta)
- **Rubro Relacionado**: Cuenta destino de la relación
- **Condiciones**: Reglas para activar la relación

**Ejemplo Práctico**:
```
Cuenta: "Préstamos Vigentes" 
Relación: "Intereses por Cobrar"
Condición: "Al momento del devengo"
```

### 🎯 Aplicaciones del Plan de Cuentas

#### Automatización de Imputaciones
- **Por Cuenta**: Movimientos agregados por cliente
- **Por Operación**: Detalle por préstamo/depósito individual  
- **Por Suboperación**: Máximo nivel de granularidad

#### Control de Operaciones
- **Moneda Nacional vs. Extranjera**: Segregación automática
- **Sobregiros**: Validación de límites en tiempo real
- **Bajas Parciales**: Control de amortizaciones
- **Incrementos**: Validación de aumentos de líneas

#### Tratamiento de Saldos
- **Permite Sobregiro**: Cuentas corrientes vs. ahorros
- **Permite Baja Parcial**: Préstamos amortizables vs. bullet
- **Permite Incrementos**: Líneas de crédito vs. préstamos fijos

### 🌐 Integración con Módulos Operativos

El Plan de Cuentas actúa como **"traductor universal"** entre:
- **Operaciones comerciales** (Préstamos, Depósitos)
- **Registro contable** (Debe, Haber)
- **Reportes regulatorios** (Balances, Estados)

---

## 🔒 Sistema de Seguridad - Arquitectura de Control (Páginas 64-70)

### 🛡️ Filosofía de Seguridad

**Analogía Central**: El sistema de seguridad de Bantotal funciona como un **"Sistema de Credenciales Inteligente"** con múltiples niveles de validación, similar a un edificio corporativo con diferentes zonas de acceso.

```
🏢 EDIFICIO BANCARIO
├── 🚪 Lobby (Menús públicos)
├── 🔐 Oficinas (Módulos operativos)  
├── 🏦 Bóveda (Transacciones críticas)
└── 🚨 Sala de Control (Excepciones y supervisión)
```

### 🏗️ Arquitectura de Seguridad de 4 Niveles

```
1️⃣ USUARIO (FST046/FST746)
    ↓ tiene permisos en
2️⃣ MÓDULO (FST047)
    ↓ puede ejecutar  
3️⃣ TRANSACCIÓN (FST048)
    ↓ puede requerir
4️⃣ EXCEPCIÓN (FST039/FSH010)
```

### 👥 Nivel 1: Gestión de Usuarios

| Tabla | Propósito | Atributos Clave |
|-------|-----------|----------------|
| **FST046** | Códigos de Usuarios | Empresa*, Usuario* |
| **FST746** | Usuarios Activos | Usuario*, Nombre, Empresa actual |
| **FST146** | Usuarios Ejecutivos | Usuario*, Cod.Ejecutivo*, Es propietario? |

**Características del Usuario**:
- **Número de Caja**: Asignación física de terminal
- **Menú Inicial**: Pantalla de entrada personalizada
- **Sucursal**: Ubicación operativa
- **Es Cajero?**: Perfil operativo específico
- **Nivel de Usuario**: Jerarquía de autorización

### 🔧 Nivel 2: Autorizaciones por Módulo (FST047)

**Función**: Define qué módulos operativos puede usar cada usuario.

**Permisos Granulares**:
- **Ingreso a Transacción?**: Puede iniciar operaciones
- **Confirmación de Transacción?**: Puede completar operaciones
- **Supervisa Transacción?**: Puede autorizar excepciones

**Ejemplo Práctico**:
```
Usuario: "CAJERO001"
Módulo: "Cuentas Corrientes" 
Permisos: Ingreso=Sí, Confirmación=Sí, Supervisión=No
```

### ⚙️ Nivel 3: Autorizaciones por Transacción (FST048)

**Función**: Control específico por tipo de operación dentro de cada módulo.

**Estructura**:
- **Empresa*** + **Usuario*** + **Módulo*** + **Transacción*** (Clave compuesta)
- **Mismos permisos granulares** que en módulos

**Ejemplo de Escalamiento**:
```
Módulo: "Préstamos"
├── Transacción: "Consulta" → Todos los usuarios
├── Transacción: "Otorgamiento" → Solo oficiales de crédito  
└── Transacción: "Castigo" → Solo gerencia
```

### 🚨 Nivel 4: Sistema de Excepciones (FST039/FSH010)

**Analogía**: Funciona como un **"Sistema de Alertas Inteligente"** que detecta operaciones fuera de parámetros normales.

#### FST039 - Códigos de Excepción (Configuración)
- **Código de Excepción***: Identificador único
- **Nombre Excepción**: Descripción del evento
- **Nivel de Clave Requerido**: Jerarquía de autorización necesaria
- **Tipo de Autorización**: Modalidad de aprobación

#### FSH010 - Excepciones (Registro Histórico)
**Clave Compuesta**: Empresa* + Módulo* + Sucursal* + Transacción* + Nro.Relación* + Fecha*

**Trazabilidad Completa**:
- **Usuario que solicito**: Iniciador de la excepción
- **Workstation que solicito**: Terminal origen
- **Usuario que autoriza**: Aprobador
- **Workstation que autoriza**: Terminal de aprobación
- **Hora de autorización**: Timestamp exacto

**Datos de Contexto**:
- **Saldo a autorizar**: Monto involucrado
- **Tasa base vs. Tasa solicitada**: Desviación detectada
- **Precio base vs. Precio solicitado**: Condiciones especiales
- **Código Ejecutivo que autoriza**: Responsabilidad personal

### 🎭 Perfiles de Autorización - Sistema Inteligente

**Filosofía**: Los perfiles resuelven la administración masiva de seguridad mediante **"plantillas de acceso"** que reflejan roles organizacionales reales.

#### Beneficios del Sistema de Perfiles
1. **Escalabilidad**: Un perfil se asigna a múltiples usuarios
2. **Consistencia**: Mismo rol = mismos permisos
3. **Mantenibilidad**: Cambio en perfil afecta a todos los usuarios
4. **Auditabilidad**: Trazabilidad por grupos de acceso

#### Ejemplo de Perfiles Bancarios
```
🏦 PERFIL: "Cajero Comercial"
├── Módulos: Cuentas Corrientes, Cajas, Ahorros
├── Transacciones: Depósitos, Retiros, Consultas
└── Excepciones: Solo hasta $1,000

🏢 PERFIL: "Oficial de Crédito"  
├── Módulos: Préstamos, Garantías, Seguros
├── Transacciones: Evaluación, Otorgamiento
└── Excepciones: Hasta $50,000 con supervisión

🎯 PERFIL: "Gerente Sucursal"
├── Módulos: Todos los operativos
├── Transacciones: Todas las comerciales
└── Excepciones: Autorización hasta $500,000
```

### 🚀 Implicaciones de Seguridad

#### Compliance y Auditoria
- **Trazabilidad completa**: Cada acción registrada con timestamp y usuario
- **Segregación de funciones**: Operador ≠ Autorizador ≠ Supervisor
- **Evidencia digital**: Rastro completo para auditorías

#### Operatividad y Control
- **Escalamiento automático**: Excepciones van al nivel correcto
- **Flexibilidad organizacional**: Perfiles adaptables a estructura bancaria
- **Control de riesgos**: Límites por usuario, transacción y monto

---

## 💰 Sistema de Precios - Motor de Pizarras (Páginas 71-83)

### 🎪 Filosofía del Sistema de Precios

**Analogía Central**: El Sistema de Precios de Bantotal funciona como una **"Bolsa de Valores Interna"** que gestiona automáticamente todas las tarifas y cotizaciones del banco en tiempo real.

```
📊 PIZARRA MAESTRA
├── 💱 TIPOS DE CAMBIO (dinámicos)
├── 💵 COMISIONES (genéricas + específicas)
└── 📈 TASAS (por monto + plazo + cuenta)
```

**Beneficio Clave**: Permite crear un **"manual de tarifas"** automático con control granular desde nivel general hasta cuenta específica.

### 💱 Tipos de Cambio - Motor Cambiario (Páginas 73-74)

#### 🏗️ Arquitectura Cambiaria

| Tabla | Propósito | Actualización |
|-------|-----------|---------------|
| **FST005** | Monedas Maestras | Configuración estática |
| **FSH005** | Cotizaciones Diarias | Histórico dinámico automático |

#### 🌍 FST005 - Monedas (Configuración)

**Atributos Estructurales**:
- **Código de Moneda*** (Clave): Identificador único (USD, EUR, UYU)
- **Configuración básica**:
  - Signo Monetario: $ € £
  - Nombre de la moneda: "Dólar Estadounidense"
  - Multiplica/Divide: Relación respecto al dólar

**Configuración Técnica**:
- **Código equivalente**: Para rubros de valuación contable
- **Redondeo**: Cantidad de decimales permitidos
- **Códigos internacionales**: SWIFT (USD), REUTER, símbolo SWIFT

#### 📈 FSH005 - Cotizaciones (Histórico Dinámico)

**Clave Compuesta**: Moneda* + Fecha Desde*

**Cotizaciones Múltiples**:
- **Tipo de Cambio**:
  - T/Cambio Cierre Comprador/Vendedor
  - T/Cambio Comprador/Vendedor Empleados
  - T/Cambio Comprador/Vendedor Especial

- **Arbitraje** (respecto al dólar):
  - Arbitraje Cierre Comprador/Vendedor
  - Arbitraje REUTER

**Automatización**: Todos los días se pasa automáticamente al histórico de cotizaciones.

### 🎭 Especies - Valores y Papeles (Páginas 75-76)

**Analogía**: Las especies amplían el concepto de "moneda" a **"instrumentos financieros"** (billetes, bonos, valores públicos).

#### 🏛️ FST205 - Especies (Catálogo de Instrumentos)

**Clave**: Código de Papel*

**Configuración del Instrumento**:
- **Identificación**:
  - Símbolo de Papel, Nombre de Papel
  - Moneda de Papel, País, Emisor
  
- **Características Operativas**:
  - Tolerancia Compras/Ventas
  - Total Emisión, Grupo de Papel, Clase de Papel
  
- **Características Financieras**:
  - Devenga Intereses?, Cotiza con interés incluido?
  - Tipo de año, Tipo de Cálculo de Interés
  - Tipo de Plazo, Tipo de Ajuste en Vencimiento

#### 📊 FSH205 - Cotizaciones de Especies (Histórico)

**Clave Compuesta**: Código de Papel* + Fecha Desde*

**Precios Múltiples**:
- Precio de Compra, Precio de Venta, Precio de Cierre
- Fecha Inversa para control temporal

### 💵 Sistema de Comisiones - Tarifario Inteligente (Páginas 77-78)

**Analogía**: Funciona como un **"Sistema de Tarifas Escalonadas"** que aplica automáticamente la comisión correcta según cliente y operación.

#### 🏗️ Jerarquía de Comisiones

```
1️⃣ COMISIONES GENÉRICAS (para todos)
    ↓ sobrescribe si existe
2️⃣ COMISIONES POR CUENTA (específicas)
```

#### 📋 Estructura de Tablas

| Tabla | Propósito | Scope |
|-------|-----------|-------|
| **FST050** | Tipos de Comisiones | Catálogo maestro |
| **FSR026** | Comisiones Genéricas | Tarifas estándar |
| **FSD026** | Comisiones por Cuenta | Tarifas específicas |

#### 🎯 FST050 - Tipos de Comisiones (Catálogo)

**Clave**: Código de Comisión*
- **Nombre de Comisión**: "Gastos SWIFT", "Bajo promedio CA"

#### 💰 FSR026 - Comisiones Genéricas

**Clave Compuesta**: Empresa* + Módulo* + Código de Comisión* + Cuenta* + Papel* + Moneda* + Fecha Desde*

**Configuración Escalonada**:
- **Vigente?**: Estado activo/inactivo
- **Estructura tarifaria**:
  - Tasa: Porcentaje aplicable
  - Comisión Mínima/Máxima: Límites automáticos
  - Importe Fijo: Tarifa plana alternativa

#### 🎯 FSD026 - Comisiones por Cuenta (Específicas)

**Misma estructura** que genéricas pero con **Monto hasta*** adicional para escalas por volumen.

### 📈 Sistema de Tasas - Motor de Intereses (Páginas 79-83)

**Analogía**: El sistema de tasas funciona como una **"Calculadora Financiera Automática"** que determina la tasa correcta según múltiples criterios.

#### 🏗️ Arquitectura de Tasas de 3 Niveles

```
1️⃣ TASAS GENÉRICAS POR CLASE
    ↓ especializa por monto
2️⃣ TASAS POR MONTO Y PLAZO  
    ↓ personaliza por cliente
3️⃣ TASAS POR CUENTA ESPECÍFICA
```

#### 📚 Catálogo de Tablas de Tasas

| Tabla | Propósito | Granularidad |
|-------|-----------|-------------|
| **FST024** | Tipos de Tasas | Configuración base |
| **FST029** | Clases de Tasas | Categorías (mora, transferencia, LIBOR) |
| **FSD024** | Tasas Genéricas por Clase | Estándar por tipo |
| **FSD025** | Tasas por Monto | Escalas volumétricas |
| **FSD027** | Tasas por Cuenta | Personalización cliente |
| **FSR025** | Pizarra Tasas por Monto y Plazo | Matrices dinámicas |
| **FSR027** | Pizarra Tasas por Cuenta | Matrices personalizadas |

#### 🎭 FST024 - Tipos de Tasas (Base Técnica)

**Clave**: Tipo de Tasa*

**Configuración Técnica**:
- **Nombre de Tasa**: Descripción
- **Efectiva/Lineal**: Tipo de cálculo
- **Mensual/Anual**: Periodicidad

#### 🏷️ FST029 - Clases de Tasas (Categorización)

**Clave**: Clase de Tasa*

**Ejemplos**: "Tasa de transferencia", "Tasa mora", "LIBOR", "Referencia BCE"

#### 📊 Pizarras Dinámicas (FSR025/FSR027)

**Función**: Matrices multidimensionales que cruzan **Monto × Plazo × Cuenta** para determinar tasa exacta.

**Tipos de Pizarra**:
- **Genérica**: Aplicable a todos
- **Por cuenta**: Residente, No residente, Empleados

**Atributos de Control**:
- **Porcentaje Tolerancia**: Margen de flexibilidad operativa
- **Fecha Desde/Inversa**: Control temporal de vigencia

### 🔧 Definición de Transacciones - ADN Operativo (Páginas 84-90)

**Analogía Central**: La Definición de Transacciones es el **"ADN Operativo"** que determina cómo se comporta cada operación bancaria desde la captura hasta la contabilización.

#### 🏗️ Arquitectura de Transacciones

```
🎯 CABEZAL (FST034) - Configuración general
    ↓ contiene
📋 ORDINALES (FST035) - Campos de captura
    ↓ pueden tener  
🔢 SUBORDINALES (FST036) - Asientos contables
    ↓ pueden ejecutar
⚙️ CÁLCULOS (FST040) - Lógica automática
```

#### 📊 Estructura de Tablas Transaccionales

| Tabla | Propósito | Función |
|-------|-----------|---------|
| **FST034** | Cabezal de Transacción | Configuración operativa global |
| **FST035** | Ordinales | Definición de campos de captura |
| **FST036** | SubOrdinales | Estructura de asientos contables |
| **FST040** | Cálculos | Lógica automática y validaciones |
| **FSX017** | Textos de Transacción | Mensajes dinámicos |
| **FST037** | Textos de Ordinal | Ayudas contextuales |

#### 🎯 FST034 - Cabezal de Transacción (Control Maestro)

**Clave Compuesta**: Empresa* + Módulo* + Transacción*

**Configuración Operativa**:
- **Nombre de Transacción**: Descripción funcional
- **Código de Preformato**: Plantilla de captura
- **Control de flujo**:
  - Retoma para confirmación?: Workflow de 2 pasos
  - Primer/Segundo Ordinal para confirmación: Puntos de validación

**Capacidades Operativas**:
- **Monedas soportadas**: M/N?, M/E?
- **Operaciones permitidas**: Incrementos?, Bajas Parciales?, Baja Anticipada?
- **Contabilidad**: Neteo de Partidas Contables?
- **Comunicaciones**: Mensaje Swift, Ingresa Texto Libre?

#### 📋 FST035 - Ordinales (Campos de Captura)

**Clave Compuesta**: Empresa* + Módulo* + Transacción* + Ordinal*

**Configuración de Campo**:
- **Comportamiento**: 
  - Ordinal Opcional?, Ordinal Repetitivo?
  - Vo.Bo.Sobregiro?, Sinónimos?, Cálculos asociados?
- **Tipo de asiento**: 1=Debe, 2=Haber

**Control de Datos** (por cada campo):
- **Sucursal, Moneda, Cuenta, Operación, SubOperación, Importe, Papel**
- **Modalidades**: Pide/Asume/Fuerza
  - **Pide**: Usuario debe ingresar
  - **Asume**: Toma valor por defecto  
  - **Fuerza**: Valor fijo predeterminado

**Configuración Financiera**:
- **Fechas**: Tratamiento Fecha Valor/Vencimiento
- **Plazos**: Tipo Plazo M/N, Tipo Plazo M/E
- **Tasas**: Tipo Año M/N, Tipo Año M/E, Tasa Interés?, Mora?

#### 🔢 FST036 - SubOrdinales (Asientos Contables)

**Clave Compuesta**: Empresa* + Módulo* + Transacción* + Ordinal* + SubOrdinal*

**Estructura Contable**:
- **Rubro Contable**: Cuenta a imputar
- **Módulo + Código Relación de Rubro**: Vínculo automático
- **Ordinal Relacionado**: Referencia cruzada

#### ⚙️ FST040 - Cálculos (Lógica Automática)

**Clave Compuesta**: Empresa* + Módulo* + Transacción* + Ordinal* + Nro. Línea de Cálculo*

**Motor de Cálculos**:
- **Comparaciones**: Código + Ordinal + Tipo de Importe de Comparación
- **Operaciones**: Código + Ordinal + Tipo de Importe de Operación  
- **Coeficientes**: Código de Coeficiente, Coeficiente Particular

### 🎯 Integración del Sistema de Precios

#### Flujo Automático de Precios
```
💰 OPERACIÓN INICIADA
    ↓ consulta
📊 PIZARRA (genérica o específica)
    ↓ determina  
💵 TASA + COMISIÓN
    ↓ aplica en
🔢 CÁLCULOS AUTOMÁTICOS
    ↓ registra en
📋 ASIENTO CONTABLE
```

#### Jerarquía de Aplicación
1. **Tasas por Cuenta** (si existe) → sobrescribe a
2. **Tasas por Monto** (si existe) → sobrescribe a  
3. **Tasas Genéricas** (siempre existe)

### 🚀 Implicaciones del Motor de Precios

#### Automatización Total
- **Cálculo dinámico**: Tasas y comisiones según contexto
- **Histórico automático**: Trazabilidad completa de cambios
- **Escalas automáticas**: Aplicación por volumen y plazo

#### Flexibilidad Comercial  
- **Tarifas diferenciadas**: Por tipo de cliente (empleados, residentes)
- **Promociones temporales**: Control por fechas de vigencia
- **Productos específicos**: Configuración granular por módulo/operación

#### Control de Riesgos
- **Tolerancias**: Márgenes de flexibilidad controlados
- **Excepciones**: Escalamiento automático fuera de parámetros
- **Auditoría**: Registro histórico de todas las cotizaciones

---

## 📝 Motor de Asientos - Registro Contable Automático (Páginas 95-100)

### 🎯 Filosofía de Asientos

**Analogía Central**: Los asientos de Bantotal funcionan como un **"Notario Automático"** que registra cada transacción con trazabilidad completa y evidencia digital irrefutable.

```
💼 TRANSACCIÓN EJECUTADA
    ↓ genera automáticamente
📋 ASIENTO CONTABLE
├── 🎯 CABEZAL (FSD015) - Control general
└── 📊 DETALLE (FSD016) - Movimientos específicos
    └── 📝 TEXTOS (FSX015/FSX016) - Descripciones
```

#### 🏗️ Estructura de Asientos

| Tabla | Propósito | Función |
|-------|-----------|---------|
| **FSD015** | Cabezal de Asiento | Control y trazabilidad general |
| **FSD016** | Detalle de Asiento | Movimientos contables específicos |
| **FSX015** | Textos de Cabezal | Descripciones del asiento completo |
| **FSX016** | Textos de Detalle | Descripciones por movimiento |

#### 🎯 FSD015 - Cabezal de Asiento (Control Maestro)

**Clave Compuesta**: Empresa* + Sucursal Origen* + Módulo* + Transacción* + Nro.relación* + Correl.asiento*

**Trazabilidad Completa**:
- **Control de ejecución**:
  - Usuario que ingresa + Estación de ingreso
  - Usuario que confirma + Estación confirma + Hora
  - Contabilizado: Estado del asiento
  
- **Control operativo**:
  - Caja Nro.: Terminal físico
  - Por Caja?: Operación de taquilla
  - Fecha valor contable + Fecha de contabilización

#### 📊 FSD016 - Detalle de Asiento (Movimientos Granulares)

**Clave Compuesta**: Empresa* + Sucursal Origen* + Módulo* + Transacción* + Nro.relación* + Ordinal* + Sub ordinal*

**Datos Operativos Completos**:
- **Identificación**: Módulo, Tipo Operac., Sucursal, Rubro, Moneda, Operación, Sub.operac.
- **Importes múltiples**: Importe movto., Importe 2, Importe 3, Importe M/Origen
- **Control temporal**: F/vto., F/valor, Plazo, Periodicidad
- **Condiciones financieras**: Tipo de tasa, Tasa, Tasa de mora, Tipo de días, Tipo de año
- **Características especiales**: Debe/Haber, Posición, Valuación, Código de papel

**Capacidad Excepcional**: Guarda 20 Tipos de Importe diferentes por movimiento.

---

## ⚙️ Datos de la Operación - Motor Operativo Central (Páginas 101-111)

### 🎪 Filosofía de Datos Operativos

**Analogía Central**: Los datos de operación funcionan como el **"Sistema Nervioso Central"** del banco, conectando cada transacción con todos los sistemas relacionados (contabilidad, saldos, eventos, documentos).

```
💼 TRANSACCIÓN CONTABILIZADA
    ↓ genera automáticamente
📊 SALDO CONTABLE (FSD011)
    ↓ si tiene módulo operativo
⚙️ OPERACIÓN (FSD010)
    ↓ puede generar
📅 EVENTOS PROGRAMADOS (FSD012/FSD601/FSD602)
    ↓ puede tener extensiones
📄 DOCUMENTOS (FSE012) + CHEQUES (FSE111) + INSTRUCCIONES (FSR111)
```

#### 📊 Arquitectura de Datos Operativos

| Tabla | Propósito | Scope | Automatización |
|-------|-----------|-------|----------------|
| **FSD011** | Saldos | Todos los movimientos | Automática |
| **FSD010** | Operaciones | Solo rubros con módulo | Automática condicional |
| **FSD601** | Operaciones a Plazo | Préstamos/Depósitos | Plan de pagos |
| **FSD602** | Eventos Plazo | Pagos de cuotas | Histórico de pagos |
| **FSD012** | Eventos | Programación futura | Calendario automático |
| **FSE012** | Documentos | Descontar/Cobrar | Gestión documental |
| **FSE111** | Cheques | Compensación | Control de plaza |
| **FSR111** | Instrucciones | Automatizaciones | Ejecución programada |

#### 💰 FSD011 - Saldos (Control Universal)

**Clave Compuesta**: Empresa* + Sucursal* + Rubro* + Moneda* + Papel* + Cuenta* + Operación* + SubOperación* + Tipo de Operación*

**Registro Integral**:
- **Identificación completa**: 9 dimensiones de clasificación
- **Control temporal**: Fecha Contabilización, Fecha Valor, Fecha Vencimiento, Fecha Ultimo Movimiento
- **Importes**: Saldo + Saldo en Dólares
- **Clasificación**: Plazo, Segmento Cliente, Función, Estado, Centro de Costos
- **Integración contable**: Título, Capítulo, Plazo, Grupo (Primer módulo)

#### ⚙️ FSD010 - Operaciones (Motor Financiero)

**Clave Compuesta**: Empresa* + Módulo* + Sucursal* + Moneda* + Papel* + Cuenta* + Operación* + SubOperación* + Tipo de Operación*

**Datos Financieros Completos**:
- **Calendario**: Fecha Valor, Fecha Vencimiento, Plazo
- **Condiciones**: Tipo de Tasa, Tasa, Tasa de Mora, Tipo Tasa de Corte, Tasa de Corte
- **Configuración**: Tipo de días, Tipo de año, Tipo de ajuste en vto., Tipo de cálculo de interés
- **Importes**: Importe, Intereses al Vencimiento
- **Control**: Status, Fecha de Baja, Afectada por IVA?, Aviso, Numerador de Eventos

#### 📅 FSD601 - Operaciones a Plazo (Plan de Pagos)

**Función**: Tabla de amortización automática para préstamos y depósitos a plazo.

**Clave Compuesta**: Empresa* + Módulo* + Sucursal* + Moneda* + Papel* + Cuenta* + Operación* + SubOperación* + Tipo de Operación* + Fecha de Pago Prevista* + Tipo de Cuota*

**Plan de Cuotas**:
- **Estructura temporal**: Desde Fecha, Hasta Fecha, Fecha de Pago Prevista
- **Composición**: Plazo Cuota, Capital Cuota, Interés Cuota
- **Impuestos**: Impuesto sobre Capital, Impuesto sobre Interés
- **Control**: Estado de la Cuota, Numerador de pagos, Fecha de Pago Inversa
- **Trazabilidad**: Clave del FSD016 que genera la extensión

#### 💳 FSD602 - Eventos Plazo (Histórico de Pagos)

**Función**: Registro de pagos reales contra plan previsto.

**Estructura de Pago Detallada**:
- **Fecha de Pago**: Real vs. Prevista
- **Descomposición del pago**: 
  - Cuotaparte pago a Capital, Interés, Interés Mora
  - Cuotaparte a impuesto de capital, interés, int.mora
- **Saldos remanentes**: 
  - Saldo de capital/interés/mora de cuota
- **Control**: Estado de la Cuota, Clave del FSD016 generador

#### 📋 FSD012 - Eventos (Programación Automática)

**Función**: Motor de eventos futuros automáticos (vencimientos, cálculos, recordatorios).

**Configuración de Eventos**:
- **Programación**: Nro. de Período, Fecha Vencimiento, Tipo Evento
- **Cálculos automáticos**: Tipo Tasa, Saldo de Capital, Saldo de Interés, Saldo de Mora
- **Procesamiento**: Cuotaparte de capital/interés/mora del pago
- **Estado**: ¿Contabilizado?, Clave del FSD016 generador

#### 📄 Extensiones Especializadas

**FSE012 - Documentos**: Gestión completa de documentos a descontar/cobrar
- **Identificación**: Nro. de Documento, Banco del Documento, Aceptante
- **Configuración**: Días para compensar/gestión, Vencimiento, Monto, Plaza
- **Condiciones**: Tipo Tasa del Documento, Tasa del Documento

**FSE111 - Cheques**: Control de compensación bancaria
- **Identificación**: Cheque, Banco, Sucursal del Banco, Plaza
- **Timing**: Días para Compensar, Fecha contabilización
- **Operativa**: Caja, Sucursal origen, Comisión

**FSR111 - Instrucciones**: Automatizaciones programadas
- **Configuración**: Código de instrucción, Rubro/Cuenta/Operación destino
- **Scope**: Empresa/Módulo/Sucursal/Moneda/Papel objetivo

---

## 📚 Sistema de Históricos - Memoria Institucional (Páginas 112-116)

### 🎪 Filosofía de Históricos

**Analogía Central**: El sistema de históricos de Bantotal funciona como la **"Biblioteca Nacional del Banco"** que preserva toda la información operativa para consultas, auditorías y análisis a largo plazo.

#### 🏗️ Arquitectura de Preservación

```
💾 DATOS OPERATIVOS DIARIOS
    ↓ procesos automáticos nocturnos
📚 HISTÓRICOS POR GRANULARIDAD
├── 📊 Por Operación (FSH014) - Máximo detalle
├── 📋 Por Rubro (FSH013) - Agregado contable  
├── 📈 Diarios (FSH031) - Mayores generales
├── 🎯 Movimientos (FSH015/FSH016) - Transacciones
└── 📊 Estadísticas (FSH017) - Análisis mensual
```

#### 📊 Catálogo de Históricos

| Tabla | Granularidad | Frecuencia | Uso Principal |
|-------|-------------|-------------|---------------|
| **FSH014** | Por Operación | Diaria | Estados de cuenta, mayores por cuenta |
| **FSH013** | Por Rubro | Diaria | Balances contables |
| **FSH031** | Saldos Diarios | Diaria | Mayores generales |
| **FSH015** | Cabezal Movimientos | Diaria | Auditoría de transacciones |
| **FSH016** | Detalle Movimientos | Diaria | Trazabilidad granular |
| **FSH017** | Estadísticas | Mensual | Análisis CC y CA, devengados |

#### 🎯 FSH014 - Saldos por Operación (Detalle Máximo)

**Clave Compuesta**: Empresa* + Sucursal* + Rubro* + Moneda* + Papel* + Cuenta* + Operación* + SubOperación* + Tipo de Operación* + Año*

**Propósito**: Punto de arranque para estados de cuenta y mayores por cuenta específica.

#### 📋 FSH013 - Saldos por Rubro (Agregación Contable)

**Clave Compuesta**: Empresa* + Sucursal* + Rubro* + Moneda* + Papel* + Año*

**Propósito**: Base para balances y reportes regulatorios consolidados.

#### 📈 FSH031 - Saldos Diarios (Mayores Generales)

**Clave Compuesta**: Fecha* + Empresa* + Sucursal* + Rubro* + Moneda* + Papel*

**Propósito**: Consulta de mayores generales por cualquier fecha específica.

#### 🔍 FSH015/FSH016 - Histórico de Movimientos

**Función**: Preservación completa de cabezales y detalles de transacciones.
- **FSH015**: Estructura idéntica a FSD015 (cabezales)
- **FSH016**: Estructura idéntica a FSD016 (detalles)

**Automatización**: Generación automática por procesos diarios.

#### 📊 FSH017 - Estadísticas (Análisis Mensual)

**Clave Compuesta**: Empresa* + Sucursal* + Rubro* + Moneda* + Papel* + Código de Papel* + Cuenta* + Operación* + SubOperación* + Tipo de Operación* + Año* + Mes*

**Aplicaciones**:
- Estadísticas de Cuentas Corrientes y Cajas de Ahorro
- Cálculo de devengados mensuales
- Análisis de comportamiento por cuenta

---

## 🔍 Motor Transaccional Completo - Integración Final (Páginas 91-94)

### 📋 Tablas Complementarias de Transacciones

#### ⚙️ FST062 - RTEs de la Transacción
**Función**: Configuración de Retenciones, Transferencias Electrónicas y reportes automáticos.

#### 💰 FST135 - Comisiones Múltiples
**Función**: Aplicación de múltiples comisiones en una sola transacción.
- **Aplicar a Tipo de Operación**: Scope específico
- **Modificable?**, **Diferible?**: Control de flexibilidad

#### 📋 FST037 - Instrucciones
**Función**: Automatizaciones programadas por transacción.
- **¿Obligatoria?**, **¿Aplicación diferida?**: Control de ejecución
- **¿Permite modificar cuenta?**: Flexibilidad operativa

#### 📝 Sistema de Textos e Impresos
- **FSX017/FSRX17**: Textos de transacción para impresos en Word
- **FST235**: Textos de ordinal para estados de cuenta
- **FST134**: Intervención de documentos para control documental

---

## 🛠️ Herramientas de Consulta - Acceso a Datos (Páginas 117-118)

### 🎯 Filosofía de Consulta

**Analogía**: Las herramientas de consulta funcionan como **"Llaves Maestras"** que permiten acceder a toda la información del banco de manera controlada y eficiente.

#### 🔧 Herramientas Disponibles

**QUERIES (AS/400)**:
- **RUNQRY**: Ejecutar consultas predefinidas
- **WRKQRY**: Crear y modificar consultas

**SQL Nativo**:
- **RUNSQL**: Ejecutar sentencias SQL directas
- **STRSQL**: Entorno interactivo SQL

**Herramientas Externas**:
- **MsQuery**: Integración con Microsoft Office

#### 🚀 Capacidades de Consulta

- **Acceso directo**: A todas las tablas del modelo
- **Flexibilidad total**: Desde consultas simples hasta análisis complejos
- **Integración**: Con herramientas externas de análisis
- **Tiempo real**: Consulta de datos operativos actuales

---

## 🛣️ Roadmap de Análisis

### ✅ Completado (Páginas 1-118) - ANÁLISIS COMPLETO
- [x] **Fundamentos conceptuales** (Páginas 1-14)
- [x] **Arquitectura GeneXus** (Páginas 1-14)
- [x] **Conceptos técnicos base** (Páginas 1-14)
- [x] **Sistema de nomenclatura** (Páginas 1-14)
- [x] **Tabla maestra FST017** (Páginas 1-14)
- [x] **Arquitectura multi-empresa** (Páginas 15-30)
- [x] **Configuración de sucursales** (Páginas 15-30)
- [x] **Datos del entorno** (Páginas 15-30)
- [x] **Sistema de calendarios** (Páginas 15-30)
- [x] **Gestión geográfica** (Páginas 15-30)
- [x] **Arquitectura de módulos** (Páginas 31-50)
- [x] **Sistema de operaciones** (Páginas 31-50)
- [x] **Sistema de clientes** (Páginas 31-50)
- [x] **Gestión de personas y cuentas** (Páginas 31-50)
- [x] **Sistema de clientes detallado** (Páginas 51-57)
- [x] **Plan de cuentas contable** (Páginas 58-63)
- [x] **Sistema de seguridad** (Páginas 64-70)
- [x] **Sistema de precios y pizarras** (Páginas 71-83)
- [x] **Definición de transacciones** (Páginas 84-90)
- [x] **Motor de asientos contables** (Páginas 95-100)
- [x] **Datos de la operación** (Páginas 101-111)
- [x] **Sistema de históricos** (Páginas 112-116)
- [x] **Herramientas de consulta** (Páginas 117-118)

### 🎉 **ANÁLISIS COMPLETO AL 100%**

### ⏳ Pendiente
- **¡ANÁLISIS COMPLETO!** - No hay páginas pendientes

### 🎯 Objetivos por Fase

#### ✅ Fase 1 Completada (Páginas 1-14)
- [x] Fundamentos conceptuales y arquitectónicos
- [x] Motor GeneXus y objetos principales
- [x] Conceptos técnicos base (tablas, claves, integridad)
- [x] Sistema de nomenclatura FST/FSD/FSR
- [x] Configuración maestra FST017

#### ✅ Fase 2 Completada (Páginas 15-30) 
- [x] **Arquitectura multi-empresa**: Estructura jerárquica de organizaciones
- [x] **Tabla FST717**: Árbol de empresas y dependencias
- [x] **Tabla FST001**: Configuración de sucursales y oficinas
- [x] **Numeradores automáticos**: FSN001, FSN002, FSN003
- [x] **Calendarios FST028**: Gestión de fechas hábiles por región
- [x] **Geografía**: FST013 (Países), FST069 (Regiones), FST068 (Localidades)
- [x] **Aplicaciones prácticas**: Consolidación, reportes, gestión operativa

#### ✅ Fase 3 Completada (Páginas 31-50)
- [x] **Arquitectura de módulos**: FST003 (Módulos), FST004 (Tipos de Operación)
- [x] **Sistemas operacionales**: FST110 (Sistemas), FST111 (Módulos de Sistema)
- [x] **Catálogo operativo**: 20+ módulos identificados (Préstamos, Cuentas, Inversiones)
- [x] **Tipos de operación**: Variantes específicas por módulo
- [x] **Sistema de clientes**: Personas, Cuentas, Grupos
- [x] **Identificación internacional**: Documentos multi-país
- [x] **Jerarquías de clientes**: Grupos económicos y clasificaciones

#### ✅ Fase 4 Completada (Páginas 51-70)  
- [x] **Sistema de clientes detallado**: 8 tablas FSD catalogadas (Personas, Cuentas, Domicilios)
- [x] **Relaciones FSR**: 6 tablas de vínculos (Cónyuges, Teléfonos, Integración)
- [x] **Calificadores FST**: 12 tablas de clasificación (Documentos, Riesgo, Sectores)
- [x] **Plan de cuentas**: FSD014 (Rubros), FSD013 (Primer Módulo), FSR014 (Relaciones)
- [x] **Motor contable**: Reglas de imputación automática y control de operaciones
- [x] **Sistema de seguridad**: 6 tablas de control (Usuarios, Permisos, Excepciones)
- [x] **Perfiles de autorización**: Gestión masiva de accesos por roles

#### ✅ Fase 5 Completada (Páginas 71-90)  
- [x] **Sistema de precios**: Pizarras de tipos de cambio, comisiones y tasas
- [x] **Tipos de cambio**: FST005 (Monedas) + FSH005 (Cotizaciones históricas)
- [x] **Especies**: FST205/FSH205 para valores y papeles financieros
- [x] **Comisiones**: Sistema jerárquico (genéricas → específicas por cuenta)
- [x] **Tasas**: Motor de 3 niveles (clase → monto → cuenta específica)
- [x] **Pizarras dinámicas**: Matrices multidimensionales (monto × plazo × cliente)
- [x] **Definición de transacciones**: ADN operativo (cabezal → ordinales → cálculos)
- [x] **Motor de cálculos**: Lógica automática y validaciones inteligentes

#### ✅ Fase 6 Completada (Páginas 91-118) - ¡FINAL!
- [x] **Motor de asientos**: Notario automático con trazabilidad completa (FSD015/FSD016)
- [x] **Datos de operación**: Sistema nervioso central del banco (8 tablas operativas)
- [x] **Saldos universales**: FSD011 con 9 dimensiones de clasificación
- [x] **Operaciones financieras**: FSD010 con condiciones completas
- [x] **Plan de pagos**: FSD601/FSD602 con amortización automática
- [x] **Eventos programados**: FSD012 con calendario automático
- [x] **Extensiones especializadas**: Documentos, Cheques, Instrucciones
- [x] **Sistema de históricos**: Biblioteca nacional del banco (6 tablas FSH)
- [x] **Herramientas de consulta**: Acceso total con QUERIES y SQL

### 🏆 **¡ANÁLISIS COMPLETO AL 100%!**
#### ⏳ Fase 6 (Páginas 91-118)
- [ ] Casos de uso prácticos
- [ ] Ejemplos de implementación
- [ ] Mejores prácticas operativas
- [ ] Troubleshooting y mantenimiento

---

## 🎯 Hallazgos Principales - Análisis Completo (Páginas 1-118)

### 🏆 **Descubrimiento Fase 1 (1-14): Fundamentos Arquitectónicos**

**Bantotal + GeneXus** = **"Traductor automático"** de ideas bancarias a código ejecutable
- ✅ Nomenclatura universal FST/FSD/FSR/etc.
- ✅ Patrón de 9 campos base
- ✅ Tabla maestra FST017

### 🌐 **Descubrimiento Fase 2 (15-30): Ecosistema Multi-empresa**

**Bantotal = "AWS para Bancos"** - Plataforma de ecosistema financiero completo
- ✅ Arquitectura híbrida (infraestructura compartida + datos segregados)
- ✅ 7 tablas FST de configuración geográfica y organizacional
- ✅ Numeradores automáticos sin colisiones

### 🔧 **Descubrimiento Fase 3 (31-50): Motor Operacional**

**Bantotal = "Sistema Operativo Bancario"** con arquitectura modular inteligente

#### 🎭 **Módulos con Doble Personalidad**
- 🏢 **Sectores Operativos**: Organización departamental (Cajas, Inversiones)
- ⚙️ **Operativas Específicas**: Reglas de negocio (Préstamos Francés vs. Alemán)

#### 🏗️ **Jerarquía Operacional de 3 Niveles**
```
🌐 SISTEMA → 🔧 MÓDULO → 📋 TIPO DE OPERACIÓN
```

#### 🏦 **Sistema de Clientes Universal**
- 👤 **Personas**: Físicas/Jurídicas con identificación internacional
- 🏦 **Cuentas**: Números internos con asociación flexible
- 🎯 **Grupos**: Clasificación para tratamiento estratégico

### 🏗️ **Descubrimiento Fase 4 (51-70): Arquitectura de Datos y Control**

**Bantotal = "Cerebro Bancario"** con sistemas de datos, contabilidad y seguridad interconectados

#### 🧠 **Red Social Bancaria**
- 📊 **8 tablas FSD de clientes**: Arquitectura completa de personas y cuentas
- 🔗 **6 tablas FSR de relaciones**: Vínculos complejos (cónyuges, socios, telefonos)
- 🏷️ **12 tablas FST calificadores**: Clasificación automática regulatoria y comercial

#### 📊 **GPS Contable Automático**
- 🎯 **FSD014 Plan de Cuentas**: Motor de imputación inteligente
- 🏗️ **FSD013 Primer Módulo**: Organización jerárquica contable
- 🔗 **FSR014 Relaciones**: Sinapsis contables que conectan cuentas automáticamente

#### 🛡️ **Sistema de Credenciales Inteligente** 
- 👥 **6 tablas de seguridad**: Control granular de acceso (Usuario → Módulo → Transacción → Excepción)
- 🎭 **Perfiles de autorización**: Plantillas organizacionales escalables
- 🚨 **Trazabilidad total**: Auditoría completa con timestamp y responsabilidad

### 💰 **Descubrimiento Fase 5 (71-90): Motor Financiero Automático**

**Bantotal = "Bolsa de Valores Interna"** con sistema de precios y transacciones completamente automatizado

#### 📊 **Pizarras Inteligentes Multidimensionales**
- 💱 **Tipos de cambio**: Cotizaciones automáticas con histórico (FST005 + FSH005)
- 🎭 **Especies**: Instrumentos financieros complejos (bonos, valores, papeles)
- 💵 **Comisiones jerárquicas**: Genéricas → Específicas por cuenta
- 📈 **Tasas multinivel**: Clase → Monto → Plazo → Cuenta específica

#### 🔧 **ADN Operativo de Transacciones**
- 🎯 **Cabezal**: Configuración operativa completa (FST034)
- 📋 **Ordinales**: Campos de captura inteligentes (FST035)
- 🔢 **SubOrdinales**: Asientos contables automáticos (FST036)
- ⚙️ **Cálculos**: Motor de lógica y validaciones (FST040)

#### 🚀 **Automatización Financiera Total**
- **Escalas dinámicas**: Tasas automáticas por volumen, plazo y perfil de cliente
- **Jerarquía de precios**: Sistema que busca desde específico hasta genérico
- **Motor de cálculos**: Validaciones y operaciones automáticas en tiempo real
- **Trazabilidad de precios**: Histórico completo de cotizaciones y cambios

### 📚 **Descubrimiento Fase 6 (91-118): Sistema Nervioso Central**

**Bantotal = "Notario + Biblioteca + Sistema Nervioso"** integrado que preserva, procesa y conecta toda la información bancaria

#### 📝 **Notario Automático (Asientos)**
- 🎯 **FSD015/FSD016**: Registro contable con trazabilidad irrefutable
- 📝 **FSX015/FSX016**: Documentación automática de movimientos
- 🕐 **Control temporal**: Timestamp completo (ingreso, confirmación, contabilización)
- 👥 **Trazabilidad humana**: Usuario + Estación por cada acción

#### ⚙️ **Sistema Nervioso Central (Datos de Operación)**
- 💰 **FSD011 Saldos**: Registro universal con 9 dimensiones de clasificación
- ⚙️ **FSD010 Operaciones**: Motor financiero con condiciones completas
- 📅 **FSD601/FSD602 Eventos**: Plan de pagos y amortización automática
- 🔄 **FSD012 Eventos**: Calendario automático de vencimientos y cálculos
- 📄 **Extensiones FSE**: Especialización por tipo (Documentos, Cheques)
- 🔧 **Instrucciones FSR111**: Automatizaciones programadas

#### 📚 **Biblioteca Nacional del Banco (Históricos)**
- 🎯 **FSH014**: Saldos por operación (máximo detalle)
- 📋 **FSH013**: Saldos por rubro (balances)
- 📈 **FSH031**: Saldos diarios (mayores generales)
- 🔍 **FSH015/016**: Movimientos completos (auditoría)
- 📊 **FSH017**: Estadísticas mensuales (análisis)
- 🤖 **Automatización**: Procesos nocturnos de preservación

#### 🔍 **Llaves Maestras (Herramientas)**
- **QUERIES**: Consultas predefinidas (RUNQRY, WRKQRY)
- **SQL**: Acceso directo a datos (RUNSQL, STRSQL)
- **Integración**: Herramientas externas (MsQuery)

### 🎯 **Arquitectura Completa Revelada - MODELO INTEGRAL**

**80+ tablas estructurales catalogadas en 6 sistemas integrados**:

```
🏗️ BANTOTAL = "SISTEMA OPERATIVO BANCARIO COMPLETO"
├── 🧠 Fundamentos (GeneXus + Nomenclatura universal)
├── 🌐 Multi-empresa (AWS para bancos)
├── ⚙️ Motor operacional (20+ módulos bancarios)
├── 🛡️ Cerebro bancario (datos + contabilidad + seguridad)
├── 💰 Bolsa interna (precios + transacciones automáticas)
└── 📚 Sistema nervioso (asientos + operaciones + históricos + consultas)
```

**Dominios Funcionales Completos**:
- 💰 **Captación**: Cuentas Corrientes, Ahorros, Plazo Fijo
- 💸 **Colocación**: Préstamos, Descuentos, Personales  
- 🏦 **Servicios**: Cajas, Inversiones, Comercio Exterior
- 📊 **Contabilidad**: Plan automático + Asientos + Históricos
- 🔒 **Seguridad**: Control multinivel + Excepciones + Auditoría
- 💰 **Precios**: Pizarras dinámicas + Jerarquías + Históricos
- 🔧 **Operaciones**: ADN transaccional + Datos + Eventos + Extensiones
- 📚 **Preservación**: Históricos + Consultas + Análisis

### 🚀 **Implicaciones Estratégicas Definitivas**

1. **Escalabilidad Infinita**: Multi-empresa + Multi-país + Multi-módulo + Multi-usuario + Multi-moneda + Multi-instrumento
2. **Automatización Total**: Contabilidad + Clasificación + Precios + Cálculos + Eventos + Preservación automáticas
3. **Compliance Absoluto**: Trazabilidad + Segregación + Control + Auditoría + Históricos + Evidencia digital
4. **Flexibilidad Extrema**: Configuración granular desde empresa hasta campo de transacción específica
5. **Inteligencia Financiera**: Precios dinámicos + Jerarquías + Eventos programados + Cálculos en tiempo real
6. **Memoria Institucional**: Preservación automática + Consultas flexibles + Análisis histórico + Estadísticas

### 📊 **Métricas Finales del Análisis - 100% COMPLETADO**
- ✅ **118 páginas analizadas** de 118 total (**100% COMPLETADO**)
- ✅ **80+ tablas catalogadas** en 10 sistemas integrados  
- ✅ **40+ tablas FST** (configuración, tipos, calificadores, transacciones)
- ✅ **25+ tablas FSD** (datos operativos, clientes, precios, asientos, operaciones)
- ✅ **15+ tablas FSR** (relaciones, vínculos, pizarras, instrucciones)
- ✅ **10+ tablas FSH** (históricos, cotizaciones, movimientos, estadísticas)
- ✅ **5+ tablas FSE** (extensiones especializadas)
- ✅ **5+ tablas FSX** (textos y documentación)
- ✅ **3 tablas FSN** (numeradores automáticos)
- ✅ **6 fases completadas** de 6 totales
- ✅ **20+ módulos** operacionales identificados
- ✅ **4 niveles** de seguridad mapeados
- ✅ **5 sistemas** de precios integrados
- ✅ **8 tipos** de extensiones operativas
- ✅ **6 tipos** de históricos automáticos

### 🏆 **LOGRO FINAL**

**Bantotal revelado como el "SISTEMA OPERATIVO BANCARIO MÁS COMPLETO"** - Una plataforma integral que combina:
- **Inteligencia** (automatización total)
- **Flexibilidad** (configuración granular)
- **Seguridad** (control multinivel)
- **Escalabilidad** (multi-todo)
- **Memoria** (preservación automática)
- **Transparencia** (trazabilidad completa)

Un sistema diseñado para bancos que aspiran a ser **líderes tecnológicos** en el siglo XXI.

---

## 🔗 Referencias y Fuentes

### 📄 Documento Principal
- **Título**: Estructura del Modelo de Datos Bantotal
- **Autor**: Alejandro Danielián
- **Empresa**: De Larrobla & Asociados (DLYA)
- **Fecha Original**: 25 de abril de 2001
- **Última Modificación**: 19 de junio de 2025
- **Herramienta**: Acrobat PDFMaker 11 para PowerPoint

### 🛠️ Herramientas de Análisis
- **pdf-processing-pro**: Extracción y procesamiento de contenido PDF
- **bt-sql-analyzer**: Análisis especializado de estructuras Bantotal
- **Patrón de 9 campos**: Arquitectura estándar identificada en documentación

### 📚 Contexto Histórico
- **Bantotal**: Sistema bancario desarrollado por De Larrobla & Asociados
- **GeneXus**: Herramienta de desarrollo automático de aplicaciones
- **Capacitación**: Documento parte de programa de entrenamiento técnico

---

## 📝 Notas de Metodología

### 🔍 Proceso de Análisis
1. **Extracción**: Uso de pdf-processing-pro para contenido estructurado
2. **Interpretación**: Análisis contextual y técnico
3. **Correlación**: Conexión con patrones de bt-sql-analyzer
4. **Documentación**: Consolidación en formato markdown

### 🎯 Enfoque Didáctico
- **Analogías**: Conceptos técnicos explicados con ejemplos cotidianos
- **Progresión**: De conceptos simples a complejos
- **Práctica**: Orientado a implementación real
- **Referencias**: Enlaces cruzados entre conceptos

---

*Documento generado automáticamente mediante análisis de PDF especializado*  
*Fases 1-5 completadas usando pdf-processing-pro + bt-sql-analyzer*  
*Última actualización: Octubre 2025 - Páginas 1-90 analizadas (76% completado)*
