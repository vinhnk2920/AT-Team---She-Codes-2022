import React from 'react';
import Button from 'react-bootstrap/Button';
import "bootstrap/dist/js/bootstrap.js";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css'

function Header() {
  return (
    <div className='Header'>
      <img src={'./img/ATLogo.png'} className='logo-header'/>
      <div class="dropdown">
        <a class="btn btn-secondary dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
          Board
        </a>

        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
          <li><a class="dropdown-item" href="#">Something else here</a></li>
        </ul>
      </div>
      <div class="dropdown">
        <a class="btn btn-secondary dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
          App
        </a>

        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
          <li><a class="dropdown-item" href="#">Something else here</a></li>
        </ul>
      </div>
    </div>

  );
}
export default Header;