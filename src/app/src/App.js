import React, { useState, useEffect } from 'react';
import './App.css';
import logo from './logo.svg';
import axios from 'axios';

export default function App() {
  const [toDoList, setToDoList] = useState([]);
  const [taskName, setTaskName] = useState('');

  const fetchAllTodos = async () => {
    try {
      // hitting get api of backend for getting all tasks
      const response = await axios.get('http://localhost:8000/todos/');
      setToDoList(response.data);
    } catch (error) {
      console.error('Error fetching todos:', error);
    }
  };

  const saveAndFetchAllTodos = async () => {
    try {
      // hitting post api of backend for saving new task
      await axios.post('http://localhost:8000/todos/', { task_name: taskName });
      // fetching updated list of todos
      await fetchAllTodos();
      setTaskName(''); // clear input after adding
    } catch (error) {
      console.error('Error saving todo:', error);
    }
  };

  useEffect(() => {
    fetchAllTodos();
  }, []);

  return (
    <div className="App">
      <div>
        <h1>List of TODOs</h1>
        <ul>
          {toDoList.map((todo, idx) => (
            <li key={idx}>{todo.task_name || 'Unnamed Task'}</li>
          ))}
        </ul>
      </div>
      <div>
        <h1>Create a ToDo</h1>
        <form>
          <div>
            <label htmlFor="todo">ToDo: </label>
            <input
              type="text"
              id="todo"
              value={taskName}
              onChange={e => setTaskName(e.target.value)}
            />
          </div>
          <div style={{ marginTop: '5px' }}>
            <button type="button" onClick={saveAndFetchAllTodos}>Add ToDo!</button>
          </div>
        </form>
      </div>
    </div>
  );
}