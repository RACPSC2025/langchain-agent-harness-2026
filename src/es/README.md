# 🇪🇸 LangChain Moderno: Guía de Estudio (Español)

¡Bienvenido a la versión en español del curso **LangChain Moderno: La Era del Agent Harness (2026)**! Esta carpeta contiene los notebooks interactivos y scripts de Python locales diseñados para un aprendizaje enfocado en producción.

---

## 📂 Contenido de la Carpeta

- **`lesson1_connect_es.ipynb`**: El notebook interactivo principal de Google Colab para la Lección 1. Cubre el paradigma del Agent Harness, `create_agent` y la creación de perfiles dinámicos de hiperparámetros mediante middleware.
- *(Las futuras lecciones se añadirán aquí como archivos `.ipynb`)*

---

## 🚀 Cómo Ejecutar los Notebooks

### Opción A: Google Colab (Recomendado)
1. Haz clic en `lesson1_connect_es.ipynb` en esta carpeta.
2. Haz clic en la insignia **"Abrir en Colab"** en la parte superior del archivo.
3. En Colab, haz clic en el icono de **Secretos** (🔑) en la barra lateral izquierda.
4. Añade un nuevo secreto llamado `GEMINI_API_KEY` y pega tu clave de API de [Google AI Studio](https://aistudio.google.com/).
5. Habilita el acceso del notebook al secreto y ejecuta las celdas en orden.

### Opción B: Ejecución Local (Avanzado)
Si prefieres ejecutarlo en tu máquina local (ej. VS Code o terminal):
1. Asegúrate de tener Python 3.11+ y `uv` o `pip` instalados.
2. Copia el archivo `.env.example` de la raíz del repositorio y renómbralo a `.env`, añadiendo tu `GEMINI_API_KEY`.
3. Instala las dependencias: `pip install -r requirements.txt` (o usa el `pyproject.toml` de la raíz).
4. Ejecuta el script de la lección: `python src/es/lesson_1_connect.py` (si está disponible) o usa `jupyter notebook`.

---

## 📝 Resumen de la Lección 1: El Agent Harness

En esta lección, aprendiste que el desarrollo moderno con LangChain ya no se trata de cadenas secuenciales y rígidas. En su lugar, utilizamos el **Agent Harness** (`create_agent`), que actúa como el chasis que envuelve al motor del LLM.

Exploraste tres formas de configurar el modelo:
1. **Clases de Integración Directa** (ej. `ChatGoogleGenerativeAI`: Útil para scripts locales, pero fuertemente acoplado al proveedor.
2. **Inicialización Agnóstica** (`init_chat_model`): El estándar recomendado para un código flexible e independiente del proveedor.
3. **Perfiles Dinámicos con Middleware** (Estándar de Producción): Uso de `runtime.context` y middleware personalizado para inyectar hiperparámetros (como la `temperature`) en cada petición, sin necesidad de reconstruir el agente.

---

## 🔗 Enlaces Útiles
- [Documentación Oficial de LangChain: Agents](https://docs.langchain.com/oss/python/langchain/agents)
- [Documentación Oficial de LangChain: Models](https://docs.langchain.com/oss/python/langchain/models)
- [Documentación Oficial de LangChain: Middleware & Runtime](https://docs.langchain.com/oss/python/langchain/runtime)

---
*¿Necesitas ayuda? Abre un issue en el repositorio principal o consulta el `README.md` de la raíz para ver la hoja de ruta completa del curso.*