import React, { useState, useEffect } from "react";
import axios from 'axios';
import { Box, Card, CardHeader, CardBody, Divider, FormLabel, Button } from '@chakra-ui/react';

const RegisterForm = () => {
    const [userData, setUserData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        username: '',
        password: ''
    });

    const handleChange = (event) => {
        setUserData({ ...userData, [event.target.name]: event.target.value });  //Creating a new object based on the existing userData updated by the changed field event.target.name with the new value event.target.value 
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:5000/register', JSON.stringify(userData), { headers: { 'Content-Type': 'application/json' } });
            console.log("FROM REACT", response);
        } catch (error) {
            console.log('Error registering user:', error);
        }
    };

    return (
        <Box display='flex' alignItems='center' justifyContent='center' bg="#B1AFFF" height='900px'>
            <Card width='30%' p={5} bg='#640D6B' fontSize='18px'>
                <CardHeader align='center' fontSize='30px' textColor='white'>Register</CardHeader>
                <Divider borderColor='white'></Divider>
                <CardBody>
                    <form onSubmit={handleSubmit}>
                        <FormLabel textColor='white' fontSize='20px'>First Name:</FormLabel>
                        <input type="text" name="first_name" value={userData.first_name} onChange={handleChange} />
                        <FormLabel textColor='white' fontSize='20px'>Last Name:</FormLabel>
                        <input type="text" name="last_name" value={userData.last_name} onChange={handleChange} />
                        <FormLabel textColor='white' fontSize='20px'>Email:</FormLabel>
                        <input type="email" name="email" value={userData.email} onChange={handleChange} />
                        <FormLabel textColor='white' fontSize='20px'>Username:</FormLabel>
                        <input type="text" name="username" value={userData.username} onChange={handleChange}/>
                        <FormLabel textColor='white' fontSize='20px'>Password:</FormLabel>
                        <input type="password" name="password" value={userData.password} onChange={handleChange} />
                        <br /> <br />
                        <Button type="submit">Submit</Button>
                    </form>
                </CardBody>
            </Card>
        </Box>
    );
};

export default RegisterForm;
