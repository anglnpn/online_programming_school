import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

class App extends Component{
  state = {
    courses: [], // Изменил на множественное число для ясности, предполагается, что это массив курсов
  }

  componentDidMount(){
    let data;
    axios.get('http://localhost:8000/list/')
      .then(res => {
        data = res.data;
        this.setState({
          courses: data // Устанавливаю состояние напрямую с данными ответа
        });
      })
      .catch(error => {
        console.error('Ошибка загрузки данных:', error);
      });
  }
//вывести 1 элемент
  render() {
    return (
      <div>
        <header>Список курсов</header>
        <hr></hr>
        {this.state.courses.map((course, id) => (
          <div>
            <h1>{id}</h1>
              <h2>{course.name_course}</h2>
                <p>{course.description}</p>
          </div>
        ))}
      </div>
    )
  }
}

export default App;

