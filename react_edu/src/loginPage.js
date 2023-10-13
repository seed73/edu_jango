import React from 'react';
// import './loginPage.css';

function LoginForm() {
  return (
    <div id="main" className="main">
      <div className="background-image-wrapper">
        <img src="" alt=""/>
      </div>
      <form>
        <div>
          <input type="id" name="id" placeholder="id" />
          <input type="password" name="password" placeholder="password" />
        </div>                    
        <div>
          <input type="submit" className="blue-button" value="login" />
        </div>
      </form>
    </div>
  );
}

export default LoginForm;