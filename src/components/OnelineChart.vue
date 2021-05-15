<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: {
    title: {
      type: String,
      default: "",
    },
    description: {
      type: String,
      default: "",
    },
    chartData: {
      type: Array,
      default: null,
      require: true,
    },
    options: {
      type: Object,
      default: null,
    },
  },
  watch: {
    chartData: function() {
      this.createChart();
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

    colorWarning(context) {
      let index = context.dataIndex;
      let value = context.dataset.data[index];
      var res = "#0000ff";

      if (this.title == "Vlhkost") {
        res = value >= 95 || value <= 0 ? "#ff0000" : "#0000ff";
      }

      if (this.title == "Teplota") {
        res = value < 10 ? "#ff0000" : "#0000ff";
      }
      if (this.title == "Hmotnost") {
        if (index == 0) {
          res = "#0000ff";
        } else {
          let value2 = context.dataset.data[index - 1];
          res = Math.abs(value - value2) > 5 ? "#ff0000" : "#0000ff";
        }
      }
      return res;
    },

    sizeWarning(context) {
      let index = context.dataIndex;
      let value = context.dataset.data[index];
      var res = 3;

      if (this.title == "Vlhkost") {
        res = value >= 95 || value <= 0 ? 7 : 3;
      }

      if (this.title == "Teplota") {
        res = value < 10 ? 7 : 3;
      }

      if (this.title == "Hmotnost") {
        if (index == 0) {
          res = 3;
        } else {
          let value2 = context.dataset.data[index - 1];
          res = Math.abs(value - value2) > 5 ? 7 : 3;
        }
      }
      return res;
    },

    createChart() {
      var myLabels;
      var myValues;

      myLabels = this.parseDataset(this.chartData)[0];
      myValues = this.parseDataset(this.chartData)[1];

      this.renderChart(
        {
          labels: myLabels,
          datasets: [
            {
              label: this.title,
              fill: false,
              backgroundColor: this.colorWarning,
              borderColor: this.colorWarning,
              pointBackgroundColor: this.colorWarning,
              pointBorderColor: this.colorWarning,
              data: myValues,
              yAxisID: "y",
              xAxisID: "x",
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
          elements: {
            point: {
              radius: this.sizeWarning,
              display: true,
            },
          },
          scales: {
            xAxes: [
              {
                font: {
                  family: "'Source Sans Pro', 'Helvetica', 'Arial', sans-serif",
                },
                scaleLabel: {
                  display: true,
                  labelString: "Datum",
                },
                type: "time",
                time: {
                  parser: "YYYY-MM-DD HH:mm:ss",
                  unit: "day",
                  displayFormats: {
                    day: "DD. MM. YYYY",
                  },
                },
                id: "x",
              },
            ],
            yAxes: [
              {
                font: {
                  family: "'Source Sans Pro', 'Helvetica', 'Arial', sans-serif",
                },
                scaleLabel: {
                  display: true,
                  labelString: this.description,
                },
                type: "linear",
                display: true,
                position: "left",
                id: "y",
              },
            ],
          },
        }
      );
    },
  },
  mounted() {
    this.createChart();
  },
};
</script>
