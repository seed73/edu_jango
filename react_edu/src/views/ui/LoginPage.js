import React from 'react';
import './css/LoginPage.css';
import LoginForm from './component/LoginPage/LoginForm.js';

function LoginPage() {
  return (
    <div className="login-page pageWrapper d-lg-flex">
      <img src={process.env.PUBLIC_URL + '/assets/images/usfd9ae8yojcqgxbmafaistv8.webp'} className="login-logo" alt="logo"/>
      <LoginForm />
      <p className="find-password">
        find password
      </p>
    </div>
  );
}

export default LoginPage;