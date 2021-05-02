<script>
// import * as chart from 'chart.js';
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: {
    // onChange: function(){},
    chartdata: {
      type: Array,
      default: null,
      require: true,
    },
    chartdata2: {
      type: Array,
      default: null,
      require: false,
    },
    chartdata3: {
      type: Array,
      default: null,
      require: false,
    },
    options: {
      type: Object,
      default: null,
    },
  },
  methods: {
    parseDataset(dataset) {
      var labels = [];
      var values = [];

      dataset.forEach((element) => {
        labels.push(element.date);
        values.push(element.value);
      });
      return [labels, values];
    },
  },
  mounted() {
    var myLabels;
    var myValues;

    // var myLabels2;
    var myValues2;
    var myValues3;

    myLabels = this.parseDataset(this.chartdata)[0];
    myValues = this.parseDataset(this.chartdata)[1];

    // myLabels2 = this.parseDataset(this.chartdata2)[0];
    myValues2 = this.parseDataset(this.chartdata2)[1];
    myValues3 = this.parseDataset(this.chartdata3)[1];

    this.renderChart(
      {
        labels: myLabels,
        datasets: [
          {
            label: "Teplota",
            fill: false,
            backgroundColor: "#0000ff",
            borderColor: "#0000ff",
            pointBackgroundColor: "#0000ff",
            pointBorderColor: "0000ff",
            data: myValues2,
            yAxisID: "y",
          },
          {
            label: "Vlhkost",
            fill: false,
            backgroundColor: "#7FD97E",
            borderColor: "#7FD97E",
            pointBackgroundColor: "#7FD97E",
            pointBorderColor: "#7FD97E",
            data: myValues,
            yAxisID: "y1",
          },
          {
            label: "Hmotnost",
            fill: false,
            backgroundColor: "#ff0000",
            borderColor: "#ff0000",
            pointBackgroundColor: "#ff0000",
            pointBorderColor: "#ff0000",
            data: myValues3,
            yAxisID: "y2",
          },
        ],
      },
      {
        maintainAspectRatio: false,
        responsive: true,
        interaction: {
          mode: "index",
          intersect: false,
        },
        stacked: false,
        plugins: {
          title: {
            display: true,
            text: "Chart.js Line Chart - Multi Axis",
          },
        },
        scales: {
          yAxes: [
                  {
                  type: 'linear',
                  display: true,
                  position: 'left',
                  id: 'y',
                    },
                    {
                  type: 'linear',
                  display: true,
                  position: 'right',
                  grid: {
                    display: false, // only want the grid lines for one axis to show up
                  },
                  id: 'y1',
                    },
                    {
                  type: 'linear',
                  display: true,
                  position: 'left',
                  grid: {
                    display: false, // only want the grid lines for one axis to show up
                  },
                  id: 'y2',
                    },
                ],
        //  {
        //   y: {
        //     type: "linear",
        //     display: true,
        //     position: "left",
        //   },
        //   y1: {
        //     type: "linear",
        //     display: true,
        //     position: "right",

        //     // grid line settings
        //     grid: {
        //       drawOnChartArea: false, // only want the grid lines for one axis to show up
        //     },
        //   },
        // },
      }
      },
    );
  },
};
</script>
