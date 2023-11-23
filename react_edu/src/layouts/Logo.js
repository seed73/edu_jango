import logoImage from "../assets/images/logos/uSfD9Ae8YOjCQGxBMAFaIsTV8.webp";
import { Link } from "react-router-dom";

const Logo = () => {
  return (
    <Link to="/">
      <img src={logoImage} alt="Logo" className="logo-image" />
    </Link>
  );
};

export default Logo;