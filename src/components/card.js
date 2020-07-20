import React, { Component } from 'react';

class Card extends Component {
  render() {
    return (
      <div className="card">
        <img src="" />
        <div className="card-body">
          <h5 className="card-title">CardTitle</h5>
          <p className="card-text">Lorem Ipsum lol</p>
          <a className="btn btn-primary">Button</a>
        </div>
      </div>
    )
  }
};

export default Card;
