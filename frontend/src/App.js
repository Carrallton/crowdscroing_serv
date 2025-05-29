import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UploadForm from './UploadForm';
import CompaniesList from './CompaniesList';
import CompanyPage from './CompanyPage';

function App() {
  return (
    <Router>
      <div style={{ fontFamily: 'Arial', maxWidth: '800px', margin: 'auto' }}>
        <nav>
          <a href="/">Главная</a> | 
          <a href="/upload">Загрузить</a> | 
          <a href="/companies">Компании</a>
        </nav>

        <Routes>
          <Route path="/" element={<UploadForm />} />
          <Route path="/upload" element={<UploadForm />} />
          <Route path="/companies" element={<CompaniesList />} />
          <Route path="/company/:inn" element={<CompanyPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;