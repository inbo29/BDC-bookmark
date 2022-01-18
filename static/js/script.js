//////////////////pie1 //////////////////////


// setup
const datapie = {
    labels: ['Нэмэлт Дата төв өргөжүүлэлт', 'IEO санал болгох хэмжээ'],
    datasets: [{
        label: 'Block Box AC',
        data: [90, 10],
        backgroundColor: [
            'rgba(37, 191, 198, 1)',
            'rgba(155, 154, 154, 0.5)'
        ],
        borderColor: [
            'rgba(37, 191, 198, 1)',
            'rgba(155, 154, 154, 0.5)'
        ],
        borderWidth: 1
    }]
};

// plugin block
const legendMargin = {
    id: 'legendMargin',
    beforeInit(chart, legend, options) {
        console.log(chart.legend.fit)
        const fitValue = chart.legend.fit;

        chart.legend.fit = function fit() {
            fitValue.bind(chart.legend)();
            return this.height += 30;
        }
    }
};

// config
const configpie = {
    type: 'doughnut',
    data: datapie,
    options: {
        layout: {
            padding: 20
        },
        plugins:{
            datalabels: {
                color: '#fff',
            },
            legend:{
                labels: {
                    padding: 5
                },
                display: true,
                position: 'bottom'
            },
            labels: {
                // render: 'label',
                // precision: 1,
                // arc: false,
                // position: 'border',
                fontSize: 15,
            }
        }
    },
    plugin: [legendMargin]
};

// render init block
const myChart3 = new Chart(
    document.getElementById('myChart3'),
    configpie
);
/////////////////// pie2 ///////////////////


const datapie2 = {
    labels: ['Блокчэйн Дата Төв', 'Маркетинг', 'Хөгжүүлэлт', 'Компанийн ашиг'],
    datasets: [{
        data: [70, 10, 10, 10],
        backgroundColor: [
            'rgba(37, 191, 198, 1)',
            'rgba(7, 104, 159, 1)',
            'rgba(73, 127, 229, 1)',
            'rgba(155, 154, 154, 0.5)'
        ],
        borderColor: [
            'rgba(37, 191, 198, 1)',
            'rgba(7, 104, 159, 1)',
            'rgba(73, 127, 229, 1)',
            'rgba(155, 154, 154, 0.5)'
        ],
        borderWidth: 1,
    }]
};


const configpie2 = {
    type: 'doughnut',
    data: datapie2,
    options: {
        layout: {
            padding: 20
        },
        plugins:{
            legend:{
                labels: {
                    padding: 5
                },
                display: true,
                position: 'bottom'
            },
            labels: {
                fontSize: 15
            }
        }
    }
};


const pieChart = new Chart(
    document.getElementById('pieChart'),
    configpie2
);

////////////// pie3 ///////////////////

const datapie3 = {
    labels: ['BuyBack-BurnOut', 'Үйл ажиллагаа', 'Биткойн Тараалт','Өргөжүүлэлт'],
    datasets: [{
        data: [20, 20, 30, 30],
        backgroundColor: [
            'rgba(73, 127, 229, 1)',
            'rgba(155, 154, 154, 0.5)',
            'rgba(7, 104, 159, 1)',
            'rgba(37, 191, 198, 1)'
        ],
        borderColor: [
            'rgba(73, 127, 229, 1)',
            'rgba(155, 154, 154, 0.5)',
            'rgba(7, 104, 159, 1)',
            'rgba(37, 191, 198, 1)'
        ],
        borderWidth: 1
    }]
};


const configpie3 = {
    type: 'doughnut',
    data: datapie3,
    options: {
        layout: {
            padding: 20
        },
        plugins:{
            legend:{
                labels: {
                    padding: 3
                },
                display: true,
                position: 'bottom'
            },
            labels: {
                fontSize: 15
            }
        }
    }
};


const pieChartLast = new Chart(
    document.getElementById('pieChartLast'),
    configpie3
);
