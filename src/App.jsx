import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios';

function App() {
  const [user, setUser] = useState('')

  const fetchUser = async() => {
    const response = await axios.get("http://127.0.0.1:5000/");
    console.log(response.data);
    setUser(response.data);
  }

  useEffect(() => {
    fetchUser()
  }, [])

  return (
    <>
      <div>
        {user}
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
    </>
  )
}

export default App
