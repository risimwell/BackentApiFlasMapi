import { getConnection } from "../database/database";

const getacudientes = async (req, res) => {
    try {
        const connection = await getConnection();
        const result = await connection.query("SELECT * FROM acudiente");
        res.json(result);
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

const getacudiente = async (req, res) => {
    try {
        const {cedula_acudiente} = req.params;
        const connection = await getConnection();
        const result = await connection.query("SELECT * FROM acudiente WHERE cedula_acudiente=?",cedula_acudiente);
        res.json(result);
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

const addacudiente = async (req, res) => {
    console.log(req.body);
    try {
        const { cedula_acudiente,nombre,apellido,telefono,clave } = req.body;

        if (cedula_acudiente === undefined || nombre === undefined || apellido === undefined|| telefono === undefined|| clave === undefined) {
            res.status(400).json({ message: "Alguno de los datos estan vacio" });
        }
        else{
            const acudiente = { cedula_acudiente,nombre,apellido,telefono,clave };
            const connection = await getConnection();
            await connection.query("INSERT INTO acudiente SET ?", acudiente);
            res.json({ message: "Usuaro añadido" });
        }
        
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

const updateacudiente = async (req, res) => {
    try {
        const { cedula_acudiente } = req.params;
        const { nombre,apellido,telefono,clave } = req.body;

        if (cedula_acudiente === undefined || nombre === undefined || apellido === undefined|| telefono === undefined|| clave === undefined) {
            res.status(400).json({ message: "Alguno de los datos estan vacio" });
        }else{
            const acudiente = { cedula_acudiente,nombre,apellido,telefono,clave };
            const connection = await getConnection();
            const result = await connection.query("UPDATE acudiente SET ? WHERE cedula_acudiente = ?", [acudiente, cedula_acudiente]);
            res.json(result,{ message: "Usuaro Actualizado" });
        }

    } catch (error) {
        res.status(500);
        res.send(error.message,{ message: "El usuario no fue actualizado" });
    }
};

const deleteacudiente = async (req, res) => {
    try {
        const { cedula_acudiente } = req.params;
        const connection = await getConnection();
        const result = await connection.query("DELETE FROM acudiente WHERE cedula_acudiente = ?", cedula_acudiente);
        res.json(result,{ message: "Usuaro eliminado" });
    } catch (error) {
        res.status(500);
        res.send(error.message,{ message: "No se pudo eliminar el usuario" });
    }
};

export const methods = {
    getacudientes,
    getacudiente,
    addacudiente,
    updateacudiente,
    deleteacudiente
};
