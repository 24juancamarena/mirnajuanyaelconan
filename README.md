# Proceso para documentar las prácticas de HTML — Construye Aplicaciones Web

## Objetivo
Mantener **un solo archivo Word** (no uno por actividad) que se va actualizando cada vez que se resuelven prácticas nuevas del manual. Ese mismo archivo es el que se entrega en cada actividad (Act 4, Act 5, Act 6, …); crece práctica por práctica, sin borrar ni duplicar lo que ya está.

## Archivo maestro
- **Nombre fijo:** `JCCP_Web_Practicas.docx`
- Es el ÚNICO archivo que se edita. No se crean archivos nuevos por cada actividad.
- Si el profesor pide un nombre específico para entregar una actividad puntual (ej. `JCCP_Web_Act6`), se guarda una **copia** del maestro con ese nombre al momento de entregar, pero el trabajo real sigue en el maestro.

## Encabezado fijo (no cambia entre prácticas)
| Campo | Valor |
|---|---|
| Plantel | CBTIS 224 |
| Asignatura | Construye Aplicaciones Web |
| Semestre / Especialidad | 5° semestre, Programación |
| Nombre | Juan Carlos Camarena Pillado |
| Fecha | se actualiza a la fecha de la última modificación |

## Plantilla que se repite en cada práctica
Cada práctica nueva se agrega **al final** del documento con esta estructura exacta, para que todas se vean iguales:

1. **Encabezado:** `Práctica N — [Título tal como aparece en el manual]`
2. **Etiquetas utilizadas:** lista de las etiquetas/atributos HTML vistos en esa práctica.
3. **Capturas de pantalla:** 1–2 imágenes (código en el editor y/o resultado en el navegador).
4. **Tabla "Observaciones / Efecto de las etiquetas":** explicación breve, con palabras propias, de qué hace cada etiqueta según lo observado al ejecutar el código.

## Pasos para actualizar el archivo cada vez que hay prácticas nuevas
1. Comparar el manual de prácticas (PDF) más reciente contra las secciones **"Práctica N"** que YA existen en `JCCP_Web_Practicas.docx`.
2. Identificar solo los números de práctica que faltan (los que no tienen todavía su sección en el documento).
3. Agregar esas prácticas nuevas al final, siguiendo la plantilla de arriba, sin modificar ni duplicar las que ya están.
4. Insertar las capturas de pantalla que el alumno suba para esas prácticas nuevas — el documento no se da por completo sin ellas.
5. Actualizar únicamente la fecha del encabezado.
6. Guardar todo bajo el mismo nombre: `JCCP_Web_Practicas.docx`.

## Instrucción lista para pegarle a la IA cada vez
> "Aquí está el manual de prácticas actualizado y mi documento maestro `JCCP_Web_Practicas.docx`. Revisa qué números de práctica son nuevos comparando contra lo que ya existe en el documento, agrégalos siguiendo exactamente la misma plantilla y formato que las prácticas anteriores, y no toques las que ya están. Te subo aparte las capturas de pantalla de las prácticas nuevas."

## Notas
- Las capturas de pantalla siempre las aporta el alumno (código + resultado en el navegador); una IA no puede generarlas por ti.
- Cuidar ortografía y que cada observación esté en palabras propias, no copiada literal del manual.
- Formato de los archivos `.html`:
  - Comentarios al inicio: `<!-- Practica N -->`, `<!-- Juan Carlos Camarena Pillado -->`, `<!-- Objetivo de la Practica: ... -->`.
  - Primer párrafo en el `<body>`: `<p>Juan Carlos Camarena Pillado</p>`.
- Estado actual:
  - `act4`: Práctica 1.
  - `act5`: Prácticas 1 a 9.
  - `act6`: Prácticas 11 a 20 (archivos `.html` con los datos del alumno Juan Carlos Camarena Pillado).
  - Documento maestro `JCCP_Web_Practicas.docx` y copia para entrega `JCCP_Web_Act6.docx` en `docs/` con las secciones de las prácticas 11 a 20 agregadas según la plantilla.

