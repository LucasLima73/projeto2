import { HashRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from './components/navbar'
import Home from  './components/home'
const About = () => <h1>About Page</h1>;
const Services = () => <h1>Services Page</h1>;
const Contact = () => <h1>Contact Page</h1>;

const App = () => {
  return (
    <Router>
      <div>
        <NavBar />
        <div style={{ marginLeft: "250px", padding: "20px" }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/services" element={<Services />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
