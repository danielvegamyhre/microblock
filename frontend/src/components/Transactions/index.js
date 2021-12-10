import axios from 'axios';
import React from 'react';
import './index.css';

export default class TransactionForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
          'current_transaction': { sender: '', recipient:'', amount: 0.0 },
          'unvalidated_transactions': [],
      }
    }

    componentDidMount() {
        axios.get('http://0.0.0.0:5000/transactions')
          .then(res => {
            this.setState({unvalidated_transactions: res.data });
          })
      }

    handleChange = (event) => {
      this.state.current_transaction[event.target.name] = event.target.value;
    }

    handleSubmit = (event) => {
      fetch('http://0.0.0.0:5000/transactions/new', {
          method: 'POST',
          body: JSON.stringify(this.state.current_transaction),
        }
      ).then(function(response) {
          console.log(response)
          return response.json();
        });

      event.preventDefault();
      window.location.reload();
  }

    render() {
      return (
          <div>
        <form onSubmit={this.handleSubmit}>
          <label class="transactionLabel">
            Sender
            <input class="transactionField" type="text" value={this.state.current_transaction.sender.value} name="sender" onChange={this.handleChange} />
           </label>
           <br/>
           <label class="transactionLabel">
                Recipient
                <input class="transactionField" type="text" value={this.state.current_transaction.recipient.value} name="recipient" onChange={this.handleChange} />
            </label>
            <br/>
            <label class="transactionLabel">
                Amount
                <input class="transactionField" type="text" value={this.state.current_transaction.amount.value} name="amount" onChange={this.handleChange} />
              </label>
              <br/>
          <input class="submitButton" type="submit" value="Submit" />
        </form>

        <h2>Unvalidated Transactions</h2>
        <table className="table">
            <thead>
                <tr className="table-row">
                    <th>From</th>
                    <th>To</th>
                    <th>Amount</th>
                </tr>
            </thead>
            <tbody>
                { this.state.unvalidated_transactions.map(t =>
                    <tr key={t}>
                        <td><b style={{color: 'green'}}>{t.sender}</b></td>
                        <td><b style={{color: 'green'}}>{t.recipient}</b></td>
                        <td><b style={{color: 'green'}}>{parseFloat(t.amount).toFixed(5)} </b></td>
                    </tr>
                    )
                }
            </tbody>
            </table>
        </div>
      );
    }
  }
