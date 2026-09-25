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
3. **Capturas de pantalla:** imagen generada automáticamente por `generador_imagenes.py` (código resaltado + vista real en el navegador, lado a lado).
4. **Tabla "Observaciones / Efecto de las etiquetas":** explicación breve, con palabras propias, de qué hace cada etiqueta según lo observado al ejecutar el código.

## Generador de imágenes automático

El script `generador_imagenes.py` hace **todo en un solo comando**:
1. Renderiza el código HTML con resaltado de sintaxis estilo Dracula.
2. Toma una captura de pantalla real del archivo abierto en Chromium.
3. Combina ambas en una imagen PNG lado a lado (guardada en `capturas/`).
4. Inserta automáticamente la imagen en la sección correspondiente de `docs/JCCP_Web_Practicas.docx`.
5. Guarda también la copia de entrega `docs/JCCP_Web_Act6.docx`.

> [!IMPORTANT]
> **No cierres el archivo Word antes de ejecutar el script.** Si está abierto, el script no podrá guardar.

```powershell
# Todas las prácticas de act6 (por defecto)
py generador_imagenes.py

# Una carpeta completa
py generador_imagenes.py act5/

# Un archivo específico
py generador_imagenes.py act6/practica14.html
```

## Pasos para actualizar cuando hay prácticas nuevas
1. Crear los archivos `.html` en la carpeta `actN/` con el formato estándar.
2. Agregar las secciones nuevas al final de `JCCP_Web_Practicas.docx` siguiendo la plantilla.
3. Ejecutar `py generador_imagenes.py actN/` — las imágenes se generan e insertan solas.
4. Actualizar la fecha del encabezado del documento.
5. Hacer commit y push a GitHub.

## Notas
- Cuidar ortografía y que cada observación esté en palabras propias, no copiada literal del manual.
- Formato de los archivos `.html`:
  - Comentarios al inicio: `<!-- Practica N -->`, `<!-- Juan Carlos Camarena Pillado -->`, `<!-- Objetivo de la Practica: ... -->`.
  - Primer párrafo en el `<body>`: `<p>Juan Carlos Camarena Pillado</p>`.
- Estado actual:
  - `act4`: Práctica 1.
  - `act5`: Prácticas 1 a 9.
  - `act6`: Prácticas 11 a 20 con imágenes generadas e insertadas automáticamente en el documento Word.
  - Documento maestro `JCCP_Web_Practicas.docx` y copia para entrega `JCCP_Web_Act6.docx` en `docs/`.
