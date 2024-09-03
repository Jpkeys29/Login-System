import { useEffect, useState } from "react";


const ToDoList = () => {
    const [task, setTask] = useState('')
    const [newTasks, setNewTasks] = useState([]);
    const newId = newTasks.length + 1;

    function handleAddTask() {
        if (task !== '') {
            setNewTasks(prevTask => [...prevTask, { id: newId, task }])
        }
        setTask('');  //Clear input after adding task
    }

    const handleChange = (e) => {
        setTask(e.target.value)
    }

    return (
        <div>
            <textarea value={task} onChange={handleChange}/>
            <br/>
            <button onClick={handleAddTask}>Add Task</button>
            <ul>
                {newTasks.map(task => (
                    <li key={task.id}>{task.task}</li>
                ))}
            </ul>
        </div>
    )
}

export default ToDoList;