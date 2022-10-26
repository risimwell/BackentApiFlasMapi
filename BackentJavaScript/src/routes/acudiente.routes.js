import { Router } from "express";
import { methods as acudienteController } from "../controllers/acudiente.controller";

const router = Router();

router.get("/", acudienteController.getacudientes);
router.get("/:id", acudienteController.getacudiente);
router.post("/", acudienteController.addacudiente);
router.put("/:id", acudienteController.updateacudiente);
router.delete("/:id", acudienteController.deleteacudiente);

export default router;