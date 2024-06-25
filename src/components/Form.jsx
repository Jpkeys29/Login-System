function Form({ user, setUser }) {
    
    return (
        <div>
            {user.First_name}
            {user.Last_name}
            {user.Email}
        </div>
    )
}

export default Form;