import Index from './pages/Index';
import ForgotPassword from './pages/ForgotPassword';
import Login from './pages/Login';
import Register from './pages/Register';
import NoFound from './pages/NoFound';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Index/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/forgotpassword' element={<ForgotPassword/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path="#" element={<NoFound/>} />
      </Routes>
    </BrowserRouter>  
  );
}

export default App;