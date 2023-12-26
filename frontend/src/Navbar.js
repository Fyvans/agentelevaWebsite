// frontend/src/Navbar.js

import React from 'react';

const Navbar = () => {
  return (
    <nav className="navbar navbar-light navbar-expand-lg menuNav">
      <a href="/"> {/* Use your URL for the homepage */}
        <img alt="brand" height="50px" width="50px" src="/static/images/logo-2.png" /> {/* Adjust the image source */}
      </a>
      <div className="collapse navbar-collapse container-fluid" id="navbarCollapse">
        <ul className="navbar-nav">
          <li className="nav-item"><a className="nav-link text-dark" href="/agente">Agent</a></li>
          <li className="nav-item"><a className="nav-link text-dark" href="/servico">Servicos</a></li>
          <li className="nav-item"><a className="nav-link text-dark" href="/contato">contactos</a></li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
