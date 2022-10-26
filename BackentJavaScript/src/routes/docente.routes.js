import { Router } from "express";
import { methods as docenteController } from "../controllers/docente.controller";

const router = Router();

router.get("/", docenteController.getdocentes);
router.get("/:id", docenteController.getdocente);
router.post("/", docenteController.adddocente);
router.put("/:id", docenteController.updatedocente);
router.delete("/:id", docenteController.deletedocente);

export default router;