# Pizza Viva — free template

Plantilla gratuita para pizzerías, con fotografías generadas con IA, diseño responsive, español/inglés/portugués, tema claro/oscuro, filtros vegetarianos, personalización de pizza y carrito.

## Uso

Sirve este directorio con cualquier servidor estático, por ejemplo `python -m http.server 3300`, y abre `http://localhost:3300`. No necesita npm ni compilación. Google Fonts es opcional; hay tipografías de respaldo locales.

## Recibir solicitudes reales

Edita `config.js`:
- `whatsapp`: tu número internacional real, solo dígitos (sin +, espacios ni guiones).
- `contactEmail`: correo comercial real para solicitudes de personalización.

El pedido abre WhatsApp con un resumen, y el formulario abre el correo del visitante (o WhatsApp si solo se configuró ese canal). El visitante debe completar el envío. La plantilla NO guarda leads en un servidor, NO procesa pagos y NO confirma pedidos ni reservas. Sin contacto configurado, muestra una demo honesta y permite copiar el resumen. Los datos de formularios permanecen en memoria; solo se guardan idioma y tema en localStorage.

Precios ilustrativos en USD. Actualiza productos, precios, alérgenos, textos y contactos antes de publicar. No se incluyen tarifas de entrega.

## Archivos

- `index.html`: contenido y traducciones.
- `styles.css`: diseño y adaptación móvil.
- `app.js`: catálogo, filtros, carrito, idiomas y contacto.
- `config.js`: configuración pública de contacto. Nunca agregues secretos.
- `assets/*.webp`: fotografías optimizadas usadas por el sitio.
- `IMAGE-PROMPTS.md`: procedencia y prompts de imágenes.
- `build-template.py`: regenera el ZIP después de editar.

Ejecuta `python build-template.py` para actualizar la descarga local. El ZIP incluye una copia de sí mismo de un solo nivel para que la descarga también funcione al descomprimirlo, sin recursión infinita.

## Licencia

Código bajo licencia MIT. Conserva LICENSE y el aviso de copyright original de Iran Trinidad. El sitio es una demostración, no un restaurante real. Las fotografías nuevas fueron generadas mediante la herramienta de imágenes integrada; no representan productos de un establecimiento real.
