import './App.css';
import React from 'react';
import UploadForm from './UploadForm';

function App() {
  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>Оценка кредитоспособности компаний</h1>
      <UploadForm />
    </div>
  );
}

export default App;
