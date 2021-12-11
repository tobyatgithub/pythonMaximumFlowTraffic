import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LocalSource from "./components/LocalSource";
import RemoteSource from "./components/RemoteSource";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LocalSource />} />
        <Route path="abb" element={<RemoteSource />} />
      </Routes>
    </Router>
  );
}

function Home() {
  return <h2>Home</h2>;
}

export default App;
