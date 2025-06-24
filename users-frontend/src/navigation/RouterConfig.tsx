import { Routes, Route } from "react-router";
import { URLS } from "./CONTANTS";
import { LoginForm } from "../pages/LoginForm";
import { RegisterForm } from "../pages/RegisterForm";
import { AdminUsuarios } from "../pages/AdminUsuarios";

const RouterConfig = () => (
  <Routes>
    <Route path={URLS.LOGIN} element={<LoginForm />} />
    <Route path={URLS.REGISTER} element={<RegisterForm />} />
    <Route path={URLS.USUARIOS_ADMIN} element={<AdminUsuarios />} />

  </Routes>
);

export default RouterConfig;