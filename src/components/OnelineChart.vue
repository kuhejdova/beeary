<script>
// import * as chart from 'chart.js';
import { Line } from "vue-chartjs";
// const { reactiveProp } = mixins;

export default {
  extends: Line,
  // mixins: [reactiveProp],
  props: {
    // onChange: function(){},
    title: {
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
    chartData: function(){
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

    humidityWarning(context){
      let index = context.dataIndex;
      let value = context.dataset.data[ index ];
      
      var res = value >= 95 ? "#ff0000" : "#0000ff";
      console.log(res)
      return res
    },

    createChart(){
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
            backgroundColor: "#0000ff",
            borderColor: "#0000ff",
            pointBackgroundColor: this.humidityWarning,
            pointBorderColor: this.humidityWarning,
            data: myValues,
            yAxisID: "y",
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
        // elements: {
        //   point: {
        //     pointBackgroundColor : this.humidityWarning,
        //     pointBorderColor : this.humidityWarning,
        //     display: true
        //   }
        // },
        scales: {
          yAxes: [
            {
              type: "linear",
              display: true,
              position: "left",
              id: "y",
            },
          ],
        },
      }
    );
    }


  },
  mounted() {
    this.createChart();
  },
};
</script>
