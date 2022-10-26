//import express from "express";
import morgan from "morgan";
// Routes
import acudienteRoutes from "./routes/acudiente.routes";

const express=require('express');
const cors = require('cors');
const app = express();
app.use(express.json());
app.use(cors());

// Settings
app.set("port", 4000);

// Middlewares
app.use(morgan("dev"));

// Routes
app.use("/", acudienteRoutes);
app.use("/api/acudiente", acudienteRoutes);  

export default app;