import { useState } from 'react';
import RegisterForm from './components/RegisterForm';
import { Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Login from './components/Login';


function App() {
  return (
    <>
      <Routes>
        <Route index element={<RegisterForm/>}/>
        <Route path='/dashboard' element={<Dashboard/>} />
        <Route path='/login' element={<Login/>}/>
      </Routes>
    </>
  )
}

export default App
