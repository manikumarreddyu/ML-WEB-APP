import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import CropForm from './components/CropForm';
import Prediction from './components/Prediction';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Predict" element={<CropForm />} />
        <Route path="/prediction" element={<Prediction />} />
      </Routes>
    </Router>
  );
}

export default App;
