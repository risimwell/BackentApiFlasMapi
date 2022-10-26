import { getConnection } from "../database/database";

const getdocentes = async (req, res) => {
    try {
        const connection = await getConnection();
        const result = await connection.query("SELECT * FROM docente");
        res.json(result);
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

const getdocente = async (req, res) => {
    try {
        const {cedula_docente} = req.params;
        const connection = await getConnection();
        const result = await connection.query("SELECT * FROM docente WHERE cedula_docente=?",cedula_docente);
        res.json(result);
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

const adddocente = async (req, res) => {
    console.log(req.body);
    try {
        const { cedula_docente,nombre,apellido,telefono,clave } = req.body;

        if (cedula_docente === undefined || nombre === undefined || apellido === undefined|| telefono === undefined|| clave === undefined) {
            res.status(400).json({ message: "Alguno de los datos estan vacio" });
        }
        else{
            const docente = { cedula_docente,nombre,apellido,telefono,clave };
            const connection = await getConnection();
            await connection.query("INSERT INTO docente SET ?", docente);
            res.json({ message: "Usuaro añadido" });
        }
        
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

const updatedocente = async (req, res) => {
    try {
        const { cedula_docente } = req.params;
        const { nombre,apellido,telefono,clave } = req.body;

        if (cedula_docente === undefined || nombre === undefined || apellido === undefined|| telefono === undefined|| clave === undefined) {
            res.status(400).json({ message: "Alguno de los datos estan vacio" });
        }else{
            const docente = { cedula_docente,nombre,apellido,telefono,clave };
            const connection = await getConnection();
            const result = await connection.query("UPDATE docente SET ? WHERE cedula_docente = ?", [docente, cedula_docente]);
            res.json(result,{ message: "Usuaro Actualizado" });
        }

    } catch (error) {
        res.status(500);
        res.send(error.message,{ message: "Algo esta mal en el update" });
    }
};

const deletedocente = async (req, res) => {
    try {
        const { cedula_docente } = req.params;
        const connection = await getConnection();
        const result = await connection.query("DELETE FROM docente WHERE cedula_docente = ?", cedula_docente);
        res.json(result,{ message: "Usuaro eliminado" });
    } catch (error) {
        res.status(500);
        res.send(error.message,{ message: "No se pudo eliminar el usuario" });
    }
};

export const methods = {
    getdocentes,
    getdocente,
    adddocente,
    updatedocente,
    deletedocente
};
