import React, { useState } from 'react';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    if (!inputValue) return;
    const newTask = {
      text: inputValue,
      completed: false
    };
    setTasks([...tasks, newTask])
    setInputValue('');
  };

  const handleTaskClick = (index) => {
    const newTasks = [...tasks];
    newTasks[index].completed = !newTasks[index].completed;
    setTasks(newTasks);
  };

  const handleTaskRemove = (index) => {
    const newTasks = [...tasks];
    newTasks.splice(index, 1);
    setTasks(newTasks);
  };

  return (
    <div className="container">
      <h1 className="title">Tasks</h1>
      <form onSubmit={handleFormSubmit}>
        <input type="text" value={inputValue} onChange={handleInputChange} placeholder="Add task..." className="input-task" />
        <button type="submit" className="button-add">Add</button>
      </form>
      <ul>
        {tasks.map((task, index) => (
          <li key={index} className="task-item" onClick={() => handleTaskClick(index)}>
            <input type="checkbox" checked={task.completed} className="task-checkbox" />
            <span className="task-text">{task.text}</span>
          </li>
        ))}
      </ul>
      <button className="button-clear" onClick={() => setTasks([])}>Clear</button>
    </div>
  );
}

export default App;
