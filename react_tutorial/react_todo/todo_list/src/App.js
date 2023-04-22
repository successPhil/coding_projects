import { useState } from 'react';
import './App.css';

function App() {
  const [taskList, setTaskList] = useState([]);

  const handleAddTask = (e) => {
    e.preventDefault();
    const taskInput = document.getElementById('task-input');
    const newTask = taskInput.value.trim();
    if (newTask !== '') {
      setTaskList([...taskList, { task: newTask, completed: false }]);
      taskInput.value = '';
    }
  };

  const handleDeleteTask = (taskIndex) => {
    const newTaskList = [...taskList];
    newTaskList.splice(taskIndex, 1);
    setTaskList(newTaskList);
  };

  const handleClearList = () => {
    setTaskList([]);
  };

  const handleTaskCompletion = (taskIndex) => {
    const newTaskList = [...taskList];
    newTaskList[taskIndex].completed = !newTaskList[taskIndex].completed;
    setTaskList(newTaskList);
  };

  return (
    <div className="body">
      <div className="container">
        <h1 className="title">To-Do List</h1>
        <form onSubmit={handleAddTask}>
          <input
            type="text"
            id="task-input"
            className="input-task"
            placeholder="Add a task..."
            required
          />
          <button type="submit" className="button-add">
            Add
          </button>
        </form>
        <ul className="list">
          {taskList.map((taskObj, taskIndex) => (
            <li className="task-item" key={taskIndex}>
              <input
                type="checkbox"
                className="task-checkbox"
                checked={taskObj.completed}
                onChange={() => handleTaskCompletion(taskIndex)}
              />
              <p
                className={`task-text ${taskObj.completed ? 'completed' : ''}`}
              >
                {taskObj.task}
              </p>
              <button
                className="task-remove"
                onClick={() => handleDeleteTask(taskIndex)}
              >
                X
              </button>
            </li>
          ))}
        </ul>
        <button className="button-clear" onClick={handleClearList}>
          Clear List
        </button>
      </div>
    </div>
  );
}

export default App;
