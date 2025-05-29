import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CompaniesList() {
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/companies/')
      .then(res => setCompanies(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Список компаний</h2>
      <ul>
        {companies.map(company => (
          <li key={company.inn}>
            <a href={`/company/${company.inn}`}>{company.name} ({company.inn})</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CompaniesList;