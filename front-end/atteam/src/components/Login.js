import React from 'react';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css'

function Login() {
  return (
    <div class="container login">
      <div class="login-left">
        <div class="col login-left-content">
          <img src={'./img/ATLogo.png'} className='img-login-left' />
          <h2 className='welcome'>Welcome</h2>

          <div className='form'>
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label label-login">Username:</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder='Enter your username'/>
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label label-login">Password:</label>
              <input type="password" class="form-control" id="exampleInputPassword1" placeholder='Enter your password' />
            </div>
            <a href=''>
              <label style={{color:'black',cursor:'pointer',fontWeight:'bold'}}>Forgot password?</label>
            </a>
            <button type="submit" class="btn btn-primary btn-login">Login</button>
          </form>
          </div>

        </div>
      </div>
      <div class="login-right">
        <div class="col login-right-content">
          <h5 className='paragraph'>Let's be great together</h5>
          <img src={'./img/together.png'} className='img-login-right' />
        </div>
      </div>
    </div>
  );
}
export default Login;