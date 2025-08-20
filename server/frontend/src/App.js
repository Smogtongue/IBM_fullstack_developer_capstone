import LoginPanel from "./components/Login/Login"
import Register from "./components/Register/Register"
import Dealers from './components/Dealers/Dealers';
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dealers" element={<Dealers/>} />
<<<<<<< HEAD
      <Route path="/dealer/:id" element={<Dealer/>} />
=======
      
>>>>>>> d9dd10bea227ec069d2a6e5e99ce3b1cbcbda389
    </Routes>
  );
}
export default App;
