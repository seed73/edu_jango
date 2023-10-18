import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import './App.css';

function Page1() {
  return <div>페이지 1</div>;
}

function Page2() {
  return <div>페이지 2</div>;
}

function Page3() {
  return <div>페이지 3</div>;
}

function Page4() {
  return <div>페이지 4</div>;
}

function App() {
  const [activePage, setActivePage] = useState('1');

  return (
    <Router>
      <div className="container">
        <aside className="sidebar">
          <ul>
            <li>
              <Link to="/1" className={activePage === '1' ? 'active' : ''} onClick={() => setActivePage('1')}>1</Link>
            </li>
            <li>
              <Link to="/2" className={activePage === '2' ? 'active' : ''} onClick={() => setActivePage('2')}>2</Link>
            </li>
            <li>
              <Link to="/3" className={activePage === '3' ? 'active' : ''} onClick={() => setActivePage('3')}>3</Link>
            </li>
            <li>
              <Link to="/4" className={activePage === '4' ? 'active' : ''} onClick={() => setActivePage('4')}>4</Link>
            </li>
          </ul>
        </aside>
        <main className="main-content">
          <Route path="/1" component={Page1} />
          <Route path="/2" component={Page2} />
          <Route path="/3" component={Page3} />
          <Route path="/4" component={Page4} />
        </main>
      </div>
    </Router>
  );
}

export default App;