import { useState, useEffect } from 'react'
import axios from 'axios';
import { Card, CardBody, CardHeader, Heading, Divider, FormControl, FormLabel, FormHelperText, Button, Input, Box } from '@chakra-ui/react';

function App() {
  const [user, setUser] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
  })

  const handleChange = (event) => {
    setUser({ ...user, [event.target.name]: event.target.value });
  }

  const fetchUser = async (event) => {
    if (event) {
      event.preventDefault();
    }

    try {
      const response = await axios.post("http://127.0.0.1:5000", user, { headers: { 'Content-Type': 'application/json' } });
      console.log(response.data);
      setUser(response.data);

    } catch (error) {
      console.log(error)
    }
  };

  useEffect(() => {
    fetchUser()
  }, [])

  return (
    <Box display='flex' alignItems='center' justifyContent='center' bg="#B1AFFF" height='900px'>
      <Card width='30%' p={5} bg='#640D6B' fontSize='18px' >
        <CardHeader align='center' fontSize='30px' textColor='white'>Login</CardHeader>
        <Divider borderColor='white'></Divider>
        <CardBody justifyContent='center' fontSize='25px' >
          <form onSubmit={fetchUser}>
            <FormLabel textColor='white' fontSize='20px'>First Name</FormLabel>
            <input type='text' name='firstName' value={user.firstName} onChange={handleChange}/>
            <FormLabel textColor='white' fontSize='20px'>Last Name</FormLabel>
            <input type='text' name='lastName' value={user.lastName} onChange={handleChange} />
            <FormLabel textColor='white' fontSize='20px'>Email</FormLabel>
            <input type='text' name='email' value={user.email} onChange={handleChange} />
            <FormLabel textColor='white' fontSize='20px'>Password</FormLabel>
            <input type='password' name='password' value={user.password} onChange={handleChange} />
            <br />
            <Button type='submit' mt={5}>Submit</Button>
          </form>
        </CardBody>
      </Card>
    </Box>
  )
}

export default App
