<script>
// import * as chart from 'chart.js';
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: {
    chartdata: {
      type: Object,
      default: null,
    },
    options: {
      type: Object,
      default: null,
    },
  },
  mounted() {
    this.renderChart(
      {
        labels: ["date", "value"],
        datasets: [
          {
            label: "humidity",
            data: this.chartdata,
          },
        ],
      },
      this.options
    );
  },
};
</script>
