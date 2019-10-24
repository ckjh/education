<template>
    <div id="container">
      <div id="terminal"></div>
    </div>
</template>

<script>
import { Terminal } from 'xterm'
import * as attach from 'xterm/lib/addons/attach/attach'
import * as fit from 'xterm/lib/addons/fit/fit'
Terminal.applyAddon(attach)
Terminal.applyAddon(fit)

export default {
    name:'container',
    mounted () {
        let terminalContainer = document.getElementById('terminal')
        this.term = new Terminal(this.terminal)
        this.term.open(terminalContainer)
        // open websocket
        this.terminalSocket = new WebSocket('ws://127.0.0.1:8000/webssh/')
        this.terminalSocket.onopen = function(){
            console.log('websocket is Connected...')
        }
        this.terminalSocket.onclose = function(){
            console.log('websocket is Closed...')
        }
        this.terminalSocket.onerror = function(){
            console.log('damn Websocket is broken!')
        }
        this.term.attach(this.terminalSocket)
        
    // 绑定xterm到ws流中 
    },
    beforeDestroy () {
        this.terminalSocket.close()
        this.term.destroy()
        }
};
</script>