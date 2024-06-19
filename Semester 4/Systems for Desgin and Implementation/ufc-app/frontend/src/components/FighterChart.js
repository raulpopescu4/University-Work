import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';

function FighterDoughnutChart({ fightersList }) {
  const fightersYoungerThan30 = fightersList.filter((fighter) => fighter.age < 30).length;
  const fighters30OrOlder = fightersList.filter((fighter) => fighter.age >= 30).length;

  const data = {
    labels: ['Younger than 30', '30 or Older'],
    datasets: [
      {
        data: [fightersYoungerThan30, fighters30OrOlder],
        backgroundColor: ['#FF6384', '#36A2EB'],
        hoverBackgroundColor: ['#FF6384', '#36A2EB'],
      },
    ],
  };

  return (
    <div style={{ width: "20%" }}>
      <h2>Fighters Younger and Older than 30</h2>
      <Doughnut data={data} />
    </div>
  );
}

export default FighterDoughnutChart;
