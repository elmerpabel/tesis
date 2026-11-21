# 🎓 Skill `tesis` — Tu Tesis, de Cero a Lista, en una Sola Conversación 🔥

[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-blue.svg)](LICENSE)
[![Compatible con Antigravity](https://img.shields.io/badge/Antigravity-Skill%20Oficial-6C47FF.svg)](SKILL.md)
[![Para Cualquier Profesión](https://img.shields.io/badge/Disciplinas-Todas%20las%20Profesiones-00A86B.svg)](#-adaptable-a-cualquier-profesión)

**`tesis`** es un *skill* abierto y reutilizable para **Antigravity** (y agentes compatibles con el estándar `SKILL.md`) que transforma tu conversación en un **comité académico de élite** capaz de estructurar, diseñar, redactar y planificar tu proyecto de tesis de **pregrado, maestría, doctorado o titulación profesional** en **6 fases secuenciales**, adaptable a **cualquier carrera o disciplina**.

---

## 💖 Apoya este Proyecto (Donación Voluntaria)

Si este *skill* te ayudó a estructurar tu tesis, ahorrar semanas de trabajo metodológico o preparar tu sustentación, considera apoyar su mantenimiento y mejora continua con una donación voluntaria a través de **PayPal**:

<p align="center">
  <a href="https://www.paypal.com/donate/?hosted_button_id=CJ8FZVFZ3QVTS" target="_blank" rel="noopener noreferrer">
    <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="Donar con PayPal" title="PayPal - The safer, easier way to pay online!" />
  </a>
</p>

También puedes abrir o incrustar directamente el formulario oficial de donación disponible en [`donate.html`](donate.html):

```html
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="hosted_button_id" value="CJ8FZVFZ3QVTS" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_PE/i/scr/pixel.gif" width="1" height="1" />
</form>
```

---

## 🧠 El Comité Académico de Élite

Cada sesión del skill activa cuatro perfiles especializados trabajando de manera integrada:

1. **Metodólogo PhD:** Rigor científico, coherencia epistemológica, Matriz de Consistencia y validez del diseño.
2. **Estadístico:** Análisis cuantitativo, cualitativo y mixto, operacionalización de variables, muestreo y pruebas estadísticas.
3. **Redactor Académico (Scopus / WoS):** Estilo científico formal, precisión terminológica, transiciones fluidas y citación normativa (APA 7, IEEE, Vancouver, ISO 690, Chicago).
4. **Asesor Estratégico (+500 tesis aprobadas):** Viabilidad real, defensa ante jurado evaluador (criterios de Golding, 2017) y prevención de errores de rechazo.

---

## 🧭 Metodología Completa en 6 Fases

| Fase | Nombre | Entregables Clave |
| :--- | :--- | :--- |
| **Fase 1** | **Diagnóstico y arquitectura conceptual** | Evaluación de viabilidad, 3 enfoques alternativos, definición quirúrgica del problema, pregunta central y secundarias, hipótesis principal/alternativas, objetivos con taxonomía de Bloom y Matriz de Consistencia. |
| **Fase 2** | **Arquitectura estructural completa** | Índice completo capítulo por capítulo con subcapítulos, extensión recomendada en páginas por sección e hilo conductor narrativo. |
| **Fase 3** | **Marco teórico y estado del arte** | Teorías principales, autores clave y corrientes indispensables, estructura del marco teórico lista para desarrollar y ecuaciones booleanas para Scopus / WoS / SciELO / Latindex / Consensus / Scite. |
| **Fase 4** | **Diseño metodológico** | Enfoque (cuantitativo, cualitativo o mixto) justificado, tipo, diseño, población, muestra, instrumentos (validez y confiabilidad), Matriz de Operacionalización y plan paso a paso de recolección y análisis. |
| **Fase 5** | **Redacción del Capítulo 1 completo** | Introducción, planteamiento del problema, justificación, objetivos y delimitación listos para entregar en lenguaje académico formal con transiciones fluidas. |
| **Fase 6** | **Hoja de ruta final** | Cronograma semana por semana, presupuesto referencial, fuentes primarias recomendadas en la norma solicitada, guía anti-rechazo y guion de sustentación (Regla 6x6). |

---

## 🌍 Adaptable a Cualquier Profesión

| Disciplina / Carrera | Normas Sugeridas | Diseños Habituales |
| :--- | :--- | :--- |
| **Ingenierías** (Industrial, Civil, Sistemas, Metalúrgica, Minas, Mecánica, Eléctrica, Ambiental) | APA 7 / IEEE / ISO 690 | Experimental, optimización, simulación, propuesta técnico-económica |
| **Ciencias de la Salud** (Medicina, Enfermería, Odontología, Farmacia, Nutrición) | Vancouver / APA 7 | Observacional analítico, transversal, casos-controles, cohortes |
| **Administración, Economía, Contabilidad y Marketing** | APA 7 | Correlacional, descriptivo-propositivo, econométrico, estudio de caso |
| **Educación y Psicología** | APA 7 | Cuasi-experimental, correlacional, investigación-acción, fenomenológico |
| **Derecho y Ciencias Políticas** | APA 7 / Chicago / ISO 690 | Dogmático-jurídico, socio-jurídico, análisis jurisprudencial comparado |
| **Arquitectura, Diseño y Comunicaciones** | APA 7 / ISO 690 | Proyectual, descriptivo-propositivo, análisis espacial/comunicacional |

---

## 📂 Organización Automática de Proyectos (`000_Tesis_Antigravity_<Acronimo>`)

El script [`scripts/create_tesis_folder.py`](scripts/create_tesis_folder.py) crea automáticamente carpetas enumeradas correlativamente para cada solicitud de tesis (tanto en modo **local** como integrado con **Google Drive**):

```text
001_Tesis_Antigravity_EHuayna/
├── 01_Estructura_y_Borradores/       # Documento maestro (6 fases), Matrices y Capítulo 1
├── 02_Marco_Teorico_y_Referencias/   # Bases teóricas, antecedentes y bibliografía
├── 03_Metodologia_y_Datos/           # Diseño metodológico, instrumentos y guías de análisis
├── 04_Presentaciones/                # Guiones y diapositivas de sustentación (Regla 6x6)
└── 05_Cronograma_y_Entregables/      # Cronograma semanal, presupuesto y checklist anti-rechazo
```

---

## 🚀 Instalación y Uso Rápido

### 1. Clonar el repositorio
```bash
git clone https://github.com/elmerpabel/tesis.git
cd tesis
```

### 2. Instalar como Skill en Antigravity (o agente compatible con `SKILL.md`)
Copia o registra la carpeta del repositorio en tu directorio de skills:
```bash
mkdir -p ~/.agents/skills/tesis
cp -r SKILL.md references scripts templates ~/.agents/skills/tesis/
```
O desde Antigravity, guarda el directorio clonado usando la gestión de skills con el nombre `tesis`.

### 3. Crear una carpeta de proyecto de tesis
**Modo local (sin dependencias externas, funciona en cualquier equipo con Python 3.10+):**
```bash
python3 scripts/create_tesis_folder.py --full-name "Elmer Huayna" --local-dir ./tesis_output
# Crea: ./tesis_output/001_Tesis_Antigravity_EHuayna/
```

**Modo Google Drive (opcional, requiere CLI `gdrive` y `gdocs` configurados):**
```bash
export TESIS_DRIVE_OUTPUT_FOLDER_ID="<TU_ID_CARPETA_DRIVE>"
python3 scripts/create_tesis_folder.py --acronym "EHuayna"
```

### 4. Invocar el Skill con tu Información Base
Pega tu información base en el chat (ver plantilla en [`templates/01_ficha_base.md`](templates/01_ficha_base.md)):

```text
Usa el skill tesis con la siguiente información base:
- Tesista: María López (MLopez)
- Nivel académico: Pregrado
- Área de conocimiento: Ingeniería Industrial
- Tema o idea inicial: Optimización de tiempos de ciclo en líneas de empaque mediante Lean Manufacturing
- Universidad e institución: Universidad Nacional de Ingeniería
- Normas de citación requeridas: APA 7ª edición
- Número de páginas aproximado: 90 - 110 páginas
- Tiempo disponible para completarla: 16 semanas
```

---

## 📁 Estructura del Repositorio

```text
tesis/
├── SKILL.md                              # Definición oficial del skill para Antigravity / agentes
├── README.md                             # Documentación principal y botón de donación PayPal
├── donate.html                           # Página HTML con el formulario oficial de donación PayPal
├── LICENSE                               # Licencia MIT
├── references/
│   ├── methodology_guide.md              # Metodología científica, Causa-Problema-Efecto-Solución y ética IA
│   ├── bloom_and_matrices.md             # Taxonomía de Bloom, Matrices y guía por profesión
│   └── presentation_guide.md             # Regla 6x6 y guía de visualización científica para sustentación
├── templates/
│   ├── 01_ficha_base.md                  # Plantilla de ficha de entrada del tesista
│   ├── 02_matriz_consistencia.md         # Plantilla de Matriz de Consistencia y Operacionalización
│   └── 03_capitulo_1_plantilla.md        # Plantilla académica del Capítulo 1
└── scripts/
    ├── create_tesis_folder.py            # Creador automático de carpetas 000_Tesis_Antigravity_<Acronimo>
    └── export_to_gdocs.py                # Exportador opcional de Markdown a Google Docs
```

---

## ⚖️ Uso Ético y Responsabilidad Académica

Este *skill* está diseñado como un **asistente metodológico y estructural**. Toda investigación académica rigurosa exige que el tesista:
- Verifique personalmente cada cita, autor, año y DOI en bases indexadas reales (Scopus, Web of Science, SciELO, PubMed, IEEE Xplore).
- Recolecte y analice datos empíricos reales (el skill marca cualquier dato faltante como `[DATO PENDIENTE]` y nunca inventa resultados).
- Revise la redacción final conforme al reglamento y políticas de originalidad/antiplagio de su universidad.

---

## 📄 Licencia

Distribuido bajo licencia **MIT**. Libre para usar, adaptar y compartir en cualquier universidad o profesión. Si te resulta útil, recuerda dejar una estrella ⭐ en GitHub o apoyar el proyecto vía [PayPal](https://www.paypal.com/donate/?hosted_button_id=CJ8FZVFZ3QVTS).
