import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function CompanyPage() {
  const { inn } = useParams();
  const [company, setCompany] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/companies/${inn}/`)
      .then(res => setCompany(res.data))
      .catch(err => console.log(err));
  }, [inn]);

  if (!company) return <p>Загрузка...</p>;

  return (
    <div style={{ padding: '2rem' }}>
      <h2>{company.name} ({company.inn})</h2>

      <h3>Отчеты:</h3>
      <table border="1" cellSpacing="0" cellPadding="5">
        <thead>
          <tr>
            <th>Год</th>
            <th>Выручка</th>
            <th>Себестоимость</th>
            <th>Прибыль</th>
            <th>Активы</th>
            <th>Обязательства</th>
          </tr>
        </thead>
        <tbody>
          {company.reports.map(report => (
            <tr key={report.id}>
              <td>{report.year}</td>
              <td>{report.revenue}</td>
              <td>{report.cost_of_sales}</td>
              <td>{report.net_profit}</td>
              <td>{report.total_assets}</td>
              <td>{report.total_liabilities}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default CompanyPage;