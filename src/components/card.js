import React, { Component } from 'react';

class Card extends Component {
  render() {
    return (
      <div>
        <h1>This is a test of the <code>Card.js</code> class.</h1>
        <p>{this.props.vari}</p>
      </div>
    )
  }
};

export default Card;
