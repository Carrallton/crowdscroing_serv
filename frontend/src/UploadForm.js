import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [inn, setInn] = useState('');
  const [message, setMessage] = useState('');

  const handleUpload = async () => {
    if (!file) {
      alert("Выберите файл");
      return;
    }

    if (!inn || inn.length !== 10) {
      alert("Введите корректный ИНН (10 цифр)");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('inn', inn);

    try {
      const res = await axios.post('http://localhost:8000/api/upload/', formData);
      setMessage(res.data.message);
    } catch (err) {
      setMessage("Ошибка при загрузке файла");
    }
  };

  return (
    <div style={{ maxWidth: '500px', margin: 'auto' }}>
      <h2>Загрузите финансовые данные</h2>

      <label>
        <strong>ИНН компании:</strong>
        <input
          type="text"
          placeholder="10 цифр"
          value={inn}
          onChange={(e) => setInn(e.target.value)}
          style={{ width: '100%', padding: '8px', marginBottom: '10px' }}
        />
      </label>

      <label>
        <strong>Финансовый файл (.xlsx):</strong>
        <input
          type="file"
          accept=".xlsx"
          onChange={(e) => setFile(e.target.files[0])}
          style={{ width: '100%', padding: '8px', marginBottom: '10px' }}
        />
      </label>

      <button
        onClick={handleUpload}
        style={{
          width: '100%',
          padding: '10px',
          backgroundColor: '#007BFF',
          color: 'white',
          border: 'none',
          cursor: 'pointer'
        }}
      >
        Загрузить
      </button>

      <p style={{ marginTop: '10px' }}>{message}</p>
    </div>
  );
}

export default UploadForm;