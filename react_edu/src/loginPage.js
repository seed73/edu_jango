import React from 'react';
// import myImage from '/assets/images/usfd9ae8yojcqgxbmafaistv8-1.webp';
// import './loginPage.css';

function LoginForm() {
  return (
    <div class="w-[1440px] h-[1024px] relative overflow-hidden bg-white">
      <img src={process.env.PUBLIC_URL + '/assets/images/usfd9ae8yojcqgxbmafaistv8.webp'} class="w-[926px] h-[180px] absolute left-64 top-[182px] object-cover" alt="logo"/>
      <div class="w-[315px] h-[60px] absolute left-[563px] top-[528px]">
        <div
          class="w-[315px] h-[60px] absolute left-[-1px] top-[-1px] rounded-[5px] bg-[#f2f5f6]"
        ></div>
        <p class="absolute left-8 top-[19px] text-base text-left text-black/20">id</p>
      </div>
      <div class="w-[315px] h-[60px] absolute left-[563px] top-[603px]">
        <div
          class="w-[315px] h-[60px] absolute left-[-1px] top-[-1px] rounded-[5px] bg-[#f2f5f6]"
        ></div>
        <p class="absolute left-8 top-[19px] text-base text-left text-black/20">password</p>
      </div>
      <div class="w-[314px] h-[60px] absolute left-[563px] top-[702px]">
        <div
          class="w-[315px] h-[60px] absolute left-[-1px] top-[-1px] rounded-[5px] bg-[#4880ee]"
        ></div>
        <p
          class="w-[124px] h-[25px] absolute left-[95px] top-[18px] text-base font-bold text-center text-white"
        >
          LOGIN
        </p>
      </div>
      <p
        class="w-[195px] h-[30px] absolute left-[622px] top-[777px] text-base font-bold text-center text-[#4880ee]"
      >
        find password
      </p>
    </div>
  );
}

export default LoginForm;