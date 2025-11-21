# Laboratorio Final — Profundización I en Inteligencia Artificial  
**Universidad de Manizales — Ingeniería de Sistemas y Telecomunicaciones**  
**Estudiantes:** Tomás Marín Toro, Daniel Cortes Valencia, Valentina Arango Mendieta, Juan Esteban Marín
**Curso:** Profundización I — Inteligencia Artificial  
**Docente:** PhD. Carlos Betancourt Correa  

---

# Sobre este Repositorio

Este repositorio contiene **todas las actividades desarrolladas en el Laboratorio Final de Profundización I – Inteligencia Artificial**, siguiendo los lineamientos del documento oficial.

Aquí se incluyen **todas las actividades del Paso 2 (Actividades detalladas por plataforma)**, además de los entregables requeridos como notebooks, análisis técnicos, comparaciones, prototipos funcionales y evidencias.

Las actividades cubren las siguientes plataformas y herramientas:

### 🧩 Actividades del Laboratorio  
✔ **2.1 — Hugging Face (NLP, Visión, Audio + Space público)**  
✔ **2.2 — NotebookLM (análisis de documentos)**  
✔ **2.3 — Google AI Studio (prompts técnicos y creativos)**  
✔ **2.4 — Kaggle (EDA + notebook publicado)**  
✔ **2.5 — Perplexity AI (consulta avanzada + validación de fuentes)**  
✔ **2.6 — Papers With Code (reproducción de experimento)**  
✔ **2.7 — Replicate (modelos generativos + consumo por API)**  
✔ **2.8 — Modelscope (modelo alternativo + comparación)**  
✔ **2.9 — LLaMaIndex (pipeline RAG + base de conocimiento)**  
✔ **2.10 — GitHub Copilot (módulo generado + comparación)**  
✔ **2.11 — Codeium (función + refactorización + contraste)**  
✔ **2.12 — Replit AI (microproyecto con IA)**  
✔ **2.13 — Claude Code (análisis de repositorio + mejoras)**  
✔ **2.14 — Devin AI (análisis conceptual)**  

Cada carpeta contiene:

- Notebook ejecutado  
- Archivos del modelo / script  
- Imágenes de evidencia  
- README explicativo  
- Conclusiones técnicas  
- Archivos adicionales (PDF, datasets, códigos)

Además, el repositorio incluye:

### 📁 Estructura General  
- `/huggingface/`  
- `/notebooklm/`  
- `/google_ai_studio/`  
- `/kaggle/`  
- `/perplexity/`  
- `/papers_with_code/`  
- `/replicate/`  
- `/modelscope/`  
- `/llamaindex/`  
- `/copilot/`  
- `/codeium/`  
- `/replit/`  
- `/claude/`  
- `/devin/`  
- `/integrador/`

---

Este repositorio cumple con los requisitos del laboratorio final:  
documentación profesional, evidencias completas, análisis crítico y organización clara para evaluación.

---

# Estructura de Este Repositorio (Mi Parte)

Lab_Final_IA
├── README.md ← Actividad 1 (tabla comparativa)
├── kaggle/ ← Actividad 5
├── modelscope/ ← Actividad 9
├── replit/ ← Actividad 13
├── capturas/ ← Evidencias individuales
└── informes/ ← PDF, reportes y análisis


---

#  **Actividad 1 — Tabla Comparativa de Plataformas IA**

A continuación se presenta la tabla comparativa profesional solicitada en el criterio #1 de la rúbrica.  
La tabla analiza las plataformas globales utilizadas en el laboratorio, destacando su descripción técnica, ventajas, limitaciones y escenarios de uso.

---

#  Tabla Comparativa de Plataformas IA — Laboratorio Final

| Plataforma | Descripción Técnica | Ventajas | Desventajas | Escenarios de Uso | Complejidad | Recomendación |
|-----------|----------------------|----------|--------------|--------------------|--------------|----------------|
| **Hugging Face** | Ecosistema open-source más grande de modelos IA (LLM, visión, audio, embeddings). Incluye Transformers, Datasets y Spaces para demos. | Miles de modelos, comunidad grande, Spaces públicos. | Requiere GPU para modelos grandes. | Chatbots, clasificadores, embeddings, demos. | Media | Úsala para proyectos IA open-source y demos técnicas. |
| **Google NotebookLM** | Asistente IA que trabaja únicamente con documentos cargados. | Respuestas basadas en tus fuentes. | Limitado a documentos cargados. | Resúmenes, análisis de papers, estudio técnico. | Baja | Ideal para investigación y análisis académicos. |
| **Google AI Studio** | Plataforma para crear prompts y agentes con modelos Gemini. Ajuste de temperatura, top-k, etc. | Excelente para ingeniería de prompts. | Funciones avanzadas requieren Cloud. | Agentes, análisis de prompts, prototipos. | Media | Úsala para diseñar prompts técnicos/creativos. |
| **Kaggle** | Plataforma líder en datasets, notebooks y EDA con GPU gratuita. | Muchísimos datasets, GPU gratis, comunidad. | Límites de tiempo en GPU. | EDA, ML rápido, visualizaciones. | Media-Alta | Perfecta para análisis estadístico y modelos rápidos. |
| **Perplexity AI** | Buscador con IA y citación verificable. | Fuentes reales, verificación académica. | A veces menos profundo que Scholar. | Estado del arte, búsquedas técnicas. | Baja | Úsala para investigación con evidencia. |
| **Papers With Code** | Conecta papers con implementación oficial. | Permite replicar experimentos reales. | No todos los papers tienen repos actualizados. | Benchmarking, investigación avanzada. | Alta | Úsala para replicar papers y analizar modelos. |
| **Replicate** | Ejecuta modelos generativos vía API sin GPU propia. | API simple, modelos variados. | Algunos modelos cuestan; latencia. | Imagen, video, voz, prototipos. | Baja-Media | Excelente para prototipos generativos rápidos. |
| **Modelscope (Alibaba)** | Alternativa optimizada en visión, voz y NLP. | Modelos ligeros y eficientes. | Comunidad menor que HF. | Visión, voz, NLP optimizado. | Media | Úsala para comparar rendimiento con HuggingFace. |
| **LLaMaIndex** | Framework especializado para RAG y bases de conocimiento. | Muy potente para chat con documentos. | Requiere conocer pipelines de RAG. | Asistentes privados, chat con PDFs. | Media-Alta | Ideal para sistemas con grounding real. |
| **GitHub Copilot** | Asistente para programar integrado en VS Code. | Genera funciones, explica, refactoriza. | Puede generar errores si no se revisa. | Desarrollo de software, documentación. | Baja-Media | Úsala para acelerar codificación. |
| **Codeium** | Asistente gratuito para completar y explicar código. | Gratis, muy bueno explicando. | Menos preciso en proyectos grandes. | Refactorización, funciones rápidas. | Baja | Excelente opción gratuita de asistencia. |
| **Replit AI / Ghostwriter** | IDE en la nube que genera proyectos completos con IA. | Crea apps instantáneas. | A veces genera estructura desordenada. | Prototipos, APIs rápidas. | Baja-Media | Úsala para crear microproyectos en minutos. |
| **Claude Code** | IA que actúa como ingeniero colaborador (documenta, revisa repos, genera módulos). | Excelente para repos grandes. | No ejecuta código dentro del entorno. | Documentación, análisis de repos, mejoras. | Media-Alta | Úsala para proyectos complejos y documentación. |
| **Devin AI (conceptual)** | Primer prototipo de “ingeniero autónomo” capaz de ejecutar pipelines y debugging. | Visión del futuro de la IA. | No listo para producción. | Análisis ético y de tendencias. | Alta | Úsalo solo para análisis conceptual. |

# 🧩 Actividades del Laboratorio — Sección 2 (Plataformas IA)

Esta sección describe cada una de las actividades detalladas del PASO 2 del laboratorio, siguiendo el documento oficial del curso.  
Cada actividad trabaja una plataforma, metodología o herramienta distinta, generando evidencias completas, análisis técnicos y entregables específicos.

---

## **2.1 — Hugging Face (Modelos y Datasets)**
Exploración de modelos de NLP, visión y audio utilizando la librería Transformers y Spaces.

**Desarrollo realizado:**
- Se probaron 3 modelos distintos:
  - NLP: Sentiment Analysis (DistilBERT)
  - Visión: ResNet-50
  - Audio: Whisper Tiny
- Se ejecutó un modelo descargado en notebook.
- Se creó un Space público usando Gradio.

**Entregables:**
- Notebook ejecutado.
- Link del Space público.
- Capturas de inferencias.
- Análisis técnico del modelo (arquitectura, rendimiento, limitaciones).

---

## **2.2 — NotebookLM (Notebooks Inteligentes)**
Asistente basado en documentos para análisis profundo de contenido técnico.

**Desarrollo realizado:**
- Carga de un documento técnico.
- Generación de 5 preguntas argumentativas.
- Elaboración de un resumen automatizado.
- Evaluación de sesgos y consistencia en las respuestas.

**Entregables:**
- Capturas del notebook.
- Exportación del resumen generado.
- PDF con análisis crítico.

---

## **2.3 — Google AI Studio (Prompt Engineering)**
Plataforma para crear agentes y ajustar prompts con modelos Gemini.

**Desarrollo realizado:**
- Creación de dos prompts:
  - Uno técnico.
  - Uno creativo.
- Iteración con ajustes de temperatura, top-k y top-p.
- Comparación de resultados y análisis del comportamiento del modelo.

**Entregables:**
- Capturas del proceso.
- Archivo comparativo de iteraciones.
- Reflexión técnica.

---

## **2.4 — Kaggle (EDA + Colaboración)**
Exploración y análisis de datos usando notebooks ejecutables y datasets reales.

**Desarrollo realizado:**
- Selección del dataset “Student Mental Health”.
- Limpieza, análisis estadístico y generación de visualizaciones.
- Publicación del notebook en Kaggle.
- Relación del dataset con un caso educativo.

**Entregables:**
- Notebook público de Kaggle.
- PDF del EDA.
- README en GitHub con explicación.

---

## **2.5 — Perplexity AI (Asistente de Investigación)**
Motor de búsqueda con IA que proporciona fuentes verificables.

**Desarrollo realizado:**
- Consulta técnica compleja.
- Validación manual de 5 fuentes proporcionadas.
- Comparación de resultados con Google Scholar.

**Entregables:**
- Capturas de consulta.
- Reporte de validación de fuentes.
- Conclusiones escritas.

---

## **2.6 — Papers With Code**
Relación entre literatura científica y código replicable.

**Desarrollo realizado:**
- Selección de un paper con código reproducible.
- Ejecución parcial del experimento.
- Comparación entre resultados obtenidos y los del paper.

**Entregables:**
- Notebook con ejecución.
- Informe técnico de replicación.
- Gráficas comparativas.

---

## **2.7 — Replicate (Modelos Generativos)**
Ejecución de modelos de imagen, texto o voz mediante API.

**Desarrollo realizado:**
- Prueba de dos modelos generativos.
- Construcción de un microservicio o script con la API de Replicate.
- Evaluación de latencia y calidad del contenido generado.

**Entregables:**
- Evidencias de imágenes/textos generados.
- Script documentado.
- Carpeta `/replicate/` con el proyecto.

---

## **2.8 — Modelscope (Alibaba)**
Repositorio alternativo con modelos optimizados para hardware ligero.

**Desarrollo realizado:**
- Ejecución de un modelo alternativo.
- Comparación de rendimiento vs. Hugging Face.
- Construcción de una gráfica comparativa.

**Entregables:**
- Notebook ejecutado.
- Gráfica comparativa.
- Análisis en Markdown.

---

## **2.9 — LLaMaIndex (RAG)**
Framework especializado en creación de asistentes basados en documentos propios.

**Desarrollo realizado:**
- Creación de una base de conocimiento con 5 documentos académicos.
- Pipeline completo RAG (ingestión + indexación + consulta).
- Validación del grounding verificando si las respuestas provienen de los documentos.

**Entregables:**
- Notebook RAG ejecutado.
- Capturas de consultas.
- README técnico explicando arquitectura.

---

## **2.10 — GitHub Copilot (Asistente de Codificación)**
Integración de IA en el flujo de programación.

**Desarrollo realizado:**
- Generación de módulos de código.
- Refactorización y documentación automática.
- Comparación entre versión manual y generada por IA.

**Entregables:**
- Capturas en el IDE.
- Código documentado.
- Comparación técnica.

---

## **2.11 — Codeium**
Asistente gratuito para explicación y refactorización.

**Desarrollo realizado:**
- Generación de una función automática.
- Solicitud de refactorización y explicación paso a paso.
- Contraste con GitHub Copilot.

**Entregables:**
- Archivos de código.
- Capturas del proceso.
- Informe comparativo.

---

## **2.12 — Replit AI / Ghostwriter**
Entorno en la nube para crear aplicaciones completas con IA.

**Desarrollo realizado:**
- Microproyecto creado con IA (API / script / web app).
- Generación de archivos y rutas automáticamente.
- Evaluación de la estructura generada.

**Entregables:**
- Proyecto ejecutable.
- Carpeta `/replit/`.
- Informe técnico.

---

## **2.13 — Claude Code (Anthropic)**
IA que actúa como ingeniero de software colaborador.

**Desarrollo realizado:**
- Análisis completo de un repositorio subido.
- Refactorización automática del código.
- Generación de documentación.
- Creación de un módulo adicional mediante IA.

**Entregables:**
- Capturas del chat con Claude.
- Proyecto modificado.
- Informe de mejoras.

---

## **2.14 — Devin AI (Tendencias Futuras)**
Estudio conceptual del ingeniero autónomo.

**Desarrollo realizado:**
- Análisis crítico del concepto Devin AI.
- Evaluación de riesgos, límites y futuro del rol del ingeniero.
- Comparación con copilotos actuales.

**Entregables:**
- Ensayo técnico (1–2 páginas).
- Cuadro comparativo.
- Presentación breve.

---


---



