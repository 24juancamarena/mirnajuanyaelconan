// Proyecto Ciberseguridad SNCT 2026 - interacciones de la página

// Sombra en la cabecera y botón de subir al hacer scroll
const cabecera = document.getElementById('cabecera');
const subir = document.getElementById('subir');
window.addEventListener('scroll', () => {
  cabecera.classList.toggle('sombra', window.scrollY > 10);
  subir.classList.toggle('visible', window.scrollY > 600);
}, { passive: true });

// Menú hamburguesa (celular)
const hamburguesa = document.getElementById('hamburguesa');
const menu = document.getElementById('menu');
hamburguesa.addEventListener('click', () => {
  const abierto = menu.classList.toggle('abierto');
  hamburguesa.setAttribute('aria-expanded', abierto);
  hamburguesa.setAttribute('aria-label', abierto ? 'Cerrar menú' : 'Abrir menú');
});
menu.querySelectorAll('a').forEach(enlace => enlace.addEventListener('click', () => {
  menu.classList.remove('abierto');
  hamburguesa.setAttribute('aria-expanded', 'false');
  hamburguesa.setAttribute('aria-label', 'Abrir menú');
}));

// Resaltar en el menú la sección que se está viendo
const enlacesMenu = [...menu.querySelectorAll('a:not(.boton)')];
const observadorSecciones = new IntersectionObserver(entradas => {
  entradas.forEach(entrada => {
    if (!entrada.isIntersecting) return;
    enlacesMenu.forEach(a => a.classList.toggle('activo', a.getAttribute('href') === '#' + entrada.target.id));
  });
}, { rootMargin: '-45% 0px -50% 0px' });
enlacesMenu.forEach(a => {
  const seccion = document.querySelector(a.getAttribute('href'));
  if (seccion) observadorSecciones.observe(seccion);
});

// Contadores animados (formato español: 2.760 / 4,99)
const formato = (valor, decimales) => valor.toLocaleString('es-ES', {
  minimumFractionDigits: decimales,
  maximumFractionDigits: decimales,
  useGrouping: 'always'
});
const animarContador = el => {
  const meta = parseFloat(el.dataset.contador);
  const decimales = parseInt(el.dataset.decimales || '0', 10);
  const prefijo = el.dataset.prefijo || '';
  const sufijo = el.dataset.sufijo || '';
  const duracion = 1600;
  const inicio = performance.now();
  const paso = ahora => {
    const t = Math.min((ahora - inicio) / duracion, 1);
    const suave = 1 - Math.pow(1 - t, 3);
    el.textContent = prefijo + formato(meta * suave, decimales) + sufijo;
    if (t < 1) requestAnimationFrame(paso);
  };
  requestAnimationFrame(paso);
};
const sinMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const observadorCifras = new IntersectionObserver(entradas => {
  entradas.forEach(entrada => {
    if (!entrada.isIntersecting) return;
    if (!sinMovimiento) animarContador(entrada.target);
    observadorCifras.unobserve(entrada.target);
  });
}, { threshold: .6 });
document.querySelectorAll('[data-contador]').forEach(el => observadorCifras.observe(el));

// Pestañas de la sección de IA (clic y flechas del teclado)
const pestanas = [...document.querySelectorAll('.pestana')];
const activarPestana = pestana => {
  pestanas.forEach(p => {
    const activa = p === pestana;
    p.classList.toggle('activa', activa);
    p.setAttribute('aria-selected', activa);
    p.tabIndex = activa ? 0 : -1;
    document.getElementById(p.getAttribute('aria-controls')).classList.toggle('activo', activa);
  });
};
pestanas.forEach((pestana, i) => {
  pestana.addEventListener('click', () => activarPestana(pestana));
  pestana.addEventListener('keydown', e => {
    if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    const siguiente = pestanas[(i + (e.key === 'ArrowRight' ? 1 : -1) + pestanas.length) % pestanas.length];
    siguiente.focus();
    activarPestana(siguiente);
  });
});

// Aparición suave de tarjetas y bloques al hacer scroll
const observadorRevelar = new IntersectionObserver(entradas => {
  entradas.forEach(entrada => {
    if (!entrada.isIntersecting) return;
    entrada.target.classList.add('visible');
    observadorRevelar.unobserve(entrada.target);
  });
}, { threshold: .12 });
document.querySelectorAll('.tarjeta, .titulo-seccion, .linea-tiempo li, .casos li, .aviso, .tabla-envoltura, .comparativa, .glosario > div').forEach(el => {
  el.classList.add('revelar');
  observadorRevelar.observe(el);
});
