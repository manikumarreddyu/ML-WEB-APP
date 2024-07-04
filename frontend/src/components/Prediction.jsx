import React from 'react';

function Prediction({ prediction }) {
  return (
    <div className="p-4">
      <h5>According to your soil nutrients</h5>
      <h5>You Should Grow:</h5>
      <div className="prediction bg-gray-100 p-4 rounded-md shadow-md">
        <h4>{prediction}</h4>
      </div>
    </div>
  );
}

export default Prediction;
