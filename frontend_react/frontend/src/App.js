import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

//импорт шапки
import Header from './components/header/Header.jsx';
//импорт промо
import Promo from './components/promo/Promo.jsx';
//импорт рекламы
import Advert from './components/advert/Advert.jsx';

import SignUp from './components/signup/SignUp.jsx';

function App() {
    return (
      <div className="App">
          <Header />
          <Promo />
          <Advert />
          <SignUp />
      </div>
    );
}


export default App;