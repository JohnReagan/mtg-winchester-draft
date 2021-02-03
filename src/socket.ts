import {io} from 'socket.io-client';

// todo dev only
const socket = io('http://localhost:5000');
socket.on('my response', (msg: {data: string}) => {
    console.log(`Received: ${msg.data}`);
});

(() => {
    socket.emit('my event', {data: 'client event'});
    return false;
})();
(() => {
    socket.emit('my broadcast event', {data: 'client broadcast'});
    return false;
})();