<script>
// import * as chart from 'chart.js';
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: {
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

    myLabels = this.parseDataset(this.chartdata)[0];
    myValues = this.parseDataset(this.chartdata)[1];

    // myLabels2 = this.parseDataset(this.chartdata2)[0];
    myValues2 = this.parseDataset(this.chartdata2)[1];

    this.renderChart(
      {
        labels: myLabels,
        datasets: [
          {
            label: "Vlhkost",
            fill: false,
            backgroundColor: "#0000000",
            borderColor: "#7FD97E",
            pointBackgroundColor: '#0000000',
            pointBorderColor: '#7FD97E',
            data: myValues,
          },
          {
            label: "Teplota",
            fill: false,
            backgroundColor: "#7FD97E",
            borderColor: '#0000ff',
            pointBackgroundColor: '#7FD97E',
            pointBorderColor: '0000ff',
            data: myValues2,
          },
        ],
      },
      this.options
    );
  },
};
</script>
