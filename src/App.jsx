import { useState, useEffect } from 'react'
import axios from 'axios';
// import Form from './components/Form';

function App() {
  const [user, setUser] = useState({
    firstName: '',
    lastName: '',
    email: '',
  })

  const handleChange = (event) => {
    setUser({ ...user, [event.target.name]: event.target.value });
  }

  const fetchUser = async (event) => {
    if (event) {
      event.preventDefault();
    }

    try {
      const response = await axios.post("http://127.0.0.1:5000", user, {headers: {'Content-Type':'application/json'}});
      console.log(response.data);
      setUser(response.data);

    }catch(error) {
      console.log(error)
    }
  };

  useEffect(() => {
    fetchUser()
  }, [])

  return (
    <>
      <form>
      </form>
    </>
  )
}

export default App
