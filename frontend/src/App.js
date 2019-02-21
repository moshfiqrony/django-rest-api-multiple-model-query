import React, { Component } from 'react';
import axios from 'axios'
import 'antd/dist/antd.css'
import ShowData from './ShowData'

class App extends Component {
  constructor(){
    super();
    this.state = {
      cl: [],
  }}

  componentDidMount(){
    axios.get('http://127.0.0.1:8000/api/campaignDetails/')
    .then(res => this.setState({
      cl: res.data
    }))
  }


  render() {
    return (
      <div>
        <ShowData/>
      </div>
    );
  }
}

export default App;
