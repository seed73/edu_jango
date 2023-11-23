import { useRoutes } from "react-router-dom";
import Themeroutes from "./routes/Router";
import "./layouts/layouts.css";
import './loginPage.css';

const App = () => {
  const routing = useRoutes(Themeroutes);

  return <div className="dark">{routing}</div>;
};

export default App;
