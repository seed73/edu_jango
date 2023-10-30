import React from 'react';
// import myImage from '/assets/images/usfd9ae8yojcqgxbmafaistv8-1.webp';
import './loginPage.css';
import LoginForm from './login/LoginForm';

function LoginPage() {
  return (
    <div class="w-[1440px] h-[1024px] relative overflow-hidden bg-white">
      <img src={process.env.PUBLIC_URL + '/assets/images/usfd9ae8yojcqgxbmafaistv8.webp'} class="w-[926px] h-[180px] absolute left-64 top-[182px] object-cover" alt="logo"/>
      <LoginForm />
      <p
        class="w-[195px] h-[30px] absolute left-[622px] top-[777px] text-base font-bold text-center text-[#4880ee]"
      >
        find password
      </p>
    </div>
  );
}

export default LoginPage;