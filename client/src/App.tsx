import React from "react";

import Controller from "@components/GPIO/Controller";
import "./App.css";
import { SocketProvider } from "@socket";
import Header from "@components/Header";

function App() {
  return (
    <div className="App">
      <SocketProvider>
        <Header />
        <Controller />
      </SocketProvider>
    </div>
  );
}

export default App;
