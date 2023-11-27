import { iaType } from "../constantes.js";
import { Render } from "../render.js";
import { obtenerIAsByType } from "./getIAsByType.js";

const iasByFunction = new Render("iaByFunctionList");
iasByFunction.fetchData(iaType, obtenerIAsByType);