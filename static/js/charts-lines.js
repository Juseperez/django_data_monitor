// Obtener datos de Django
const productoLabels = JSON.parse(document.getElementById('producto-labels').textContent);
const productoValores = JSON.parse(document.getElementById('producto-valores').textContent);

const lineConfig = {
  type: 'line',
  data: {
    labels: productoLabels,
    datasets: [
      {
        label: 'Cantidad',
        backgroundColor: '#0694a2',
        borderColor: '#0694a2',
        data: productoValores,
        fill: false,
      }
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
    tooltips: {
      mode: 'index',
      intersect: false,
    },
    hover: {
      mode: 'nearest',
      intersect: true,
    },
    scales: {
      x: {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Producto',
        },
      },
      y: {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Cantidad',
        },
      },
    },
  },
};

// Renderizar gráfico
const lineCtx = document.getElementById('line');
window.myLine = new Chart(lineCtx, lineConfig);
