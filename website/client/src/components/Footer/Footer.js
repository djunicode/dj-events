import React , { Fragment } from 'react';
// import Nav1 from './Navbar';
import './Footer.css';
import { Container, Navbar, Nav } from 'react-bootstrap';

const Footer = () => {
  return (
    <div>
    <Fragment>
    <Navbar className="footercolor"> 
        <Nav className="m-auto">
            <Nav.Link to="/privacy" className="nav-link">
                Privacy
            </Nav.Link>
            <Nav.Link to="/terms" className="nav-link">
                Terms &amp; Conditions
            </Nav.Link>
            <Nav.Link to="/policy" className="nav-link">
                Policy
            </Nav.Link>
        </Nav>
    </Navbar>
    </Fragment>
    </div>
  );
}

export default Footer;