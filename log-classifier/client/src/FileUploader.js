import React, { useState } from 'react';

function FileUploader({ onFileSelect }) {
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    onFileSelect(file);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange}
      style={{
        border: '1px solid #D5D7DF',
        padding: '10px',
        borderRadius: '10px'
      }} />
      Hi
    </div>
  );
}

export default FileUploader;
