import { useParams, useNavigate } from "react-router-dom";
import { useEffect } from "react";
import axios from "axios";

const AccountConfirmation = () => {
    const {token} = useParams();
    const navigate = useNavigate();
    
    useEffect (() => {
        const confirmEmail = async () => {
            try{
                const response = await axios.get(`/api/confirm?token=${token}`);
                console.log('Response data:', response.data);

                if (response.data.success) {
                    console.log('Email confirmed, redirecting to dashboard...')
                    navigate(response.data.redirect_url);
                } else {
                    console.log('Email confirmation failed');
                }
            }catch (error) {
                console.log('Error extracting email',error)
            }
        };
        confirmEmail();
    }, [token, navigate]);

    return(
        <div>
            <p>Confirming your email...</p>
        </div>
    )
}

export default AccountConfirmation;