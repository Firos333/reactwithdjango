import React, { Component } from 'react';
// import './Vaccancy.css'
// import FooterPage from './FooterPage.js';

export default class Vaccancy extends Component {
    constructor(props){
        super(props);
    }



    render() {
        return (
            <div className="current">
               <img src={this.props.img}/>
        <h3 className="message" >{this.props.desc}</h3>
                
            </div>
        )
    }
}
