import React, { Component } from 'react';
import './App.css';

class Tab extends Component{
  render(){
    return(
      <button onClick={()=>this.props.onClick()} class="button-tab">{this.props.value}</button>
    );
  }
}

class App extends Component {
  constructor(){
    super();

    this.state={
      MenuType: 0
    }

    this.showSortingMenu = this.showSortingMenu.bind(this);
    this.showSearchingMenu = this.showSearchingMenu.bind(this);
  }

  showSortingMenu() {
    this.setState({MenuType:1}
    );
  }

  showSearchingMenu() {
    this.setState({MenuType:2}
    );
  }

  renderSwitch(x){
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
          <Tab value={"Back"} onClick={() => this.setState({MenuType:0})}/>
          <Tab value={"Insertion Sort"}/>
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

  render() {
    console.log(this.state.MenuType)
    return (
    <div className="content">
      <div className="Left">
        <p>Click on any button to show the animation of the algorithm</p>
      </div>
      <div className="Right">
        {this.renderSwitch(this.state.MenuType)}
      </div>
    </div>
  );
  }
}

export default App;
