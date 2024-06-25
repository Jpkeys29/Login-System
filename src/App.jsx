import { useState, useEffect } from 'react'
import axios from 'axios';
import Form from './components/Form';

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
        <Form user={user}/>
      </div>
    </>
  )
}

export default App
