import React, { Component } from 'react';
import Card from './card';

class CardArea extends Component {
  render() {
    return (
      <div className="card-group">
        <Card />
        <Card />
      </div>
    )
  }
};

export default CardArea;
