import React,{useState,useCallback} from 'react';
import ReactJson from 'react-json-view';
import axios from 'axios';
import './index.css';

export default (props) => {


    const [isSending, setIsSending] = useState(false)
    const sendRequest = useCallback(async () => {
      // don't send again while we are sending
      if (isSending) return
      // update state
      setIsSending(true)
      // send the actual request
      axios.get(`http://0.0.0.0:5000/mine`).then(
          window.location.reload()
      )
      // once the request is sent, update state again
      setIsSending(false)
    }, [isSending]) // update the callback if the state changes

    return (
      <button className="miner" type="button" disabled={isSending} onClick={sendRequest}>Mine</button>
    )
  }
