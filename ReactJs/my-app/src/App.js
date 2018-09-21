import React, { Component } from 'react';
import './App.css';

class Tab extends Component{
  render(){
    return(
      <button onClick={()=>this.props.onClick()} class="button-tab">{this.props.value}</button>
    );
  }
}

class Square extends Component{
  render(){
    return(
      <div className="square">{this.props.value}  </div>
    )
  }
}

class App extends Component {
  constructor(){
    super();

    this.state={
      MenuType: 0,
      AnimationType: 0,
      AnimationArray: [],
      Count: 0
    }

    this.playInsertionSort = this.playInsertionSort.bind(this);
  }

  showSortingMenu() {
    this.setState({MenuType:1}
    );
  }

  showSearchingMenu() {
    this.setState({MenuType:2}
    );
  }

  playInsertionSort(){
    this.setState({Count: 0})
    fetch('http://127.0.0.1:5000/api/algorithm/InsertionSort')
    .then(results=>{
      return results.json()
    }).then(data=>{
      this.setState({AnimationType:1, AnimationArray:data});

    })

    var timesRun=0
    var interval=setInterval(() => {
        this.tick();
        timesRun += 1;
        if(timesRun==this.state.AnimationArray.length-1){
          clearInterval(interval);
        }
        console.log(1);
      }, 1000);
    }

  renderMenu(x){
    switch(x) {
      case 0:
        return (
          <div className="btn-group">
            <Tab value={"Sorting"} onClick={() => this.setState({MenuType:1})}/>
            <Tab value={"Searching"} onClick={() => this.setState({MenuType:2})}/>
            <Tab value={"Linked List"} onClick={() => this.setState({MenuType:3})}/>
          </div>
        );
      case 1:
      return (
        <div className="dropdown-content">
          <Tab value={"Back"} onClick={() => this.setState({MenuType:0, AnimationType:0})}/>
          <Tab value={"Insertion Sort"} onClick={() => this.playInsertionSort()}/>
          <Tab value={"Merge Sort"}/>
        </div>
      );
      case 2:
      return (
        <div className="dropdown-content">
          <Tab value={"Back"} onClick={() => this.setState({MenuType:0})}/>
          <Tab value={"Random Search"}/>
        </div>
      );
      case 3:
      return (
        <div className="dropdown-content">
          <Tab value={"Back"} onClick={() => this.setState({MenuType:0})}/>
          <Tab value={"Single Linked List"}/>
          <Tab value={"Double Linked List"}/>
        </div>
      );
      default:
        return 'foo';
      }
  }

  tick() {
    this.setState(prevState => {
       return {Count: prevState.Count + 1}
    });
    this.forceUpdate();
    console.log(this.state.Count)
  }

  renderAnimation(x){
    switch(x) {
      case 0:
        return (
          <p>Click on any button to show the animation of the algorithm</p>
        );

      case 1:
      return (
        <div className="arrays">
          <Square value={this.state.AnimationArray[this.state.Count][0]}/>
          <Square value={this.state.AnimationArray[this.state.Count][1]}/>
          <Square value={this.state.AnimationArray[this.state.Count][2]}/>
          <Square value={this.state.AnimationArray[this.state.Count][3]}/>
          <Square value={this.state.AnimationArray[this.state.Count][4]}/>
          <Square value={this.state.AnimationArray[this.state.Count][5]}/>
          <Square value={this.state.AnimationArray[this.state.Count][6]}/>
          <Square value={this.state.AnimationArray[this.state.Count][7]}/>
          <Square value={this.state.AnimationArray[this.state.Count][8]}/>
          <Square value={this.state.AnimationArray[this.state.Count][9]}/>
        </div>
      );

      default:
        return 'foo';
      }
  }


  render() {
    return (
    <div className="content">
      <div className="Left">
        {this.renderAnimation(this.state.AnimationType)}
      </div>
      <div className="Right">
        {this.renderMenu(this.state.MenuType)}
      </div>
    </div>
  );
  }
}

export default App;
