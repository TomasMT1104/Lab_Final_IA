# Laboratorio Final — Profundización I en Inteligencia Artificial  
**Universidad de Manizales — Ingeniería de Sistemas y Telecomunicaciones**  
**Estudiantes:** Tomás Marín Toro, Daniel Cortes Valencia, Valentina Arango Mendieta, Juan Esteban  
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

---
## Actividad 5 — Kaggle (EDA)

- Notebook público: [ENLACE AQUÍ]
- PDF del EDA: (archivo adjunto en /kaggle/)
- Gráficas incluidas y análisis completo.

---

# 📝 Créditos  
**Estudiante responsable de este repositorio:** Tomás Marín Toro  
**Curso:** Profundización I — Inteligencia Artificial  
**Universidad de Manizales**

