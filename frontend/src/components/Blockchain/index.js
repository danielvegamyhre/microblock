import React,{useState} from 'react';
import ReactJson from 'react-json-view';
import axios from 'axios';

export default class Blockchain extends React.Component {
    constructor(props) {
        super(props);
        this.state = {"blockchain": []};
    }

    refreshData () {
        axios.get(`http://0.0.0.0:5000/chain`)
        .then(res => {
            this.setState({ blockchain: res.data });
        })
    }

    componentDidMount() {
        this.refreshData();
    }

    render() {
        return (
            <div>
                <ReactJson src={this.state} theme="tube"/>
            </div>
        )
    }
}
