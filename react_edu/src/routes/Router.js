import { lazy } from "react";
import { Navigate } from "react-router-dom";
import { ProtectedRoute } from "./ProtectedRoute.js";
import { isAuthenticated } from '../utils/auth.js';

/****Layouts*****/
const FullLayout = lazy(() => import("../layouts/FullLayout.js"));

/***** Pages ****/

const Starter = lazy(() => import("../views/Starter.js"));
const About = lazy(() => import("../views/About.js"));
const Alerts = lazy(() => import("../views/ui/Alerts"));
const Badges = lazy(() => import("../views/ui/Badges"));
const Buttons = lazy(() => import("../views/ui/Buttons"));
const Cards = lazy(() => import("../views/ui/Cards"));
const Grid = lazy(() => import("../views/ui/Grid"));
const Tables = lazy(() => import("../views/ui/Tables"));
const Forms = lazy(() => import("../views/ui/Forms"));
const Breadcrumbs = lazy(() => import("../views/ui/Breadcrumbs"));
const Aaaa = lazy(() => import("../views/ui/aaaa.js"));


const Main = lazy(() => import("../views/ui/Main.js"));
const LoginPage = lazy(() => import("../views/ui/LoginPage.js"));

/*****Routes******/

const ThemeRoutes = [
  {
    path: "/",
    element: <FullLayout />,
    children: [
      { path: "/", element: <Navigate to="/main" /> },
      { path: "/main", exact: true, element: <ProtectedRoute><Main /></ProtectedRoute> },
      { path: "/main2", exact: true, element: <Main /> },
      { path: "/starter", exact: true, element: <Starter /> },
      { path: "/student", exact: true, element: <Starter /> },
      { path: "/schedule", exact: true, element: <Starter /> },
      { path: "/about", exact: true, element: <About /> },
      { path: "/alerts", exact: true, element: <Alerts /> },
      { path: "/badges", exact: true, element: <Badges /> },
      { path: "/buttons", exact: true, element: <Buttons /> },
      { path: "/cards", exact: true, element: <Cards /> },
      { path: "/grid", exact: true, element: <Grid /> },
      { path: "/table", exact: true, element: <Tables /> },
      { path: "/forms", exact: true, element: <Forms /> },
      { path: "/breadcrumbs", exact: true, element: <Breadcrumbs /> },
      { path: "/aaaa", exact: true, element: <Aaaa /> },
    ],
  },
  { 
    path: "/login",
    element: isAuthenticated() ? <Navigate to="/main" /> : <LoginPage />,
    exact: true,
  },
];

export default ThemeRoutes;