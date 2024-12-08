import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { Container, Nav } from "react-bootstrap";
import "./App.css";
import Home from "./components/home"; // Importa o componente Home
import About from "./components/home"; // Crie outros componentes conforme necessário
import Services from "./components/home";
import Contact from "./components/home";

const App = () => {
  return (
    <Router>
      <div className="main-layout">
        {/* Barra Lateral */}
        <div className="sidebar">
          <h2 className="sidebar-title">Menu</h2>
          <Nav className="flex-column">
            <Nav.Link as={Link} to="/home" className="sidebar-link">Home</Nav.Link>
            <Nav.Link as={Link} to="/about" className="sidebar-link">About</Nav.Link>
            <Nav.Link as={Link} to="/services" className="sidebar-link">Services</Nav.Link>
            <Nav.Link as={Link} to="/contact" className="sidebar-link">Contact</Nav.Link>
          </Nav>
        </div>

        {/* Conteúdo Principal */}
        <div className="content">
          <Container>
            <Routes>
              <Route path="/home" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/services" element={<Services />} />
              <Route path="/contact" element={<Contact />} />
            </Routes>
          </Container>
        </div>
      </div>
    </Router>
  );
};

export default App;
