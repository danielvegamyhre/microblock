import logo from './logo.svg';
import './App.css';
import Blockchain from './components/Blockchain';
import Miner from './components/Miner';
import Transactions from './components/Transactions';

function App() {
  return (
    <div className="App">
        <header className="header">
          <h1 className="title">Microblock</h1>
        </header>
      <div>
        <Miner></Miner>
      </div>
      <div className="leftColumn">
        <h2 className="columnHeader">Blockchain</h2>
        <Blockchain />
      </div>
      <div className="rightColumn">
        <h2 className="columnHeader">New Transaction</h2>
        <Transactions />
      </div>
    </div>
  );
}

export default App;
