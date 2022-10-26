import { config } from "dotenv";

config();

export default {
    host: process.env.HOST || "",
    database: process.env.DATABASE || "",
    acudiente: process.env.acudiente || "",
    password: process.env.PASSWORD || ""
};
