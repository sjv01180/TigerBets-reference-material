import React from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

const LeaderboardChart = () => {
  const options = {
    chart: {
      type: 'bar'
    },
    title: {
      text: 'Leaderboard Chart',
      style: {
        fontSize: '14px',
      }
    },
    xAxis: {
      categories: ['Grey_Sloan126', 'AveryJ', 'Derek253', 'Arizona_34', 'Xtina_Yang']
    },
    yAxis: {
      title: {
        text: 'Points'
      }
    },
    series: [{
      name: 'Points',
      data: [200, 180, 150, 140, 120],
      color: '#FBCEB1'
    }]
  };

  return (
    <HighchartsReact highcharts={Highcharts} options={options}/>
  );
};

export default LeaderboardChart;